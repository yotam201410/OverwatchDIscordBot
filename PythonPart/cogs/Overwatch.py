import discord
from discord.ext import commands
from OverwatchUserDirectory import User
from Globals import Globals


def getBattleTagWithMember(member: discord.Member):
    data = Globals().jsonfile
    for dic in data:
        print(dic["discordUserID"])
        if int(dic["discordUserID"]) == member.id:
            return dic["battleTag"]
    return None


class Overwatch(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    async def sr(self, ctx: commands.Context):
        battleTag = getBattleTagWithMember(ctx.author)
        print(battleTag)
        if battleTag is not None:
            print(type(battleTag),battleTag)
            user = User(battleTag)
            print(user.ratings.__dict__)
            if user.ratings is not None:
                embed = discord.Embed(title=f"{battleTag} Competitive sr")
                try:
                    embed.add_field(name="Tank", value=str(user.ratings.tank.level))
                except AttributeError:
                    pass
                try:
                    embed.add_field(name="Damage", value=str(user.ratings.damage.level))
                except AttributeError:
                    pass
                try:
                    embed.add_field(name="Support", value=str(user.ratings.support.level))
                except AttributeError:
                    pass
                avg = user.ratings.average_level
                if avg is not None:
                    embed.add_field(name="Avg sr", value=str(avg))
                await ctx.send(embed=embed)
            else:
                await ctx.send(
                    f"{ctx.author.mention} you have not been placed yet at competitive")
        else:
            await ctx.send(
                f"{ctx.author.mention} you have not had any Battle Net account connected **or** your profile is private")


def setup(client: commands.Bot):
    client.add_cog(Overwatch(client))
