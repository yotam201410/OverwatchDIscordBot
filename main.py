import datetime
import os

import discord
from dateutil.parser import parse
from discord.ext import commands
import sqlite3
from app import keep_alive
import sql_table_building
from Globals import Globals

times = 0


def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try:
        parse(string, fuzzy=fuzzy)
        return True
    except ValueError:
        return False


def removeNone(value: tuple):
    ret = []
    for i in value:
        if i == "None":
            ret.append(None)
        else:
            if type(i) is int or i.isnumeric():
                ret.append(int(i))
            elif is_date(i):
                ret.append(datetime.datetime.strptime(i, "%Y-%m-%d %H:%M:%S.%f"))
            else:
                ret.append(i)
    print(ret)
    return tuple(ret)


def update_data():
    c = Globals.conn.cursor()
    d = Globals.sheets.worksheet("server_preference").get_all_values()
    for i in range(1, len(d)):
        try:
            c.execute(
                """insert into server_preference(guild_id,prefix,report_mod_channel_id,mods_role_id,helpers_role_id,join_to_create_a_room_category_id,join_to_create_a_room_channel_id,member_count_category_id,tempmute_role_id,audit_log_channel_id,commands_log_channel_id,pug_player_role,moderation)
                values (?,?,?,?,?,?,?,?,?,?,?,?,?)""", removeNone(d[i]))
        except sqlite3.IntegrityError:
            pass
    d = Globals.sheets.worksheet("voice_user_data").get_all_values()
    for i in range(1, len(d)):
        try:
            c.execute("""insert into voice_user_data(voice_owner_id,voice_name,voice_limit)
            values (?,?,?)""", removeNone(removeNone(d[i])))
        except sqlite3.IntegrityError:
            pass
    d = Globals.sheets.worksheet("voice_data").get_all_values()
    for i in range(1, len(d)):
        try:
            c.execute("""insert into voice_data(voice_owner_id,voice_channel_id,guild_id)
            values (?,?,?)""", removeNone(d[i]))
        except sqlite3.IntegrityError:
            pass
    d = Globals.sheets.worksheet("member_count").get_all_values()
    for i in range(1, len(d)):
        try:
            c.execute("""insert into member_count(guild_id,member_count_channel_id)
            values (?,?)""", removeNone(d[i]))
        except sqlite3.IntegrityError:
            pass
    d = Globals.sheets.worksheet("offences").get_all_values()
    for i in range(1, len(d)):
        try:
            c.execute("""insert into offences(member_id,member_name,guild_id,kind,start_date,end_date,reason,treated,moderator_id)
            values (?,?,?,?,?,?,?,?,?)""", removeNone(d[i]))
        except sqlite3.IntegrityError:
            pass
    # d = Globals.sheets.worksheet("pug_limit_5").get_all_values()
    # for i in range(1, len(d)):
    #     c.execute("""insert into pug_limit_5(match_id,guild_id,red_team_player_1,red_team_player_2,red_team_player_3,red_team_player_4,red_team_player_5,blue_team_player_1,blue_team_player_2,blue_team_player_3,blue_team_player_4,blue_team_player_5,result)
    #     values (?,?,?,?,?,?,?,?,?,?,?,?,?)""", removeNone(d[i]))
    # d = Globals.sheets.worksheet("pug_limit_6").get_all_values()
    # for i in range(1, len(d)):
    #     c.execute("""insert into pug_limit_6(match_id,guild_id,red_team_player_1,red_team_player_2,red_team_player_3,red_team_player_4,red_team_player_5,,red_team_player_6,blue_team_player_1,blue_team_player_2,blue_team_player_3,blue_team_player_4,blue_team_player_5,blue_team_player_6,result)
    #     values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", removeNone(d[i]))
    Globals.conn.commit()


def get_prefix(client, message):
    c = Globals.conn.cursor()
    c.execute("""SELECT * FROM server_preference
               WHERE guild_id = :guild_id
""", {"guild_id": message.guild.id})
    data = c.fetchone()
    return data[1]


client = commands.Bot(command_prefix=get_prefix, intents=discord.Intents.all(),
                      active=discord.activity.Game(name="!setup help"))
client.remove_command('help')


@client.event
async def on_guild_join(guild):
    c = Globals.conn.cursor()
    c.execute("""INSERT INTO server_preference(guild_id,prefix)
    SELECT :guild_id, :prefix
    WHERE NOT EXISTS (SELECT 1 FROM server_preference WHERE guild_id = :guild_id)""",
              {"guild_id": guild.id, "prefix": "."})
    Globals.conn.commit()


@client.event
async def on_guild_remove(guild):
    c = Globals.conn.cursor()
    c.execute("""DELETE FROM server_preference WHERE guild_id=:guild_id""",
              {"guild_id": guild.id})
    c.execute("""DELETE FROM member_count WHERE guild_id=:guild_id""",
              {"guild_id": guild.id})
    Globals.conn.commit()


@client.event
async def on_command_error(ctx: commands.Context, error):
    print(ctx.message.content)
    c = Globals.conn.cursor()
    c.execute("""select prefix from server_preference
    where guild_id = :guild_id""", {"guild_id": ctx.guild.id})
    prefix = c.fetchone()[0]
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title="all commands", colour=0x0000ff,
                              description=f"**commands prefix {prefix} **\nall of the help module commands")
        embed.set_thumbnail(url=client.user.avatar_url)
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
        embed.add_field(name=f"**{prefix}help setup**", value="all of the commands of the setup module")
        embed.add_field(name=f"**{prefix}help voice**", value="all of the commands of the voice module")
        embed.add_field(name=f"**{prefix}help ow**", value="all of the commands of the overwatch module")
        await ctx.send(embed=embed)
    else:
        raise error


@client.event
async def on_ready():
    global times
    if times == 0:
        c = Globals.conn.cursor()
        try:
            update_data()
            for guild in client.guilds:
                c.execute("""INSERT INTO server_preference(guild_id,prefix)
            SELECT :guild_id, :prefix
            WHERE NOT EXISTS (SELECT 1 FROM server_preference WHERE guild_id = :guild_id)""",
                          {"guild_id": guild.id, "prefix": "."})
        except sqlite3.OperationalError:
            sql_table_building.idk()
            update_data()
            for guild in client.guilds:
                c.execute("""INSERT INTO server_preference(guild_id,prefix)
            SELECT :guild_id, :prefix
            WHERE NOT EXISTS (SELECT 1 FROM server_preference WHERE guild_id = :guild_id)""",
                          {"guild_id": guild.id, "prefix": "!"})
        for filename in os.listdir("cogs"):
            if filename.endswith(".py") and filename != "__init__.py":
                client.load_extension(f"cogs.{filename[:-3]}")
        times += 1
    print("bot is ready v 1.0")


keep_alive()
client.run(Globals.token)
