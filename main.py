import os
import sqlite3
import discord
from discord.ext import commands
import sql_table_building
times = 0


def get_prefix(client, message):
    conn = sqlite3.connect(
        "discord_bot.db")
    c = conn.cursor()
    c.execute("""SELECT * FROM server_preference
               WHERE guild_id = :guild_id
""", {"guild_id": message.guild.id})
    data = c.fetchone()
    conn.commit()
    conn.close()
    return data[1]


client = commands.Bot(command_prefix=get_prefix)
client.remove_command('help')


@client.event
async def on_guild_join(guild):
    conn = sqlite3.connect(
        "discord_bot.db")
    c = conn.cursor()
    c.execute("""INSERT INTO server_preference(guild_id,prefix)
    SELECT :guild_id, :prefix
    WHERE NOT EXISTS (SELECT 1 FROM server_preference WHERE guild_id = :guild_id)""",
              {"guild_id": guild.id, "prefix": "!"})
    conn.commit()
    conn.close()


@client.event
async def on_guild_remove(guild):
    conn = sqlite3.connect(
        "discord_bot.db")
    c = conn.cursor()
    c.execute("""DELETE FROM server_preference WHERE guild_id=:guild_id""",
              {"guild_id": guild.id})
    c.execute("""DELETE FROM member_count WHERE guild_id=:guild_id""",
              {"guild_id": guild.id})
    conn.commit()
    conn.close()


@client.event
async def on_command_error(ctx, error):
    conn = sqlite3.connect("discord_bot.db")
    c = conn.cursor()
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


@client.event
async def on_ready():
    print("bot is ready v 1.0")
    conn = sqlite3.connect(
        "discord_bot.db")
    c = conn.cursor()
    try:
        for guild in client.guilds:
            c.execute("""INSERT INTO server_preference(guild_id,prefix)
    SELECT :guild_id, :prefix
    WHERE NOT EXISTS (SELECT 1 FROM server_preference WHERE guild_id = :guild_id)""",
                      {"guild_id": guild.id, "prefix": "!"})
    except:
        conn.commit()
        conn.close()
        sql_table_building.idk()
        conn = sqlite3.connect(
            "discord_bot.db")
        c = conn.cursor()
        for guild in client.guilds:
            c.execute("""INSERT INTO server_preference(guild_id,prefix)
        SELECT :guild_id, :prefix
        WHERE NOT EXISTS (SELECT 1 FROM server_preference WHERE guild_id = :guild_id)""",
                      {"guild_id": guild.id, "prefix": "!"})
    global times
    if times == 0:
        for filename in os.listdir("cogs"):
            if filename.endswith(".py") and filename != "__init__.py":
                client.load_extension(f"cogs.{filename[:-3]}")
        times += 1

client.run(os.environ["discord_token"])
