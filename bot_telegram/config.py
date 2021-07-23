import os
import dotenv
import json


dotenv.load_dotenv()

TOKEN = os.getenv("TOKEN")
PASSWORD = os.getenv("email_password")
HOST = os.getenv("HOST")
EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAILS_TO = json.loads(os.getenv("EMAILS_TO"))

