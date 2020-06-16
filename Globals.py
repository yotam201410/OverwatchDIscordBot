import sqlite3


class Globals:
    redirect_URL = "https://overwatch-israel-discord-bot.herokuapp.com/login"
    clientID = "988d19acb11947499c2509b0453aaf17"
    clientSecret = "ZCbJ6GAi139CNa7hb7787ypPrAvaKL9V"
    redirect_URL2 = "http://localhost:5000/login"
    conn = sqlite3.connect("discord_bot.db")
