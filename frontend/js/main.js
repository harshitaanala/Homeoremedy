// setting up firebase with our website
const firebaseConfig = {
    apiKey: "AIzaSyBbke5QsgaK28tYxEOlHsTJckvdld-Vhp0",
    authDomain: "praxis-23.firebaseapp.com",
    projectId: "praxis-23",
    storageBucket: "praxis-23.appspot.com",
    messagingSenderId: "385659931354",
    appId: "1:385659931354:web:bc18f42e30b312c4e333e3"
  };
const firebaseApp = firebase.initializeApp(firebaseConfig);
const db = firebaseApp.firestore();
const auth = firebaseApp.auth();

const signUp = () => {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    console.log(email, password)
    firebase.auth().createUserWithEmailAndPassword(email, password)
        .then((result) => {
            window.location.href = "main.html";
            console.log(result)
        })
        .catch((error) => {
            console.log(error.code);
            console.log(error.message)
        });
}

const signIn = () => {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    firebase.auth().signInWithEmailAndPassword(email, password)
        .then((result) => {
            window.location.href = "main.html";
            console.log(result)
        })
        .catch((error) => {
            console.log(error.code);
            console.log(error.message)
        });
}