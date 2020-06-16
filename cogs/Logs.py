import datetime
import sqlite3

import discord
from discord.ext import commands

from Globals import Globals


def get_changed_roles(before: discord.Member, after: discord.Member):
    dic = {}
    for i in before.roles:
        if i not in after.roles:
            dic[i] = "given"
    for i in after.roles:
        if i not in before.roles:
            dic[i] = "removed"

    return dic


def get_audit_log_channel_id(guild_id: int):
    c = Globals.conn.cursor()
    c.execute("""select audit_log_channel_id from server_preference
    where guild_id  = :guild_id""", {"guild_id": guild_id})
    data = c.fetchone()
    return data[0]


def get_command_log_channel_id(guild_id: int):
    c = Globals.conn.cursor()
    c.execute("""select * from server_preference
    where guild_id :guild_id""", {"guild_id": guild_id})
    data = c.fetchone()
    return data[10]


class Logs(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_raw_message_delete(self, payload):
        channel = get_audit_log_channel_id(payload.guild_id)
        if channel is not None:
            if payload.cached_message is None:
                date = datetime.datetime.utcnow()
                embed = discord.Embed(title=f"message has been deleted in {self.client.get_channel(payload.channel_id)}",
                                      timestamp=date)
                embed.add_field(name="date", value=f"{date}")
            else:
                date = datetime.datetime.utcnow()
                message = payload.cached_message
                embed = discord.Embed(title=f"message has been deleted in {message.channel}", timestamp=date)
                embed.set_author(name=message.author, icon_url=message.author.avatar_url)
                embed.add_field(name="content", value=f"{message.content}", inline=False)
                embed.add_field(name="ID", value=f"```py\n User = {message.author.id} \n Message = {message.id} \n ```",
                                inline=False)
                embed.add_field(name="date", value=f"{date}", inline=False)
            await self.client.get_channel(channel).send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel: discord.abc.GuildChannel):
        if self.client.get_channel(get_audit_log_channel_id(channel.guild.id)) is not None:
            if channel.category is None:
                date = datetime.datetime.utcnow()
                embed = discord.Embed(title=f"a category has been deleted", timestamp=date)
                embed.set_author(name=self.client.user, icon_url=self.client.user.avatar_url)
                embed.add_field(name="category", value=str(channel), inline=False)
                embed.add_field(name="date", value=f"{date}", inline=False)
            else:
                date = datetime.datetime.utcnow()
                embed = discord.Embed(title=f"a channel has been deleted", timestamp=date)
                embed.set_author(name=self.client.user, icon_url=self.client.user.avatar_url)
                embed.add_field(name="channel", value=str(channel), inline=False)
                embed.add_field(name="date", value=f"{date}", inline=False)
            await self.client.get_channel(get_audit_log_channel_id(channel.guild.id)).send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel: discord.abc.GuildChannel):
        if self.client.get_channel(get_audit_log_channel_id(channel.guild.id)) is not None:
            if channel.category is None:
                date = datetime.datetime.utcnow()
                embed = discord.Embed(title=f"a category has been created", timestamp=date)
                embed.set_author(name=self.client.user, icon_url=self.client.user.avatar_url)
                embed.add_field(name="category", value=channel.mention, inline=False)
                embed.add_field(name="date", value=f"{date}", inline=False)
            else:
                date = datetime.datetime.utcnow()
                embed = discord.Embed(title=f"a channel has been created", timestamp=date)
                embed.set_author(name=self.client.user, icon_url=self.client.user.avatar_url)
                embed.add_field(name="channel", value=channel.mention, inline=False)
                embed.add_field(name="date", value=f"{date}", inline=False)
            await self.client.get_channel(get_audit_log_channel_id(channel.guild.id)).send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_update(self, before: discord.abc.GuildChannel, after: discord.abc.GuildChannel):
        if self.client.get_channel(get_audit_log_channel_id(after.guild.id)) is not None:
            audit_log_channel = self.client.get_channel(get_audit_log_channel_id(after.guild.id))
            if after.category is None:
                date = datetime.datetime.utcnow()
                if before.name != after.name:
                    embed = discord.Embed(title=f"a category has been renamed", timestamp=date)
                    embed.set_author(name=self.client.user, icon_url=self.client.user.avatar_url)
                    embed.add_field(name="category", value=after.mention)
                    embed.add_field(name="before name", value=before.name)
                    embed.add_field(name="after name", value=after.name)
                    embed.add_field(name="date", value=f"{date}", inline=False)
                    await audit_log_channel.send(embed=embed)
                else:
                    embed = discord.Embed(title=f"a category has been changed", timestamp=date)
                    embed.set_author(name=self.client.user, icon_url=self.client.user.avatar_url)
                    embed.add_field(name="category", value=after.mention)
                    embed.add_field(name="date", value=f"{date}", inline=False)
                    await audit_log_channel.send(embed=embed)
            else:
                date = datetime.datetime.utcnow()
                if before.name != after.name:
                    embed = discord.Embed(title=f"a channel has been renamed", timestamp=date)
                    embed.set_author(name=self.client.user, icon_url=self.client.user.avatar_url)
                    embed.add_field(name="channel", value=after.mention)
                    embed.add_field(name="before name", value=before.name)
                    embed.add_field(name="after name", value=after.name)
                    embed.add_field(name="date", value=f"{date}", inline=False)
                    await audit_log_channel.send(embed=embed)
                else:
                    embed = discord.Embed(title=f"a channel has been changed", timestamp=date)
                    embed.set_author(name=self.client.user, icon_url=self.client.user.avatar_url)
                    embed.add_field(name="channel", value=after.mention)
                    embed.add_field(name="date", value=f"{date}", inline=False)
                    await audit_log_channel.send(embed=embed)

    v = {'type': 0, 'tts': False, 'timestamp': '2020-05-11T11:01:09.665000+00:00', 'pinned': False, 'mentions': [],
         'mention_roles': [], 'mention_everyone': False, 'member':
             {'roles': ['631032288423051297', '635912914619990027'],
              'premium_since': None, 'nick': 'yotam201410', 'mute': False,
              'joined_at': '2019-10-06T18:57:56.160000+00:00',
              'hoisted_role': '631032288423051297', 'deaf': False},
         'id': '709359439614050354', 'flags': 0, 'embeds': [], 'edited_timestamp': '2020-05-13T15:55:02.264326+00:00',
         'content': 'https://www.youtube.com/watch?v=SOUNLig8-', 'channel_id': '650801701015781398',
         'author': {'username': 'Yotam201410', 'public_flags': 128, 'id': '342725139626065920', 'discriminator': '6171',
                    'avatar': '47a7a7c5898851b3b8efad9b877cc50f'},
         'attachments': [], 'guild_id': '630411122134089747'}

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        if self.client.get_channel(get_audit_log_channel_id(member.guild.id)) is not None:
            embed = discord.Embed(name=f"{member} has just joined the server", timestamp=datetime.datetime.utcnow())
            embed.set_author(name=f"{member}", icon_url=member.avatar_url)
            embed.add_field(name="mention", value=f"{member.mention}")
            embed.add_field(name="ID", value=f" ```python \n Member = {member.id} \n```")
            await self.client.get_channel(get_audit_log_channel_id(member.guild.id)).send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        if self.client.get_channel(get_audit_log_channel_id(member.guild.id)) is not None:
            embed = discord.Embed(name=f"{member} has just left the server", timestamp=datetime.datetime.utcnow())
            embed.set_author(name=f"{member}", icon_url=member.avatar_url)
            embed.add_field(name="mention", value=f"{member.mention}")
            embed.add_field(name="ID", value=f"```python \n Member = {member.id} \n```")
            await self.client.get_channel(get_audit_log_channel_id(member.guild.id)).send(embed=embed)

    @commands.Cog.listener()
    async def on_member_update(self, before: discord.Member, after: discord.Member):
        if self.client.get_channel(get_audit_log_channel_id(after.guild.id)) is not None:

            audit_log_channel = self.client.get_channel(get_audit_log_channel_id(after.guild.id))
            if before.nick != after.nick:
                embed = discord.Embed(title=f"{after} had his nickname changed", timestamp=datetime.datetime.utcnow())
                embed.set_author(name=f"{after}", icon_url=after.avatar_url)
                embed.add_field(name="Member", value=after.mention, inline=False)
                embed.add_field(name="Date", value=f"{datetime.datetime.utcnow()}", inline=False)
                embed.add_field(name="before name", value=before.display_name)
                embed.add_field(name="After name", value=after.display_name)
                await audit_log_channel.send(embed=embed)
            if before.roles != after.roles:
                removed_roles = ""
                added_roles = ""
                roles: dict = get_changed_roles(after, before)
                for i in roles:
                    if roles[i] == "removed":
                        removed_roles += f"{i.name}({i.id}) \n"
                    elif roles[i] == "given":
                        added_roles += f"{i.name}({i.id}) \n"
                embed = discord.Embed(title=f"{after} had his roles changed", timestamp=datetime.datetime.utcnow())
                embed.set_author(name=f"{after}", icon_url=after.avatar_url)
                embed.add_field(name="Member", value=after.mention, inline=False)
                embed.add_field(name="Date", value=f"{datetime.datetime.utcnow()}", inline=False)
                if added_roles != "":
                    embed.add_field(name="given roles", value=f"{added_roles}", inline=False)
                if removed_roles != "":
                    embed.add_field(name="removed roles", value=f"{removed_roles}", inline=False)
                await audit_log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_role_create(self, role: discord.Role):
        if self.client.get_channel(get_audit_log_channel_id(role.guild.id)) is not None:
            embed = discord.Embed(title=f"{role.name} has been created", timestamp=datetime.datetime.utcnow())
            embed.set_author(name=f"{self.client.user}", icon_url=self.client.user.avatar_url)
            embed.add_field(name=f"role", value=role.name, inline=False)
            embed.add_field(name="ID", value=f"````py\n Role = {role.id}")
            await self.client.get_channel(get_audit_log_channel_id(role.guild.id)).send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role: discord.Role):
        if self.client.get_channel(get_audit_log_channel_id(role.guild.id)) is not None:
            embed = discord.Embed(title=f"{role.name} has been deleted", timestamp=datetime.datetime.utcnow())
            embed.set_author(name=f"{self.client.user}", icon_url=self.client.user.avatar_url)
            embed.add_field(name=f"role", value=role.name, inline=False)
            embed.add_field(name="ID", value=f"````py\n Role = {role.id}")
            await self.client.get_channel(get_audit_log_channel_id(role.guild.id)).send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_role_update(self, before: discord.Role, after: discord.Role):
        """

        :param after: represent the after role
        :param before: represent the before role
        :type before: discord.Role
        """
        if self.client.get_channel(get_audit_log_channel_id(after.guild.id)) is not None:

            embed = discord.Embed(title=f"{after.name} has been updated", timestamp=datetime.datetime.utcnow())
            embed.set_author(name=f"{self.client.user}", icon_url=self.client.user.avatar_url)
            embed.add_field(name=f"role", value=after.name, inline=False)
            embed.add_field(name="ID", value=f"````py\n Role = {after.id}")
            await self.client.get_channel(get_audit_log_channel_id(after.guild.id)).send(embed=embed)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState,
                                    after: discord.VoiceState):
        if self.client.get_channel(get_audit_log_channel_id(member.guild.id)) is not None:
            date = datetime.datetime.utcnow()
            audit_log_channel = self.client.get_channel(get_audit_log_channel_id(member.guild.id))
            if after.channel != before.channel:
                if before.channel is None:  # joined voice
                    embed = discord.Embed(timestamp=date, title=f"{member} has joined {after.channel} ")
                    embed.set_author(name=f"{member}", icon_url=member.avatar_url)
                    embed.add_field(name="channel", value=f"{after.channel}", inline=False)
                    embed.add_field(name="ID", value=f"```py\n Channel = {after.channel.id}\n Member = {member.id}\n```",
                                    inline=False)
                    await audit_log_channel.send(embed=embed)
                elif after.channel is None:
                    embed = discord.Embed(timestamp=date, title=f"{member} has left {before.channel} ")
                    embed.set_author(name=f"{member}", icon_url=member.avatar_url)
                    embed.add_field(name="channel", value=f"{before.channel}", inline=False)
                    embed.add_field(name="ID", value=f"```py\n Channel = {before.channel.id}\n Member = {member.id}\n```",
                                    inline=False)
                    await audit_log_channel.send(embed=embed)
                else:
                    embed = discord.Embed(timestamp=date,
                                          title=f"{member} has moved from {before.channel} to {after.channel}")
                    embed.set_author(name=f"{member}", icon_url=member.avatar_url)
                    embed.add_field(name="before channel", value=f"{before.channel}", inline=False)
                    embed.add_field(name="after channel", value=f"{after.channel}", inline=False)
                    embed.add_field(name="ID",
                                    value=f"```py\n before channel = {before.channel.id}\n After channel = {after.channel.id}\n Member = {member.id}\n```",
                                    inline=False)
                    await audit_log_channel.send(embed=embed)
            if before.deaf != after.deaf:
                if after.deaf is True:
                    embed = discord.Embed(timestamp=date,
                                          title=f"{member} has been server deafened at {after.channel}")
                    embed.set_author(name=f"{member}", icon_url=member.avatar_url)
                    embed.add_field(name="channel", value=f"{after.channel}", inline=False)
                    embed.add_field(name="ID",
                                    value=f"```py\n Channel = {after.channel.id}\n Member = {member.id}\n```", inline=False)
                    await audit_log_channel.send(embed=embed)
                else:
                    embed = discord.Embed(timestamp=date,
                                          title=f"{member} has been server undeafened at {after.channel}")
                    embed.set_author(name=f"{member}", icon_url=member.avatar_url)
                    embed.add_field(name="channel", value=f"{after.channel}", inline=False)
                    embed.add_field(name="ID",
                                    value=f"```py\n Channel = {after.channel.id}\n Member = {member.id}\n```", inline=False)
                    await audit_log_channel.send(embed=embed)
            if before.mute != after.mute:
                if after.mute is True:
                    embed = discord.Embed(timestamp=date,
                                          title=f"{member} has been server muted at {after.channel}")
                    embed.set_author(name=f"{member}", icon_url=member.avatar_url)
                    embed.add_field(name="channel", value=f"{after.channel}", inline=False)
                    embed.add_field(name="ID",
                                    value=f"```py\n Channel = {after.channel.id}\n Member = {member.id}\n```", inline=False)
                    await audit_log_channel.send(embed=embed)
                else:
                    embed = discord.Embed(timestamp=date,
                                          title=f"{member} has been server unmuted at {after.channel}")
                    embed.set_author(name=f"{member}", icon_url=member.avatar_url)
                    embed.add_field(name="channel", value=f"{after.channel}", inline=False)
                    embed.add_field(name="ID",
                                    value=f"```py\n Channel = {after.channel.id}\n Member = {member.id}\n```", inline=False)
                    await audit_log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_ban(self, guild: discord.Guild, user: discord.User):
        if self.client.get_channel(get_audit_log_channel_id(guild.id)) is not None:
            date = datetime.datetime.utcnow()
            audit_log_channel = self.client.get_channel(get_audit_log_channel_id(guild.id))
            embed = discord.Embed(title=f"{user} has been banned", timestamp=date)
            embed.set_author(name=f"{user}", icon_url=user.avatar_url)
            embed.add_field(name="ID", value=f"```py\n User = {user.id}\n```")
            await audit_log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_unban(self, guild: discord.Guild, user: discord.User):
        if self.client.get_channel(get_audit_log_channel_id(guild.id)) is not None:
            date = datetime.datetime.utcnow()
            audit_log_channel = self.client.get_channel(get_audit_log_channel_id(guild.id))
            embed = discord.Embed(title=f"{user} has been unbanned", timestamp=date)
            embed.set_author(name=f"{user}", icon_url=user.avatar_url)
            embed.add_field(name="ID", value=f"```py\n User = {user.id}\n```")
            await audit_log_channel.send(embed=embed)


def setup(client):
    client.add_cog(Logs(client))
