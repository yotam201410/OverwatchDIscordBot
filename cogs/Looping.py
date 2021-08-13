from discord.ext import commands, tasks
from Globals import Globals


def add_headers(sheets):
    server_p = ["guild_id", "prefix", "prefix", "mods_role_id", "helpers_role_id", "join_to_create_a_room_category_id",
                "join_to_create_a_room_channel_id", "member_count_category_id", "tempmute_role_id",
                "audit_log_channel_id", "commands_log_channel_id", "pug_match_user_limit"]
    sheet = sheets.worksheet("server_preference")
    sheets.worksheet("server_preference").clear()
    sheet.append_row(server_p)
    voice_user_data = ["voice_owner_id", "voice_name", "voice_limit"]
    sheets.worksheet("voice_user_data").clear()
    sheets.worksheet("voice_user_data").append_row(voice_user_data)
    voice_data = ["voice_owner_id", "voice_channel_id", "guild_id"]
    sheets.worksheet("voice_data").clear()
    sheets.worksheet("voice_data").append_row(voice_data)
    member_count = ["guild_id", "member_count_channel_id"]
    sheets.worksheet("member_count").clear()
    sheets.worksheet("member_count").append_row(member_count)
    offences = ["member_id", "member_name", "guild_id", "kind", "start_date", "end_date", "reason", "treated",
                "moderator_id"]
    sheets.worksheet("offences").clear()
    sheets.worksheet("offences").append_row(offences)
    # pug_limit_5 = ["match_id", "guild_id", "red_team_player_1", "red_team_player_2", "red_team_player_3",
    #                "red_team_player_4",
    #                "red_team_player_5", "blue_team_player_1", "blue_team_player_2", "blue_team_player_3",
    #                "blue_team_player_4", "blue_team_player_5", "result"]
    # sheets.worksheet("pug_limit_5").clear()
    # sheets.worksheet("pug_limit_5").append_row(pug_limit_5)
    # pug_limit_6 = ["match_id", "guild_id", "red_team_player_1", "red_team_player_2", "red_team_player_3",
    #                "red_team_player_4",
    #                "red_team_player_5", "red_team_player_6", "blue_team_player_1", "blue_team_player_2",
    #                "blue_team_player_3",
    #                "blue_team_player_4", "blue_team_player_5", "blue_team_player_6", "result"]
    # sheets.worksheet("pug_limit_6").clear()
    # sheets.worksheet("pug_limit_6").append_row(pug_limit_6)


class Looping(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        self.updateSheet.start()

    @tasks.loop(minutes=2)
    async def updateSheet(self):
        c = Globals.conn.cursor()
        c.execute("""select * from server_preference""")
        data = c.fetchall()
        sheets = Globals.sheets
        add_headers(sheets)
        server_p = sheets.worksheet("server_preference")
        for i in data:
            l = []
            for d in i:
                if d is not None:
                    l.append(str(d))
                else:
                    l.append("None")
            server_p.append_row(l)
        c.execute("""select * from voice_user_data""")
        data = c.fetchall()
        sheets = Globals.sheets
        server_p = sheets.worksheet("voice_user_data")
        for i in data:
            l = []
            for d in i:
                if d is not None:
                    l.append(str(d))
                else:
                    l.append("None")
            server_p.append_row(l)
        c.execute("""select * from voice_data""")
        data = c.fetchall()
        sheets = Globals.sheets
        server_p = sheets.worksheet("voice_data")

        for i in data:
            l = []
            for d in i:
                if d is not None:
                    l.append(str(d))
                else:
                    l.append("None")
            server_p.append_row(l)
        c.execute("""select * from member_count""")
        data = c.fetchall()
        sheets = Globals.sheets
        server_p = sheets.worksheet("member_count")

        for i in data:
            l = []
            for d in i:
                if d is not None:
                    l.append(str(d))
                else:
                    l.append("None")
            server_p.append_row(l)
        c.execute("""select * from offences""")
        data = c.fetchall()
        sheets = Globals.sheets
        server_p = sheets.worksheet("offences")

        for i in data:
            l = []
            for d in i:
                if d is not None:
                    l.append(str(d))
                else:
                    l.append("None")
            server_p.append_row(l)
        c.execute("""select * from pug_limit_5""")
        data = c.fetchall()
        sheets = Globals.sheets
        server_p = sheets.worksheet("pug_limit_5")

        for i in data:
            l = []
            for d in i:
                if d is not None:
                    l.append(str(d))
                else:
                    l.append("None")
            server_p.append_row(l)
        c.execute("""select * from pug_limit_6""")
        data = c.fetchall()
        sheets = Globals.sheets
        server_p = sheets.worksheet("pug_limit_6")
        for i in data:
            l = []
            for d in i:
                if d is not None:
                    l.append(str(d))
                else:
                    l.append("None")
            server_p.append_row(l)


def setup(client: commands.Bot):
    client.add_cog(Looping(client))
