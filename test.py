import pyrebase

firebaseConfig = {'apiKey': "AIzaSyDdksFXF_bDbBIYi7Nvpeo8YQvJW80U27s",
    'authDomain': "test-case-88b02.firebaseapp.com",
    'projectId': "test-case-88b02",
    'storageBucket' : "test-case-88b02.appspot.com",
    'messagingSenderId' : "222151653121",
    'appId': "1:222151653121:web:297b4d553a246ce22dcd00"}

firebase = pyrebase.initialize_app(firebaseConfig)

# db = firebase.database()

auth = firebase.auth()

# storage = firebase.storage()


email = input("Enter Your Email: ")
password = input("Enter Your Password: ")
try:
    auth.sign_in_with_email_and_password(email,password)
    print("Logged In Succesfully.")
except:
    print("Invalid User or password, Try Again!")








