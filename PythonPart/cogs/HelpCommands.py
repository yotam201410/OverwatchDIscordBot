import discord
from discord.ext import commands
import sqlite3


class HelpCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(name="help", invoke_without_command=True)
    async def help(self, ctx, *args):
        await ctx.message.delete()
        channel1 = ctx.author.voice.channel
        invite = await channel1.create_invite(max_age=60)
        conn = sqlite3.connect(
            "discord_bot.db")
        c = conn.cursor()
        c.execute("""SELECT * FROM server_preference
                       WHERE guild_id = :guild_id""",
                  {"guild_id": ctx.guild.id})
        conn.commit()
        data = c.fetchone()
        role = data[4]
        if role is not None:
            role = f'<@&{role}>'
            await ctx.send(f"{ctx.author.mention} needs help at {invite} {role}")
        else:
            await ctx.send(f"{ctx.author.mention} needs help at {invite}")

    @help.command()
    async def voice(self, ctx):
        conn = sqlite3.connect("discord_bot.db")
        c = conn.cursor()
        c.execute("""select join_to_create_a_room_category_id,join_to_create_a_room_channel_id from sever_preference
        where guild_id :guild_id""", {"guild_id": ctx.guild.id})
        data = c.fetchone()

    @help.command()
    async def setup(self, ctx):
        pass

    @help.error
    async def help_error(self, ctx, error):  # error has to be in there
        if commands.MissingRequiredArgument != AttributeError:
            conn = sqlite3.connect(
                "discord_bot.db")
            c = conn.cursor()
            c.execute("""SELECT * FROM server_preference
                           WHERE guild_id = :guild_id""",
                      {"guild_id": ctx.guild.id})
            conn.commit()
            data = c.fetchone()
            role = data[4]
            if role is not None:
                role = f'<@&{role}>'
                await ctx.send(f"{ctx.author.mention} needs help at an unknown place {role}")
            else:
                await ctx.send(f"{ctx.author.mention} needs help at an unknown place")


def setup(client):
    client.add_cog(HelpCommands(client))
