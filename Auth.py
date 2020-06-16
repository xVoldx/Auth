import pyrebase
from getpass import getpass


# Log the user in
def Login():
    try:
        firebaseConfig = {
            "apiKey": "xxx",
            "authDomain": "xxx",
            "databaseURL": "xxx",
            "projectId": "xxx",
            "storageBucket": "xxx",
            "messagingSenderId": "xxx",
            "appId": "xxx",
            "measurementId": "xxx"
        }
        firebase = pyrebase.initialize_app(firebaseConfig)
        auth = firebase.auth()
        email = input("Please Enter Your Email Address : \n> ")
        password = getpass("Please Enter Your Password : \n> ")
        login = auth.sign_in_with_email_and_password(email, password)
        # Get account information
        info = auth.get_account_info(login['idToken'])
        print("Success ... ")
    except Exception as e:
        print('EMAIL_NOT_FOUND or INVALID_PASSWORD ...')
        f = open('Error.log', 'a+')
        f.write(str(e)+'\n\n')
        exit()

# Creating users
def Create():
    try:
        firebaseConfig = {
            "apiKey": "xxx",
            "authDomain": "xxx",
            "databaseURL": "xxx",
            "projectId": "xxx",
            "storageBucket": "xxx",
            "messagingSenderId": "xxx",
            "appId": "xxx",
            "measurementId": "xxx"
        }
        firebase = pyrebase.initialize_app(firebaseConfig)
        auth = firebase.auth()
        email = input("Please Enter Your Email Address : \n> ")
        password = getpass("Please Enter Your Password : \n> ")
        user = auth.create_user_with_email_and_password(email, password)
        print("Success .... ")
    except Exception as e:
        print('EMAIL_EXISTS ...')
        f = open('Error.log', 'a+')
        f.write(str(e)+'\n\n')
        exit()

# Sending password reset emails
def Reset():
    try:
        firebaseConfig = {
            "apiKey": "xxx",
            "authDomain": "xxx",
            "databaseURL": "xxx",
            "projectId": "xxx",
            "storageBucket": "xxx",
            "messagingSenderId": "xxx",
            "appId": "xxx",
            "measurementId": "xxx"
        }
        firebase = pyrebase.initialize_app(firebaseConfig)
        auth = firebase.auth()
        email = input("Please Enter Your Email Address : \n> ")
        auth.send_password_reset_email(email)
        print("Success ... ")
    except Exception as e:
        print('EMAIL_NOT_FOUND ...')
        f = open('Error.log', 'a+')
        f.write(str(e)+'\n\n')
        exit()
