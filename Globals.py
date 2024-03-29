import sqlite3

import gspread
from oauth2client.service_account import ServiceAccountCredentials


class Globals:
    redirect_URL = "https://overwatch-israel-discord-bot.herokuapp.com/login"
    clientID = "988d19acb11947499c2509b0453aaf17"
    clientSecret = "ZCbJ6GAi139CNa7hb7787ypPrAvaKL9V"
    redirect_URL2 = "http://127.0.0.1/login/"
    conn = sqlite3.connect("discord_bot.db", check_same_thread=False)
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(creds)
    sheets = client.open("discord bot db")
    with open("token.txt", 'r') as f:
        token = f.read()
