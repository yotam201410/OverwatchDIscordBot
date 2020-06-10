import json
import discord
from OverwatchUserDirectory import User
from OverwatchUserDirectory.ratings.Ratings import Ratings
from OverwatchUserDirectory.stats.stats import Stats
from discord.ext import commands
from Globals import Globals


def getBattleTagWithMember(member: discord.Member):
    data = open("users.json", 'r')
    data = json.load(data)
    try:
        return data[str(member.id)][0]
    except KeyError:
        return None


def make_spcace(string: str):
    return_str = ""
    for i in string:
        if i.isupper():
            return_str += " " + i.lower()
        else:
            return_str += i
    return return_str


def get_role(name: str, roles):
    for i in roles:
        if i.name == name:
            return i


async def giveRole(member: discord.Member, sr: int, ):
    roles_names = {"Bronze": discord.Colour(0xa45141), "Silver": discord.Colour(0x797979),
                   "Gold": discord.Colour(0xe6d04e), "Platinum": discord.Colour(0xB5C2C4),
                   "Diamond": discord.Colour(0x7883b9),
                   "Master": discord.Colour(0xe6b54e), "GrandMaster": discord.Colour(0xe4ca94),
                   "Top 500": discord.Colour(0x5dbcd2)}
    server_roles = member.guild.roles
    roles = []
    for role in server_roles:
        roles.append(role.name)
    for role_name in roles_names.keys():
        if role_name not in roles:
            await member.guild.create_role(name=role_name, permissions=server_roles[0].permissions,
                                           colour=roles_names[role_name])
    server_roles = member.guild.roles
    if sr < 1500:
        role = get_role("Bronze", server_roles)
    elif sr < 2000:
        role = get_role("Silver", server_roles)
    elif sr < 2500:
        role = get_role("Gold", server_roles)
    elif sr < 3000:
        role = get_role("Platinum", server_roles)
    elif sr < 3500:
        role = get_role("Diamond", server_roles)
    elif sr < 4000:
        role = get_role("Master", server_roles)
    else:
        role = get_role("GrandMaster", server_roles)
    await member.add_roles(role)


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
        try:
            await ctx.author.send(baseURL + clientID + redirectURI + state)
        except discord.HTTPException:
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
                    pass
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

    @overwatch.command()
    async def give_role(self, ctx):
        battle_tag = getBattleTagWithMember(ctx.author)
        user = User(battle_tag)
        ratings = [user.ratings.tank, user.ratings.damage, user.ratings.support]
        if not user.private:
            role = None
            for i in ratings:
                if i != user.ratings.average_level and i is not None:
                    if role is None:
                        role = i
                    elif role.level < i.level:
                        role = i
            if role is None:
                await ctx.send("you have not finished you placements")
            else:
                await giveRole(ctx.author, role.level)
        else:
            await ctx.send("you have not logged in to the bot please you the login command")

    @overwatch.command()
    async def herostats(self, ctx: commands.Context, stats_kind, hero, hero_kind_of_stats):
        battletag = getBattleTagWithMember(ctx.author)
        if battletag is not None:
            user = User(battletag)
            if user.private is False:
                if stats_kind in ["competitive", "Comp", "comp", "Competitive"]:
                    try:
                        hero = user.competitiveStats.career_stats.hero_dict[hero]
                        try:
                            embed_stats = hero.__dict__[f"_{hero_kind_of_stats}"]
                            hero_thumbnail = f"https://d1u1mce87gyfbn.cloudfront.net/hero/{hero.hero}/icon-portrait.png"
                            embed = discord.Embed(
                                title=f"here are you {hero_kind_of_stats} stats at competitive with {hero.hero}")
                            embed.set_thumbnail(url=hero_thumbnail)
                            for stat in embed_stats.__dict__:
                                if embed_stats.__dict__[stat] is not None and embed_stats.__dict__[stat] is not 0:
                                    embed.add_field(name=f"{make_spcace(stat[1::])}",
                                                    value=str(embed_stats.__dict__[stat]))
                            await ctx.send(embed=embed)
                        except KeyError:
                            await ctx.send(f"there is not such a stat as {hero_kind_of_stats}")
                    except ValueError:
                        await ctx.send("you dont have a competitive stats")
                    except KeyError:
                        await ctx.send(
                            f"or that you dont have a competitive stats at {hero} or that hero does not exist")
                elif stats_kind in ["quick_play", "QuickPlay", "quickPlay", "Quick_Play", "quick", "Quick"]:
                    try:
                        hero = user.quickPlayStats.career_stats.hero_dict[hero]
                        try:
                            embed_stats = hero.__dict__[f"_{hero_kind_of_stats}"]
                            hero_thumbnail = f"https://d1u1mce87gyfbn.cloudfront.net/hero/{hero.hero}/icon-portrait.png"
                            embed = discord.Embed(
                                title=f"here are you {hero_kind_of_stats} stats at competitive with {hero.hero}")
                            embed.set_thumbnail(url=hero_thumbnail)
                            for stat in embed_stats.__dict__:
                                if embed_stats.__dict__[stat] is not None and embed_stats.__dict__[stat] is not 0:
                                    embed.add_field(name=f"{make_spcace(stat[1::])}",
                                                    value=str(embed_stats.__dict__[stat]))
                            await ctx.send(embed=embed)
                        except KeyError:
                            await ctx.send(f"there is not such a stat as {hero_kind_of_stats}")
                    except ValueError:
                        await ctx.send("you dont have a competitive stats")
                    except KeyError:
                        await ctx.send(
                            f"or that you dont have a quick play stats at {hero} or that hero does not exist")
                else:
                    await ctx.send("they are not any kind of stats only quick_play or competitive (comp)")
            else:
                await ctx.send("your profile is private")

        else:
            await ctx.send(f"you are not logged in please use the overwatch login command")

    @overwatch.command()
    async def all_heroes(self, ctx, stats_kind, kind):
        battletag = getBattleTagWithMember(ctx.author)
        if battletag is not None:
            user = User(battletag)
            if user.private is False:
                if stats_kind in ["competitive", "Comp", "comp", "Competitive"]:
                    if user.competitiveStats is not None:
                        try:
                            embed_stats = user.competitiveStats.career_stats.all_Heroes.__dict__[kind]
                            embed = discord.Embed(title=f"{ctx.author} all heroes Competitive {kind} stats")
                            embed.set_thumbnail(
                                url="https://pbs.twimg.com/profile_images/939130553835704320/xeqC89JR_400x400.jpg")
                            for stat in embed_stats.__dict__:
                                if embed_stats.__dict__[stat] is not None and embed_stats.__dict__[stat] is not 0:
                                    embed.add_field(name=f"{make_spcace(stat[1::])}",
                                                    value=str(embed_stats.__dict__[stat]))
                            await ctx.send(embed=embed)
                        except KeyError:
                            await ctx.send(f"there is not such kind as {kind}")
                        except ValueError:
                            await ctx.send(f"please contact the me at yotam201410@gmail.com and report the bug")
                elif stats_kind in ["quick_play", "QuickPlay", "quickPlay", "Quick_Play", "quick", "Quick"]:
                    if user.quickPlayStats is not None:
                        try:
                            embed_stats = user.quickPlayStats.career_stats.all_Heroes.__dict__[kind]
                            embed = discord.Embed(title=f"{ctx.author} all heroes quick play {kind} stats")
                            embed.set_thumbnail(
                                url="https://cdn.discordapp.com/attachments/351437490587959297/720210674038472714/unknown.png")
                            for stat in embed_stats.__dict__:
                                if embed_stats.__dict__[stat] is not None and embed_stats.__dict__[stat] is not 0:
                                    embed.add_field(name=f"{make_spcace(stat[1::])}",
                                                    value=str(embed_stats.__dict__[stat]))
                            await ctx.send(embed=embed)

                        except KeyError:
                            await ctx.send(f"there is not such kind as {kind}")
                        except ValueError:
                            await ctx.send(f"please contact the me at yotam201410@gmail.com and report the bug")
                else:
                    await ctx.send("they are not any kind of stats only quick_play or competitive (comp)")
            else:
                await ctx.send("your profile is private")
        else:
            await ctx.send(f"you are not logged in please use the overwatch login command")

    @overwatch.command()
    async def profile(self, ctx):
        battletag = getBattleTagWithMember(ctx.author)
        embed = discord.Embed(title=f"{battletag} profile")
        user = User(battletag)
        embed.set_thumbnail(url=user.icon)
        for obj in user.__dict__:
            if not isinstance(user.__dict__[obj], Stats) and not isinstance(user.__dict__[obj], Ratings) and \
                    user.__dict__[obj] is not "" and user.__dict__[obj] is not None:
                embed.add_field(name=f"{make_spcace(obj)}", value=f"{str(user.__dict__[obj])}")
        await ctx.send(embed=embed)

    @herostats.error
    async def herostats_error(self, ctx, error):
        await ctx.send(
            "you have to fallow this template\n {prefix}ow herostats {[competitive or quick_play]} {hero} {[assists, average, best, game, matchAwards, miscellaneous]}")

    @all_heroes.error
    async def all_heroes_error(self, ctx, error):
        await ctx.send(
            "you have to fallow this template\n {prefix}ow all_heroes {[competitive or quick_play]} {[assists, average, best, game, matchAwards, miscellaneous]}")


def setup(client: commands.Bot):
    client.add_cog(Overwatch(client))
