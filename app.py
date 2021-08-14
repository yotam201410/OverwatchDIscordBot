import requests
from flask import Flask, request, Response
from requests.auth import HTTPBasicAuth
from threading import Thread
from Globals import Globals

app = Flask("idk")


def getBattleNetToken(code, region):
    url = "https://%s.battle.net/oauth/token" % region
    body = {"grant_type": 'authorization_code', "code": f"{code}", "redirect_uri": f"{Globals.redirect_URL2}"}
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
    c = Globals.conn.cursor()
    c.execute("""select * from ow_users
                  where battle_tag = :battle_tag
                  """, {"battle_tag": battleTag})
    ow_user_data = c.fetchone()
    if ow_user_data:
        c.execute("""update ow_users
                          set member_id = :member_id , battle_tag = battle_tag, ip_address = :ip
                          where battle_tag = :battle_tag
        """, {"member_id": discordUserID, "battle_tag": battleTag, "ip": str(request.remote_addr)})
    else:
        c.execute("""insert into ow_users
        select :member_id, :battle_tag, :ip """,
                  {"member_id": discordUserID, "battle_tag": battleTag, "ip": str(request.remote_addr)})
    return Response(f"{battleTag}", status=200)


@app.route('/')
def main():
    return Response("your bot is online", status=200)


def run():
    app.run(port=80)


def keep_alive():
    server = Thread(target=run)
    server.start()
