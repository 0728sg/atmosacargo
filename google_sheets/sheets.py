from google_sheets.config_sheets import service, google_sheets_id_users
from aiogram import Dispatcher, types


def update_google_sheets(code, fullname, phone):
    try:
        range_name = "Клиенты!A:C"

        row = [code, fullname, phone]
        service.spreadsheets().values().append(
            spreadsheetId=google_sheets_id_users,
            range=range_name,
            valueInputOption="RAW",
            insertDataOption="INSERT_ROWS",
            body={"values": [row]}
        ).execute()
        print(row)

    except Exception as e:
        print(e)