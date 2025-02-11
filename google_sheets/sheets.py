import logging
import time
from googleapiclient.errors import HttpError
from google_sheets.config_sheets import service, google_sheets_id_users

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def update_google_sheets(code: str, fullname: str, phone: str):
    logger.info(f"Attempting to save: {code}, {fullname}, {phone}")
    range_name = "Клиенты!A:C"
    row = [code, fullname, phone]

    for attempt in range(3):  # Retry logic
        try:
            assert isinstance(service.spreadsheets().values().append(
                spreadsheetId=google_sheets_id_users,
                range=range_name,
                valueInputOption="RAW",
                insertDataOption="INSERT_ROWS",
                body={"values": [row]}
            ).execute, object)
            service.spreadsheets().values().append(
                spreadsheetId=google_sheets_id_users,
                range=range_name,
                valueInputOption="RAW",
                insertDataOption="INSERT_ROWS",
                body={"values": [row]}
            ).execute()
            logger.info(f"Data successfully saved: {row}")
            break
        except HttpError as e:
            logger.error(f"Attempt {attempt + 1} failed: {e}")
            if attempt < 2:  # Retry for first two attempts
                time.sleep(2 ** attempt)  # Exponential backoff
            else:
                logger.critical(f"Failed to save data after 3 attempts: {e}")
                raise
        except Exception as e:
            logger.critical(f"Unexpected error: {e}")
            raise