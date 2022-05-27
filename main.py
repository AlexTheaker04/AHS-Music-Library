import gspread
import tkinter
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

f = open("file.csv", "w")



scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
client = gspread.authorize(creds)

sheet = client.open('test123').sheet1
records_data = sheet.get_all_records()

df = pd.read_csv("test123 - Sheet1.csv")
print(df.to_string())


# for i in range(1, 263, 1):
# print(list_of_hashes[i])

# print(list_of_hashes[1])
