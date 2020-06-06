import discord
from discord.ext import commands
import sqlite3


def return_category(guild, category_to_check):
    category_dict = {}
    for i in guild.categories:
        category_dict[i.id] = i
    try:
        return category_dict[category_to_check]
    except KeyError:
        return None


def in_category(category_to_check, guild):
    for category in guild.categories:
        if category.id == category_to_check:
            return True
    return False


class ServerPreference(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(name="setup", invoke_without_command=True)
    @commands.has_permissions(administrator=True)
    async def setup(self, ctx):
        conn = sqlite3.connect(
            "discord_bot.db")
        c = conn.cursor()
        c.execute("""SELECT * FROM server_preference
                       WHERE guild_id = :guild_id""",
                  {"guild_id": ctx.guild.id})
        conn.commit()
        data = c.fetchone()
        conn.close()
        prefix = data[1]
        embed = discord.Embed(title="**Welcome to Valorant Bubbles Bot**", color=0xFF0000)
        # embed.set_image(url=self.client.get_guild(681609760843366406).icon_url_as(format='jpg'))
        embed.add_field(name="What is this bot?",
                        value="This is Valorant Bubbles Bot it contains a lot of plugins like moderation voice create "
                              "and more")
        embed.add_field(name="Who programed it?", value="<@342725139626065920>")
        embed.add_field(name="**How do i set up the bot? there is some commands:**", value="")
        embed.add_field(name=f"{prefix}change_perfix", value="change the prefix of the bot")
        embed.add_field(name=f"{prefix}set_report_channel",
                        value="sets the channel that you would get the reports to by "
                              "putting")
        embed.add_field(name=f"{prefix}set_moderation_role",
                        value="sets the moderation role by putting moderation role id")

    @commands.command()
    async def change_prefix(self, ctx, prefix):
        conn = sqlite3.connect(
            "discord_bot.db")
        c = conn.cursor()
        c.execute("""
        UPDATE server_preference
        SET prefix = :prefix 
        WHERE guild_id = :guild""", {"prefix": prefix, "guild": ctx.guild.id})
        conn.commit()
        conn.close()

    @setup.command()
    @commands.has_permissions(administrator=True)
    async def report_channel(self, ctx, channel_id):
        try:
            channel_id = int(channel_id)
            if ctx.guild.get_channel(channel_id) is not None:
                conn = sqlite3.connect(
                    "discord_bot.db")
                c = conn.cursor()
                c.execute("""
                UPDATE server_preference
    SET report_mod_channel_id = :channel_id 
    WHERE guild_id = :guild""", {"channel_id": channel_id, "guild": ctx.guild.id})
                conn.commit()
                conn.close()
                await ctx.send(f"you have successfully set the report channel id to {channel_id} ")
            else:
                await ctx.send("you gave me not a channel id")
        except ValueError:
            await ctx.send("you gave us not an id")

    @setup.command()
    @commands.has_permissions(administrator=True)
    async def moderator_role(self, ctx, role_id):
        try:
            role_id = int(role_id)
            if ctx.guild.get_role(role_id) is not None:
                conn = sqlite3.connect(
                    "discord_bot.db")
                c = conn.cursor()
                c.execute("""
                UPDATE server_preference
    SET mods_role_id = :role_id 
    WHERE guild_id = :guild""", {"role_id": role_id, "guild": ctx.guild.id})
                conn.commit()
                await ctx.send(f"you have successfully set the moderator role id to {role_id} ")
                conn.close()
            else:
                await ctx.send("you have gave me not a role id")
        except ValueError:
            await ctx.send("you have gave me not an id")

    @setup.command()
    @commands.has_permissions(administrator=True)
    async def helper_role(self, ctx, role_id):
        try:
            role_id = int(role_id)
            if ctx.guild.get_role(role_id) is not None:
                conn = sqlite3.connect(
                    "discord_bot.db")
                c = conn.cursor()
                c.execute("""
                    UPDATE server_preference
        SET helpers_role_id = :role_id 
        WHERE guild_id = :guild""", {"role_id": role_id, "guild": ctx.guild.id})
                conn.commit()
                await ctx.send(f"you have successfully set the helpers role id to {role_id} ")
                conn.close()
            else:
                await ctx.send("you have gave me not a role id")
        except ValueError:
            await ctx.send("you have gave me not an id")

    @setup.command()
    @commands.has_permissions(administrator=True)
    async def audit_log_channel(self, ctx: commands.Context, channel_id):
        try:
            channel_id = int(channel_id)
            channel = self.client.get_channel(channel_id)
            if channel is not None:
                conn = sqlite3.connect(
                    "discord_bot.db")
                c = conn.cursor()
                c.execute("""
                                                    UPDATE server_preference
                                        SET audit_log_channel_id = :channel_id 
                                        WHERE guild_id = :guild""",
                          {"channel_id": channel_id, "guild": ctx.guild.id})
                conn.commit()
                conn.close()
                await ctx.send(f"you have successfully set the command log channel ID to {channel_id} ")
            else:
                await ctx.send(f"you have not gave a channel ID")
        except ValueError:
            await ctx.send(f"you have not gave an ID")

    @setup.command()
    @commands.has_permissions(administrator=True)
    async def commands_log_channel(self, ctx: commands.Context, channel_id):
        try:
            channel_id = int(channel_id)
            channel = self.client.get_channel(channel_id)
            if channel is not None:
                conn = sqlite3.connect(
                    "discord_bot.db")
                c = conn.cursor()
                c.execute("""
                                                    UPDATE server_preference
                                        SET commands_log_channel_id = :channel_id 
                                        WHERE guild_id = :guild""", {"channel_id": channel_id, "guild": ctx.guild.id})
                conn.commit()
                conn.close()
                await ctx.send(f"you have successfully set the command log channel ID to {channel_id} ")
            else:
                await ctx.send(f"you have not gave a channel ID")
        except ValueError:
            await ctx.send(f"you have not gave an ID")

    @setup.command()
    @commands.has_permissions(administrator=True)
    async def voice_create_category(self, ctx, category_id):
        print(True)
        try:
            category_id = int(category_id)
            if in_category(category_id, ctx.guild):
                conn = sqlite3.connect(
                    "discord_bot.db")
                c = conn.cursor()
                c.execute("""
                                    UPDATE server_preference
                        SET join_to_create_a_room_category_id = :category_id 
                        WHERE guild_id = :guild""", {"category_id": category_id, "guild": ctx.guild.id})
                conn.commit()
                conn.close()
                await ctx.send(f"you have successfully set the joint to crate a category ID to {category_id} ")
            else:
                await ctx.send(f"you gave a None category ID")
        except ValueError:
            await ctx.send(f"you have not gave an ID")

    @setup.command()
    @commands.has_permissions(administrator=True)
    async def voice(self, ctx):
        conn = sqlite3.connect("discord_bot.db")
        c = conn.cursor()
        c.execute("""SELECT * FROM server_preference
                       WHERE guild_id = :guild_id""",
                  {"guild_id": ctx.guild.id})
        data = c.fetchone()
        conn.commit()
        if data[5] is None or return_category(ctx.guild, data[5]) is None:
            await ctx.send("you didn't use the voice_create_category command")
        else:
            if data[6] is None or ctx.guild.get_channel(data[6]) is None:
                voice_channel = await return_category(ctx.guild, data[5]).create_voice_channel(
                    name="join to create a channel")
                c.execute("""UPDATE server_preference
                SET join_to_create_a_room_channel_id= :channel_id
                WHERE guild_id = :guild_id""", {"channel_id": voice_channel.id, "guild_id": ctx.guild.id})
                conn.commit()
            else:
                await ctx.send("you have already crated a channel ")
        conn.close()

    @setup.command()
    async def member_count(self, ctx):
        category = await ctx.guild.create_category(name="📊 Server Stats 📊")
        conn = sqlite3.connect("discord_bot.db")
        c = conn.cursor()
        c.execute("""UPDATE server_preference
                    SET member_count_category_id = :category_id
                    WHERE guild_id = :guild_id""", {"category_id": category.id, "guild_id": ctx.guild.id})
        await ctx.send(f"{ctx.author.mention} you have successfully enabled member count")
        conn.commit()
        conn.close()
    @setup.command()
    @commands.has_permissions(administrator=True)
    async def pug(self,ctx:commands.Context,limit:int):
        conn = sqlite3.connect("discord_bot.db")
        c = conn.cursor()
        if limit == 10 or limit == 12:
            c.execute("""UPDATE server_preference
            set pug_match_user_limit = :limit
            where guild_id = :guild_id""",{"guild_id":ctx.guild.id,"limit":limit})
            await ctx.send(f"{ctx.author.mention} you have seccesfull set the pug limit to {limit}")
        else:
            await ctx.send(f"{ctx.author.mention} you can only set them to 10 or 12")


    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        conn = sqlite3.connect(
            "discord_bot.db")
        c = conn.cursor()
        c.execute("""INSERT INTO server_preference(guild_id,prefix)
        SELECT :guild_id, :prefix
        WHERE NOT EXISTS (SELECT 1 FROM server_preference WHERE guild_id = :guild_id)""",
                  {"guild_id": guild.id, "prefix": "!"})
        conn.commit()
        conn.close()

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        conn = sqlite3.connect(
            "discord_bot.db")
        c = conn.cursor()
        c.execute("""DELETE FROM server_preference WHERE guild_id=:guild_id""",
                  {"guild_id": guild.id})
        conn.commit()
        conn.close()


def setup(client):
    client.add_cog(ServerPreference(client))
