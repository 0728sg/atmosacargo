from google_sheets.config_sheets import service, google_sheets_id_users
from aiogram import Dispatcher, types
from config import dp




# def update_google_sheets(code, fullname, phone):



async def update_google_sheets(code: str, fullname: str, phone: str):
    print(f"Сохраняем: {code}, {fullname}, {phone}")
    try:
        range_name = "Клиенты!A:C"
        print(1)
        row = [code, fullname, phone]
        print(2)
        service.spreadsheets().values().append(
            spreadsheetId=google_sheets_id_users,
            range=range_name,
            valueInputOption="RAW",
            insertDataOption="INSERT_ROWS",
            body={"values": [row]}
        ).execute()
        print(3)
        print(row)
        print(4)

    except Exception as e:
        print(e)



# def get_google_sheets_data():
#     try:
#         range_name = "Клиенты!A:C"
#         result = service.spreadsheets().values().get(
#             spreadsheetId=google_sheets_id_users,
#             range=range_name,
#         ).execute()
#         rows = result.get('values', [])
#         return rows
#     except Exception as e:
#         print(e)
#         return []
