import requests
from flask import Flask, request, Response
from requests.auth import HTTPBasicAuth

from Globals import Globals

app = Flask("idk")


def getRow(sheet, discord_id):
    counter = 0
    data = sheet.get_all_values()
    for i in data:
        counter += 1
        if i[0] == str(discord_id):
            return counter
    return None


def updateSheet(sheet, discord_id, battleTag, ip_address):
    row = getRow(sheet, discord_id)
    sheet.update_cell(row, 1, str(discord_id))
    sheet.update_cell(row, 2, str(battleTag))
    sheet.update_cell(row, 3, str(ip_address))


def getBattleNetToken(code, region):
    url = "https://%s.battle.net/oauth/token" % region
    body = {"grant_type": 'authorization_code', "code": f"{code}", "redirect_uri": f"{Globals.redirect_URL}"}
    auth = HTTPBasicAuth(Globals.clientID, Globals.clientSecret)
    response = requests.post(url, data=body, auth=auth)
    response = response.json()
    print(response)
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
    battleTag = getBattleTag(battleNetToken, "eu")
    sheet = Globals.sheets.worksheet("ow_users")
    if getRow(sheet, discordUserID) is None:
        sheet.insert_row([f"{discordUserID}", f"{battleTag}", f"{request.remote_addr}"])
    else:
        updateSheet(sheet, discordUserID, battleTag, request.remote_addr)
    return Response(f"{battleTag}", status=200)


def appRun():
    app.run()


def main():
    appRun()


if __name__ == '__main__':
    main()
