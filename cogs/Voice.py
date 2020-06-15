import discord
from discord.ext import commands
import sqlite3


def return_category(guild, category_to_check):
    category_dict = {}
    for i in guild.categories:
        category_dict[i.id] = i
    return category_dict[category_to_check]


class Voice(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.member, before: discord.VoiceState,
                                    after: discord.VoiceState):
        """
        when a member joins a channel if its joint to create a room channel then it will move it to his channel base
        on last channel or not when a member leave a channel its checks if the channel is empty and if the origin of
        the channel was based of the command^ it will delete the channel
        :param member:
        :param before:
        :param after:
        """
        conn = sqlite3.connect("discord_bot.db")
        c = conn.cursor()
        c.execute("""select * from server_preference
        where guild_id = :guild_id""", {"guild_id": member.guild.id})
        server_preference_data = c.fetchone()
        if after.channel != before.channel and before.channel is not None and after.channel is not None:  # he moved a channel
            if after.channel.id == server_preference_data[6]:
                c.execute("""select * from voice_data
                                            where voice_channel_id= :voice_channel_id""",
                          {"voice_channel_id": before.channel.id})
                data = c.fetchone()
                conn.commit()
                if data is not None and len(before.channel.members) == 0:
                    c.execute("""DELETE FROM voice_data WHERE voice_channel_id = :voice_channel_id""",
                              {"voice_channel_id": before.channel.id})
                    conn.commit()
                    await before.channel.delete()
                c.execute("""SELECT * FROM voice_user_data
                                                   WHERE voice_owner_id = :owner_id""",
                          {"owner_id": member.id})
                voice_user_data = c.fetchone()
                conn.commit()
                if voice_user_data is not None:  # if he had a channel before
                    voice_channel = await after.channel.guild.create_voice_channel(name=voice_user_data[1],
                                                                                   category=self.client.get_channel(
                                                                                       server_preference_data[5]),
                                                                                   user_limit=voice_user_data[2])
                    c.execute("""INSERT INTO voice_data (voice_owner_id, voice_channel_id,guild_id)
                                                                                    VALUES(?,?,?)""",
                              (member.id, voice_channel.id, member.guild.id))
                    conn.commit()
                else:
                    voice_channel = await after.channel.guild.create_voice_channel(name=f"{member.name}'s channel",
                                                                                   category=self.client.get_channel(
                                                                                       server_preference_data[5]),
                                                                                   user_limit=0)
                    c.execute("""INSERT INTO voice_user_data(voice_owner_id,voice_name,voice_limit)
                                                VALUES(?,?,?)""",
                              (member.id, f"{member.name}'s channel", 0))
                    conn.commit()
                    c.execute("""INSERT INTO voice_data (voice_owner_id, voice_channel_id,guild_id)
                                                                VALUES(?,?,?)""",
                              (member.id, voice_channel.id, member.guild.id))
                await voice_channel.set_permissions(self.client.user, connect=True, read_messages=True)
                await voice_channel.set_permissions(member, connect=True, read_messages=True)
                try:
                    await member.move_to(voice_channel)
                except:
                    await voice_channel.delete()
            else:
                c.execute("""select * from voice_data
                                                            where voice_channel_id= :voice_channel_id""",
                          {"voice_channel_id": before.channel.id})
                data = c.fetchone()
                conn.commit()
                if data is not None and len(before.channel.members) == 0:
                    c.execute("""DELETE FROM voice_data WHERE voice_channel_id = :voice_channel_id""",
                              {"voice_channel_id": before.channel.id})
                    conn.commit()
                    await before.channel.delete()
        elif after.channel != before.channel and after.channel is not None:  # he joined a voice channel
            if after.channel.id == server_preference_data[6]:
                c.execute("""SELECT * FROM voice_user_data
                                                                   WHERE voice_owner_id = :owner_id""",
                          {"owner_id": member.id})
                voice_user_data = c.fetchone()
                conn.commit()
                if voice_user_data is not None:  # if he had a channel before
                    voice_channel = await after.channel.guild.create_voice_channel(name=voice_user_data[1],
                                                                                   category=self.client.get_channel(
                                                                                       server_preference_data[5]),
                                                                                   user_limit=voice_user_data[2])
                    c.execute("""INSERT INTO voice_data (voice_owner_id, voice_channel_id,guild_id)
                                                                                    VALUES(?,?,?)""",
                              (member.id, voice_channel.id, member.guild.id))
                    conn.commit()
                else:
                    voice_channel = await after.channel.guild.create_voice_channel(name=f"{member.name}'s channel",
                                                                                   category=self.client.get_channel(
                                                                                       server_preference_data[5]),
                                                                                   user_limit=0)
                    c.execute("""INSERT INTO voice_user_data(voice_owner_id,voice_name,voice_limit)
                                                VALUES(?,?,?)""",
                              (member.id, f"{member.name}'s channel", 0))
                    conn.commit()
                    c.execute("""INSERT INTO voice_data (voice_owner_id, voice_channel_id,guild_id)
                                                                VALUES(?,?,?)""",
                              (member.id, voice_channel.id, member.guild.id))
                await voice_channel.set_permissions(self.client.user, connect=True, read_messages=True)
                await voice_channel.set_permissions(member, connect=True, read_messages=True)
                await member.move_to(voice_channel)
        elif after.channel is None:  # he left a channel
            if len(before.channel.members) == 0:  # checks if the channel is empty
                c.execute("""SELECT * FROM voice_data
                                            WHERE voice_channel_id = :voice_channel_id""",
                          {"voice_channel_id": before.channel.id})
                voice_data = c.fetchone()
                if voice_data is not None:
                    c.execute("""DELETE FROM voice_data WHERE voice_channel_id = :voice_channel_id""",
                              {"voice_channel_id": before.channel.id})
                    conn.commit()
                    await before.channel.delete()

    @commands.group(name="voice")
    async def voice(self, ctx: commands.Context):
        """
        just creates a group the commands by itself doesnt do any thing
        future? make this the help command for the whole voice
        :param ctx:
        """
        pass

    @voice.command()
    async def help(self, ctx):
        conn = sqlite3.connect("discord_bot.db")
        c = conn.cursor()
        c.execute("""select prefix,join_to_create_a_room_channel_id from server_preference
        where guild_id = :guild_id""", {"guild_id": ctx.guild.id})
        data = c.fetchone()
        conn.close()
        prefix = data[0]
        embed = discord.Embed(title="voice help", colour=0xFFFF00)
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
        embed.set_thumbnail(url="https://i.imgur.com/RqrPc2T.png")
        embed.add_field(name=f"**{prefix}voice lock**",
                        value="makes the room locked* so you are the only one who can enter the room\n **everyone will be able to see the channel but would not be abl enter**",
                        inline=False)
        embed.add_field(name=f"**{prefix}voice unlock**", value="makes the room open so everyone can enter",
                        inline=False)
        embed.add_field(name="**" + prefix + "voice name {name}**", value="changes the name of the room", inline=False)
        embed.add_field(name="**" + prefix + "voice limit {limit}**",
                        value="makes the room limited to {limit} amount of members if you put 0there will be no limit",
                        inline=False)
        embed.add_field(name="**" + prefix + "voice permit {@user}**", value="lets {user} enter the room", inline=False)
        embed.add_field(name="**" + prefix + "voice reject {@user}**",
                        value="makes the room unavailable* to {user} \n **the {user} will see the channel but he would not be able enter**",
                        inline=False)
        embed.add_field(name="**" + prefix + "voice claim**",
                        value="if you are in a room which the owner is not in you will be the owner of the room",
                        inline=False)
        if data[1] is not None:
            await ctx.send(f"you create a channel by joining {data[1]}")
        else:
            await ctx.send(f"contact the sever admin tp setup the voice muddle")
        await ctx.send(embed=embed)

    @voice.command()
    async def name(self, ctx: commands.Context, *args):
        """
        the commands gets an args
        :param ctx: commands.Context
        """
        if args is not None:
            change_name = " ".join(args)
        else:
            await ctx.send(f"{ctx.author.mention} you cant change it to nothing")
            return None
        try:
            voice_channel = ctx.author.voice.channel
            conn = sqlite3.connect("discord_bot.db")
            c = conn.cursor()
            c.execute("""SELECT * FROM voice_data
                        WHERE voice_channel_id = :voice_channel_id""", {"voice_channel_id": voice_channel.id})
            conn.commit()
            voice_data = c.fetchone()
            if voice_data[0] == ctx.author.id:
                await voice_channel.edit(name=change_name)
                c.execute("""UPDATE voice_user_data
                            SET voice_name = :voice_name
                            WHERE voice_owner_id = :voice_owner_id""",
                          {"voice_name": change_name, "voice_owner_id": ctx.author.id})
                conn.commit()

                await ctx.send(f"{ctx.author.mention} you have successfully changed the channel name to {change_name}")
            else:
                await ctx.send(f"{ctx.author.mention} you are not the owner of the voice channel")
            conn.close()
        except ValueError:
            await ctx.send(f"{ctx.author.mention} you have to be in the voice channel")

    @voice.command()
    async def lock(self, ctx: commands.Context):
        author = ctx.author
        try:
            currant_voice_channel = ctx.author.voice.channel
            conn = sqlite3.connect("discord_bot.db")
            c = conn.cursor()
            c.execute(""" SELECT * FROM voice_data
                        WHERE voice_channel_id = :voice_channel_id """, {"voice_channel_id": currant_voice_channel.id})
            voice_data = c.fetchone()
            conn.commit()
            conn.close()
            if voice_data[0] == author.id:
                await currant_voice_channel.set_permissions(ctx.guild.roles[0], connect=False)
                await ctx.send(f"{ctx.author.mention} the channel has been locked down")
            else:
                await ctx.send(f"{ctx.author.mention} you cant lock the channel")
        except ValueError:
            await ctx.send(f"{ctx.author.mention} you have to be in the voice channel")

    @voice.command()
    async def unlock(self, ctx: commands.Context):
        try:
            author = ctx.author
            currant_voice_channel = author.voice.channel
            conn = sqlite3.connect("discord_bot.db")
            c = conn.cursor()
            c.execute("""SELECT * FROM voice_data
                        WHERE voice_channel_id = :voice_channel_id""", {"voice_channel_id": currant_voice_channel.id})
            voice_data = c.fetchone()
            conn.commit()
            conn.close()
            if voice_data[0] == author.id:
                await currant_voice_channel.set_permissions(ctx.guild.roles[0], connect=True)
                await ctx.send(f"{author.mention} the channel has been unlocked")
            else:
                await ctx.send(f"{author.mention} you d'ont own the voice channel")
        except ValueError:
            await ctx.send(f"{ctx.author.mention} you have to be in the voice channel")

    @voice.command()
    async def limit(self, ctx: commands.Context, limit: int):
        author = ctx.author
        try:
            if int(limit) >= 0:
                currant_voice_channel = author.voice.channel
                conn = sqlite3.connect("discord_bot.db")
                c = conn.cursor()
                c.execute("""SELECT * FROM voice_data
                                        WHERE voice_channel_id = :voice_channel_id""",
                          {"voice_channel_id": currant_voice_channel.id})
                voice_data = c.fetchone()
                if voice_data[0] == author.id:
                    await currant_voice_channel.edit(user_limit=int(limit))
                    c.execute("""UPDATE voice_user_data
                    SET voice_limit = :voice_limit
                    WHERE voice_owner_id = :voice_owner_id
                    """, {"voice_limit": limit, "voice_owner_id": author.id})
                    conn.commit()
                    await ctx.send(f"{author.mention} you have successfully changed the voice channel limit to {limit}")
                else:
                    await ctx.send(f"{author.mention} you are not the channel owner")
                conn.close()
            else:
                await ctx.send(f"{author.mention} you cant place a negative number as a voice limit")
        except AttributeError:
            await ctx.send(f"{author.mention} you are not in the channel ")
        except ValueError:
            await ctx.send(f"{author.mention} you are didn't give a number")

    @voice.command()
    async def claim(self, ctx: commands.Context):
        try:
            voice_channel = ctx.author.voice.channel
            conn = sqlite3.connect("discord_bot.db")
            c = conn.cursor()
            c.execute("""SELECT * FROM voice_data
            WHERE voice_channel_id = :channel_id""", {"channel_id": voice_channel.id})
            data = c.fetchone()
            if data is not None:
                if ctx.guild.get_member(data[0]) not in voice_channel.members:
                    c.execute("""UPDATE voice_data
                    SET voice_owner_id = :member_id
                    WHERE voice_channel_id = :channel_id""",
                              {"member_id": ctx.author.id, "channel_id": voice_channel.id})
                    c.execute("""SELECT * FROM voice_user_data
                    WHERE voice_owner_id = :member_id""", {"member_id": ctx.author.id})
                    voice_user_data = c.fetchone()
                    if voice_user_data is None:
                        c.execute("""INSERT INTO voice_user_data(voice_owner_id, voice_name, voice_limit)
                        VALUES (?,?,?)""", (ctx.author.id, voice_channel.name, voice_channel.user_limit))
                    else:
                        c.execute("""UPDATE voice_user_data
                        SET voice_name = :name , voice_limit = :limit
                        WHERE voice_owner_id = :voice_owner_id""",
                                  {"name": voice_channel.name, "limit": voice_channel.user_limit,
                                   "voice_owner_id": ctx.author.id})
                    conn.commit()
                    await voice_channel.set_permissions(ctx.author, connect=True)
                    await voice_channel.set_permissions(ctx.guild.get_member(data[0]), connect=True)
                    await ctx.send(f"{ctx.author.mention} you now own the chanel")
                else:
                    await ctx.send(f"{ctx.author.mention} the owner of the channel is in the channel")
            conn.commit()
            conn.close()
        except ValueError:
            await ctx.send(f"{ctx.author.mention} you are not in a channel")

    @voice.command()
    async def reject(self, ctx: commands.Context, member: discord.Member):
        try:
            conn = sqlite3.connect("discord_bot.db")
            c = conn.cursor()
            c.execute("""SELECT * FROM voice_data
            WHERE voice_channel_id = :channel_id""", {"channel_id": ctx.author.voice.channel.id})
            data = c.fetchone()
            if data is not None and data[0] == ctx.author.id:
                if member.id != self.client.user.id:
                    if member.voice is not None:
                        await member.move_to(None)
                    await ctx.author.voice.channel.set_permissions(member, connect=False)
                    await ctx.send(f"{ctx.author.mention} you have rejected {member.mention} from your voice channel")
                else:
                    await ctx.send(f"{ctx.author.mention} you cant reject me :)")
            else:
                await ctx.send(f"{ctx.author.mention} you are not the owner of the voice")
        except ValueError:
            await ctx.send(f"{ctx.author.mention} you have to be in the voice_channel")

    @voice.command()
    async def permit(self, ctx: commands.Context, member: discord.Member):
        try:
            conn = sqlite3.connect("discord_bot.db")
            c = conn.cursor()
            c.execute("""SELECT * FROM voice_data
            WHERE voice_channel_id = :channel_id""", {"channel_id": ctx.author.voice.channel.id})
            data = c.fetchone()
            if data is not None and data[0] == ctx.author.id:
                if member.id != self.client.user.id:
                    await ctx.author.voice.channel.set_permissions(member, connect=True)
                    await ctx.send(f"{ctx.author.mention} you have permit {member.mention} to join your voice channel")
                else:
                    await ctx.send(f"{ctx.author.mention} you cant reject me :)")
            else:
                await ctx.send(f"{ctx.author.mention} you are not the owner of the voice")
        except ValueError:
            await ctx.send(f"{ctx.author.mention} you have to be in the voice_channel")


def setup(client):
    client.add_cog(Voice(client))
