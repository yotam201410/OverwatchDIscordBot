import sqlite3
import discord
from discord.ext import commands
from Globals import Globals

class HelpCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(name="help", ivoke_without_command=False)
    async def help(self, ctx, *args):
        await ctx.message.delete()
        channel1 = ctx.author.voice.channel
        invite = await channel1.create_invite(max_age=60)
        c = Globals.conn.cursor()
        c.execute("""SELECT * FROM server_preference
                       WHERE guild_id = :guild_id""",
                  {"guild_id": ctx.guild.id})
        data = c.fetchone()
        role = data[4]
        if args is not []:
            reason = " ".join(args)
        else:
            reason = "Unspecified"
        if role is not None:
            role = f'<@&{role}>'
            await ctx.send(f"{ctx.author.mention} needs help at {invite} {role} for {reason}")
            await ctx.send(f"{ctx.author.mention} if you meant to get the commands do help ")
        else:
            await ctx.send(f"{ctx.author.mention} needs help at {invite} for {reason}")



    @help.error
    async def help_error(self, ctx, error):  # error has to be in there
        if commands.MissingRequiredArgument != AttributeError:
            c = Globals.conn.cursor()
            c.execute("""SELECT * FROM server_preference
                           WHERE guild_id = :guild_id""",
                      {"guild_id": ctx.guild.id})
            data = c.fetchone()
            role = data[4]
            if role is not None:
                role = f'<@&{role}>'
                await ctx.send(f"{ctx.author.mention} needs help at an unknown place {role}")
            else:
                await ctx.send(f"{ctx.author.mention} needs help at an unknown place")


def setup(client):
    client.add_cog(HelpCommands(client))
