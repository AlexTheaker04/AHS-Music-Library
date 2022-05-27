import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
client = gspread.authorize(creds)

sheet = client.open('test123').sheet1
list_of_hashes = sheet.get_all_records()
for i in range(2, 265, 1):
    print(list_of_hashes[i])

print(list_of_hashes[1])
