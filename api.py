import os
from dotenv import load_dotenv

load_dotenv()


API_KEY = {
  'apiKey': f"{os.getenv('apikey')}",
  'authDomain': f"{os.getenv('authDomain')}",
  'projectId': f"{os.getenv('projectId')}",
  'storageBucket': f"{os.getenv('storageBucket')}",
  'messagingSenderId': f"{os.getenv('messagingSenderId')}",
  'appId': f"{os.getenv('appId')}",
  'measurementId': f"{os.getenv('measurementId')}",
  'databaseURL': f"{os.getenv('databaseURL')}"
}

