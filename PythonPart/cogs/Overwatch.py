import json
import discord
from OverwatchUserDirectory import User
from discord.ext import commands
from Globals import Globals


def getBattleTagWithMember(member: discord.Member):
    data = open("webApp/users.json", 'r')
    data = json.load(data)
    print(data)
    try:
        return data[str(member.id)]
    except KeyError:
        return None


class Overwatch(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.group(name="overwatch", aliases=["ow", "OW"])
    async def overwatch(self, ctx):
        pass

    @overwatch.command()
    async def login(self, ctx):
        baseURL = "http://eu.battle.net/oauth/authorize?response_type=code"
        clientID = "&client_id=" + Globals.clientID
        redirectURI = "&redirect_uri=" + Globals.redirect_URL
        state = "&state=" + str(ctx.author.id)
        await ctx.send(baseURL + clientID + redirectURI + state)

    @overwatch.command(aliases=["rank", "ranking"])
    async def sr(self, ctx: commands.Context):
        battleTag = getBattleTagWithMember(ctx.author)
        if battleTag is not None:
            user = User(battleTag)
            if user.ratings is not None:
                try:
                    embed = discord.Embed(title=f"{battleTag} tank Competitive sr")
                    embed.set_thumbnail(url=user.ratings.tank.rankIcon)
                    embed.add_field(name="Tank", value=str(user.ratings.tank.level))
                    await ctx.send(embed=embed)
                except AttributeError:
                    print(False)
                try:
                    embed = discord.Embed(title=f"{battleTag} damage Competitive sr")
                    embed.set_thumbnail(url=user.ratings.damage.rankIcon)
                    embed.add_field(name="support", value=str(user.ratings.damage.level))
                    await ctx.send(embed=embed)
                except AttributeError:
                    pass
                try:

                    embed = discord.Embed(title=f"{battleTag} support Competitive sr")
                    embed.set_thumbnail(url=user.ratings.support.rankIcon)

                    embed.add_field(name="support", value=str(user.ratings.support.level))
                    await ctx.send(embed=embed)
                except AttributeError:
                    pass
                avg = user.ratings.average_level
                if avg is not None:
                    embed = discord.Embed(title=f"{battleTag} average Competitive sr")
                    embed.add_field(name="average", value=str(user.ratings.average_level))
                    await ctx.send(embed=embed)
            else:
                await ctx.send(
                    f"{ctx.author.mention} you have not been placed yet at competitive")
        else:
            await ctx.send(
                f"{ctx.author.mention} you have not had any Battle Net account connected **or** your profile is private")


def setup(client: commands.Bot):
    client.add_cog(Overwatch(client))
