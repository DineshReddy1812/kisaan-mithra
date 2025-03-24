// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/11.5.0/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/11.5.0/firebase-analytics.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyC-1yQL5ufMf-GPwBAN8H_GYGL6andB36g",
  authDomain: "kisaan-mitra-a0e8f.firebaseapp.com",
  projectId: "kisaan-mitra-a0e8f",
  storageBucket: "kisaan-mitra-a0e8f.firebasestorage.app",
  messagingSenderId: "28889998059",
  appId: "1:28889998059:web:e5995a6ef5ef818c8714ae",
  measurementId: "G-EL950HE3PD"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

// Initialize Firebase
const email=document.getElementById('register-email').value;
const password=document.getElementById('register-password').value;
const login=document.getElementById('login');
login.addEventListener('click',(e)=>{
    e.preventDefault();
    firebase.auth().signInWithEmailAndPassword(email, password)
  .then((userCredential) => {
    // Signed in
    var user = userCredential.user;
    console.log(user);
    // ...
  })
  .catch((error) => {
    var errorCode = error.code;
    var errorMessage = error.message;
    console.log(errorMessage);
  });
})