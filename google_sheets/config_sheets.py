from googleapiclient.discovery import build
import os
from google.oauth2 import service_account

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SERVICE_ACCOUNT_FILE = os.path.join(PROJECT_DIR, 'secrets', 'atmoscargo.json')

creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=['https://www.googleapis.com/auth/spreadsheets']
)

service = build('sheets', 'v4', credentials=creds)
google_sheets_id_users = '16peTXU4MyS3qiM0yH_dMXqw8mKDx2j5BQfg_oG1nhRc'