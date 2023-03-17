import pathlib

import gspread
import gspread.exceptions
import oauth2client.service_account

creds_fname = "topcool-380919-92fe26e56958.json"
workbook_name = "mysheet-topcool"

creds_path = pathlib.Path(creds_fname)


def main():
    credentials_path = creds_path

    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ]

    creds = (
        oauth2client.service_account.ServiceAccountCredentials.from_json_keyfile_name(
            credentials_path, scopes
        )
    )
    client = gspread.authorize(creds)
    workbook = client.open(workbook_name)

    sheets = workbook.worksheets()

    for sheet in sheets:
        sheet.clear()

    sheets[0].update("A1", "Bingo!")


main()
