import discord
import gspread
from discord.ext import commands
from oauth2client.service_account import ServiceAccountCredentials
import sqlite3
from Globals import Globals
from OverwatchUserDirectory import User
from OverwatchUserDirectory.ratings.Ratings import Ratings
from OverwatchUserDirectory.stats.stats import Stats


def getRow(sheet, discord_id):
    counter = 0
    data = sheet.get_all_values()
    for i in data:
        counter += 1
        if i[0] == str(discord_id):
            return counter
    return None


def get_rank_img(rank: str):
    dic = {
        "Bronze": "https://gamepedia.cursecdn.com/overwatch_gamepedia/8/89/Badge_1_Bronze.png?version=fa38e0c94d93c352f40367c620ddd5af",
        "Silver": "https://gamepedia.cursecdn.com/overwatch_gamepedia/b/bb/Badge_2_Silver.png?version=d5f167d121ece4c68da7559fac9b5897",
        "Gold": "https://gamepedia.cursecdn.com/overwatch_gamepedia/b/b8/Badge_3_Gold.png?version=a74dc72feb1a0306497263c1e0850411",
        "Platinum": "https://gamepedia.cursecdn.com/overwatch_gamepedia/f/f8/Badge_4_Platinum.png?version=ac66a0d7101dc3e4f5e31109ffb3c21e",
        "Diamond": "https://gamepedia.cursecdn.com/overwatch_gamepedia/2/2f/Badge_5_Diamond.png?version=bf806f5eb546cb9a1b71a04fa4cf3faa",
        "Master": "https://gamepedia.cursecdn.com/overwatch_gamepedia/f/f0/Badge_6_Master.png?version=b572955550eafbd5e8f2e32566f2ca17",
        "GrandMaster": "https://gamepedia.cursecdn.com/overwatch_gamepedia/8/87/Badge_7_Grandmaster.png?version=c7d21f01f2ecffcdcbdb367c425618f2",
        "Top 500": "https://gamepedia.cursecdn.com/overwatch_gamepedia/7/73/Badge_8_Top_500.png?version=61fe40ef7c98c2fe2e699f8708bc9248"}
    return dic[rank]


def getBattleTagWithMember(member: discord.Member):
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("ow_users").sheet1
    row = getRow(sheet, member.id)
    if row is not None:
        data = sheet.row_values(row)
        return data[1]
    else:
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


def get_rank(sr):
    if sr < 1500:
        return "Bronze"
    elif sr < 2000:
        return "Silver"
    elif sr < 2500:
        return "Gold"
    elif sr < 3000:
        return "Platinum"
    elif sr < 3500:
        return "Diamond"
    elif sr < 4000:
        return "Master"
    else:
        return "GrandMaster"


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
    role = get_role(get_rank(sr), server_roles)
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
                    embed.set_author(name=f"{ctx.author}", icon_url=ctx.author.avatar_url)
                    embed.set_thumbnail(url=user.ratings.tank.rankIcon)
                    embed.add_field(name="Tank", value=str(user.ratings.tank.level))
                    await ctx.send(embed=embed)
                except AttributeError:
                    pass
                try:
                    embed = discord.Embed(title=f"{battleTag} damage Competitive sr")
                    embed.set_author(name=f"{ctx.author}", icon_url=ctx.author.avatar_url)
                    embed.set_thumbnail(url=user.ratings.damage.rankIcon)
                    embed.add_field(name="Damage", value=str(user.ratings.damage.level))
                    await ctx.send(embed=embed)
                except AttributeError:
                    pass
                try:

                    embed = discord.Embed(title=f"{battleTag} support Competitive sr")
                    embed.set_thumbnail(url=user.ratings.support.rankIcon)
                    embed.set_author(name=f"{ctx.author}", icon_url=ctx.author.avatar_url)
                    embed.add_field(name="Support", value=str(user.ratings.support.level))
                    await ctx.send(embed=embed)
                except AttributeError:
                    pass
                avg = user.ratings.average_level
                if avg is not None:
                    embed = discord.Embed(title=f"{battleTag} average Competitive sr")
                    embed.set_author(name=f"{ctx.author}", icon_url=ctx.author.avatar_url)
                    embed.set_thumbnail(url=get_rank_img(get_rank(avg)))
                    embed.add_field(name="Average", value=str(user.ratings.average_level))
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
        if battletag is not None:
            embed = discord.Embed(title=f"{battletag} profile")
            user = User(battletag)
            embed.set_thumbnail(url=user.icon)
            for obj in user.__dict__:
                if not isinstance(user.__dict__[obj], Stats) and not isinstance(user.__dict__[obj], Ratings) and \
                        user.__dict__[obj] is not "" and user.__dict__[obj] is not None:
                    embed.add_field(name=f"{make_spcace(obj)}", value=f"{str(user.__dict__[obj])}")
            await ctx.send(embed=embed)
        else:
            await ctx.send("you have to login")

    @overwatch.command()
    async def help(self, ctx):
        conn = sqlite3.connect("discord_bot.db")
        c = conn.cursor()
        c.execute("""select prefix from server_preference
            where guild_id = :guild_id""", {"guild_id": ctx.guild.id})
        data = c.fetchone()
        conn.close()
        prefix = data[0]
        embed = discord.Embed(title=f"overwatch help", colour=0xFFFFFF)
        embed.set_thumbnail(
            url="https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Overwatch_circle_logo.svg/600px-Overwatch_circle_logo.svg.png")
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
        embed.add_field(name="**" + prefix + "ow login**",
                        value="sends url at private which asks you to authorise the access to get you battle tag",
                        inline=False)
        embed.add_field(name="**" + prefix + "ow sr**", value="sends your all of your sr details", inline=False)
        embed.add_field(name="**" + prefix + "ow give_role**",
                        value="gives you a rank role as your highest rank\n **does not give you a top 500**",
                        inline=False)
        embed.add_field(
            name="**" + prefix + "ow herostats {[competitive or quick_play]} {hero} {[assists, average, best, game, matchAwards, miscellaneous]**",
            value="sends all of your spastic stats in a hero at quick play or competitive", inline=False)
        embed.add_field(
            name="**" + prefix + "ow all_heroes {[competitive or quick_play]} {[assists, average, best, game, matchAwards, miscellaneous]}**",
            value="sends all of your spastic stats in all heroes at quick play or competitive", inline=False)
        embed.add_field(name="**" + prefix + "ow profile**", value="sends you profile values", inline=False)
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
