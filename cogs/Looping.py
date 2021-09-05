import gspread
from discord.ext import commands, tasks
from Globals import Globals


def update_sheets_data(table):
    c = Globals.conn.cursor()
    c.execute(f"select * from {table}")
    data = c.fetchall()
    write_data = []
    for rows in data:
        columns = []
        for column in rows:
            if column:
                column = str(column)
            else:
                column = "None"
            columns.append(column)
        write_data.append(columns)
    worksheet = Globals.sheets.worksheet(table)
    worksheet.update(write_data)


class Looping(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        self.updateSheet.start()

    @tasks.loop(minutes=2)
    async def updateSheet(self):
        c = Globals.conn.cursor()
        tables = ["server_preference", "voice_user_data", "voice_data", "member_count", "ow_users", "offences"]
        try:
            for table in tables:
                update_sheets_data(table)
        except gspread.exceptions.APIError:
            print("exceeded limit")


def setup(client: commands.Bot):
    client.add_cog(Looping(client))
