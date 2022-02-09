import * as firebase from 'firebase/app';
import 'firebase/auth';

var firebaseConfig = {
    apiKey: "AIzaSyDkBLgQekrqF0kCU8uVgzLXIi7aGUyBmz8",
    authDomain: "abizer-general-projects.firebaseapp.com",
    databaseURL: "https://abizer-general-projects.firebaseio.com",
    projectId: "abizer-general-projects",
    storageBucket: "abizer-general-projects.appspot.com",
    messagingSenderId: "523317994078",
    appId: "1:523317994078:web:64ab1f5c3d6c35ad088acf"
};

const app = firebase.initializeApp(firebaseConfig)

export default app