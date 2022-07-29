import pyrebase

from api import API_KEY

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

firebase_instance = pyrebase.initialize_app(API_KEY)

auth = firebase_instance.auth()


def login(username, password):
    try:
        auth.sign_in_with_email_and_password(username, password)
        return True
    except:
        return False
