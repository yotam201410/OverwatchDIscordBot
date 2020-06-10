import json
import requests
from flask import Flask, request, Response
from requests.auth import HTTPBasicAuth

from Globals import Globals

app = Flask("idk")


def getBattleNetToken(code, region):
    url = "https://%s.battle.net/oauth/token" % region
    body = {"grant_type": 'authorization_code', "code": f"{code}", "redirect_uri": f"{Globals.redirect_URL}"}
    auth = HTTPBasicAuth(Globals.clientID, Globals.clientSecret)
    response = requests.post(url, data=body, auth=auth)
    response = response.json()
    return response["access_token"]


def getBattleTag(BattleNetToken, region):
    url = f"https://{region}.battle.net/oauth/userinfo?access_token={BattleNetToken}"
    response = requests.get(url)
    return response.json()["battletag"] if response.status_code == 200 else None


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
    battleNetToken = getBattleNetToken(battleNetCode, "eu")
    with open("users.json") as r:
        data = json.load(r)
        r.close()
    with open("users.json", 'w') as w:
        data[f"{discordUserID}"] = [getBattleTag(battleNetToken, "eu"), request.remote_addr]
        json.dump(data, w)
    return Response("", status=200)


def appRun():
    app.run()


def main():
    appRun()


if __name__ == '__main__':
    main()
