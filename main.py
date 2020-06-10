import os
import sqlite3

from discord.ext import commands

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
async def on_ready():
    print("bot is ready v 0.1")
    conn = sqlite3.connect(
        "discord_bot.db")
    c = conn.cursor()
    for guild in client.guilds:
        c.execute("""INSERT INTO server_preference(guild_id,prefix)
SELECT :guild_id, :prefix
WHERE NOT EXISTS (SELECT 1 FROM server_preference WHERE guild_id = :guild_id)""",
                  {"guild_id": guild.id, "prefix": "!"})
    conn.commit()
    conn.close()
    global times
    if times == 0:
        for filename in os.listdir("cogs"):
            if filename.endswith(".py") and filename != "__init__.py":
                client.load_extension(f"cogs.{filename[:-3]}")
        times += 1

token = "NjMwNDA4Njc3Mjk1MTI4NTk2.Xt-K3Q.2C0yWPF0ZnyE9fdxu4zHVMXZIi8"

client.run(token)
