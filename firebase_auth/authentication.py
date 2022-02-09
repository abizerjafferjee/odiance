import os
import json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone

import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials

with open(os.path.join(BASE_DIR, 'firebase_auth/abizer-general-projects-firebase.json')) as cert_file:
    cert = json.load(cert_file)

from rest_framework import authentication
from rest_framework import exceptions

cred = credentials.Certificate(cert)

default_app = firebase_admin.initialize_app(cred)

class FirebaseAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        if not auth_header:
            raise NoAuthToken("No auth token provided")

        id_token = auth_header.split(" ").pop()
        decoded_token = None
        try:
            decoded_token = auth.verify_id_token(id_token)
        except Exception:
            raise InvalidAuthToken("Invalid auth token")

        if not id_token or not decoded_token:
            return None

        try:
            uid = decoded_token.get("uid")
        except Exception:
            raise FirebaseError()

        user, created = User.objects.get_or_create(username=uid)
        user.profile.last_activity = timezone.localtime()

        return (user, None)