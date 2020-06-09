import sqlite3
import requests
from requests.auth import HTTPBasicAuth
from flask import Flask, request, Response
from PythonPart.Globals import Globals

app = Flask("idk")


def getBattleNetToken(code, region):
    url = "https://%s.battle.net/oauth/token" % region
    body = {"grant_type": 'client_credentials', "code": f"{code}", "redirect_uri": f"{Globals.redirect_URL}"}
    auth = HTTPBasicAuth(Globals.clientID, Globals.clientSecret)
    response = requests.post(url, data=body, auth=auth)
    print(response)
    return response.json()


def getBattleTag(BattleNetToken, region):
    url = f"https://{region}.battle.net/oauth/userinfo?access_token={BattleNetToken}"
    print(url)
    response = requests.get(url)
    return response.json() if response.status_code == 200 else print(response.status_code)


def checkToken(battleNetToken):
    url = "http://eu.battle.net/oauth/check_token?token=" + battleNetToken
    response = requests.get(url)
    if response.status_code == 200:
        return response.status_code
    elif response.status_code == 403:
        raise ValueError(f"{battleNetToken} is not a valid token")
    else:
        raise ValueError(f"idk shit went down")


@app.route("/login/", methods=['GET'])
def login():
    battleNetCode = request.args.get('code')
    discordUserID = request.args.get('state')
    battleNetToken = getBattleNetToken(battleNetCode, "eu")["access_token"]
    print(f"the token is {battleNetToken} and the status is 200" if checkToken(
        battleNetToken) == 200 else f"the token is not good")
    print(battleNetToken, battleNetCode)
    print(getBattleTag(battleNetToken, "eu"))
    return Response("", status=200)


def appRun():
    app.run()


def main():
    appRun()


if __name__ == '__main__':
    main()
