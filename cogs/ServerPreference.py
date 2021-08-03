import discord
from discord.ext import commands, tasks

from Globals import Globals


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


def check_if_it_commands(category):
    c = Globals.conn.cursor()
    c.execute("""select cat_id from pug_channels 
    where cat_id = :cat_id""", {"cat_id": category.id})
    data = c.fetchone()
    print(data)
    return True if data is not None else False


async def update_channels(role: discord.Role):
    for channel in role.guild.channels:
        if str(channel.category) not in ["6V6 pugs", "5V5 pugs", None]:
            await channel.set_permissions(role, connect=False)


class ServerPreference(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.group(name="setup")
    @commands.has_permissions(administrator=True)
    async def setup(self, ctx):
        pass

    @commands.command()
    async def change_prefix(self, ctx, prefix):
        c = Globals.conn.cursor()
        c.execute("""
        UPDATE server_preference
        SET prefix = :prefix 
        WHERE guild_id = :guild""", {"prefix": prefix, "guild": ctx.guild.id})
        Globals.conn.commit()
        await ctx.send(f"prefix has been changed to {prefix}")

    @setup.command()
    @commands.has_permissions(administrator=True)
    async def help(self, ctx):
        c = Globals.conn.cursor()
        c.execute("""select prefix from server_preference
            where guild_id = :guild_id""", {"guild_id": ctx.guild.id})
        data = c.fetchone()
        prefix = data[0]
        embed = discord.Embed(title="setup help", colour=0xff0000)
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
        embed.set_thumbnail(url=self.client.user.default_avatar_url)
        embed.add_field(name="**" + prefix + "change_prefix {prefix}**",
                        value="changes the command prefix\n **the prefix can only be between 1-5 chars**",
                        inline=False)
        embed.add_field(name="**" + prefix + "setup report_channel {channel id}**",
                        value="changes/sets the place where the reports will be sent",
                        inline=False)
        embed.add_field(name="**" + prefix + "setup moderator_role {role id}**",
                        value="changes/sets the moderator role id",
                        inline=False)
        embed.add_field(name="**" + prefix + "setup helper_role {role id}**", value="changes/sets the helpers role id",
                        inline=False)
        embed.add_field(name="**" + prefix + "setup audit_log_channel {channel id}**",
                        value="changes/sets the place where the audit log messages will be sent",
                        inline=False)
        embed.add_field(name="**" + prefix + "setup commands_log_channel {channel id} **",
                        value="changes/sets the place where the commands log messages will be sent",
                        inline=False)
        embed.add_field(name="**" + prefix + "setup voice_create_category {category id}**",
                        value="changes/sets the place where the join to create a channel channel will be created",
                        inline=False)
        embed.add_field(name="**" + prefix + "setup voice**", value="creates the join to create a channel",
                        inline=False)
        embed.add_field(name="**" + prefix + "setup member_count**", value="create the member count channel",
                        inline=False)
        embed.add_field(name="**" + prefix + "setup pug {limit}**",
                        value="create a pugs category with according to the limit",
                        inline=False)
        await ctx.send(embed=embed)

    @setup.command()
    @commands.has_permissions(administrator=True)
    async def report_channel(self, ctx, channel_id):
        try:
            channel_id = int(channel_id)
            if ctx.guild.get_channel(channel_id) is not None:
                c = Globals.conn.cursor()
                c.execute("""
                UPDATE server_preference
    SET report_mod_channel_id = :channel_id 
    WHERE guild_id = :guild""", {"channel_id": channel_id, "guild": ctx.guild.id})
                Globals.conn.commit()
                await ctx.send(f"you have successfully set the report channel id to {channel_id} ")
            else:
                await ctx.send("you gave me not a channel id")
        except ValueError:
            await ctx.send("you gave us not an id")

    @setup.command()
    @commands.has_permissions(administrator=True)
    async def enable_moderation(self, ctx: commands.Context):
        c = Globals.conn.cursor()
        c.execute("""update server_preference
        set moderation = :true
        where guild_id = :guild_id""", {"guild_id": ctx.guild.id, "true": "true"})
        Globals.conn.commit()
        await ctx.send("you have successfully enabled moderation")

    @setup.command()
    @commands.has_permissions(administrator=True)
    async def disable_moderation(self, ctx: commands.Context):
        c = Globals.conn.cursor()
        c.execute("""update server_preference
        set moderation = :true
        where guild_id = :guild_id""", {"guild_id": ctx.guild.id, "true": "false"})
        Globals.conn.commit()
        await ctx.send("you have successfully disabled moderation")

    @setup.command()
    @commands.has_permissions(administrator=True)
    async def moderator_role(self, ctx, role_id):
        try:
            role_id = int(role_id)
            if ctx.guild.get_role(role_id) is not None:
                c = Globals.conn.cursor()
                c.execute("""
                UPDATE server_preference
    SET mods_role_id = :role_id 
    WHERE guild_id = :guild""", {"role_id": role_id, "guild": ctx.guild.id})
                Globals.conn.commit()
                await ctx.send(f"you have successfully set the moderator role id to {role_id} ")
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
                c = Globals.conn.cursor()
                c.execute("""
                    UPDATE server_preference
        SET helpers_role_id = :role_id 
        WHERE guild_id = :guild""", {"role_id": role_id, "guild": ctx.guild.id})
                Globals.conn.commit()
                await ctx.send(f"you have successfully set the helpers role id to {role_id} ")
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
                c = Globals.conn.cursor()
                c.execute("""
                                                    UPDATE server_preference
                                        SET audit_log_channel_id = :channel_id 
                                        WHERE guild_id = :guild""",
                          {"channel_id": channel_id, "guild": ctx.guild.id})
                Globals.conn.commit()
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
                c = Globals.conn.cursor()

                c.execute("""
                                                    UPDATE server_preference
                                        SET commands_log_channel_id = :channel_id 
                                        WHERE guild_id = :guild""", {"channel_id": channel_id, "guild": ctx.guild.id})
                Globals.conn.commit()
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
                c = Globals.conn.cursor()
                c.execute("""
                                    UPDATE server_preference
                        SET join_to_create_a_room_category_id = :category_id 
                        WHERE guild_id = :guild""", {"category_id": category_id, "guild": ctx.guild.id})
                Globals.conn.commit()
                await ctx.send(f"you have successfully set the joint to crate a category ID to {category_id} ")
            else:
                await ctx.send(f"you gave a None category ID")
        except ValueError:
            await ctx.send(f"you have not gave an ID")

    @setup.command()
    @commands.has_permissions(administrator=True)
    async def voice(self, ctx):
        c = Globals.conn.cursor()
        c.execute("""SELECT * FROM server_preference
                       WHERE guild_id = :guild_id""",
                  {"guild_id": ctx.guild.id})
        data = c.fetchone()
        Globals.conn.commit()
        if data[5] is None or return_category(ctx.guild, data[5]) is None:
            await ctx.send("you didn't use the voice_create_category command")
        else:
            if data[6] is None or ctx.guild.get_channel(data[6]) is None:
                voice_channel = await return_category(ctx.guild, data[5]).create_voice_channel(
                    name="join to create a channel")
                c.execute("""UPDATE server_preference
                SET join_to_create_a_room_channel_id= :channel_id
                WHERE guild_id = :guild_id""", {"channel_id": voice_channel.id, "guild_id": ctx.guild.id})
                Globals.conn.commit()
            else:
                await ctx.send("you have already crated a channel ")

    @setup.command()
    async def member_count(self, ctx):
        category = await ctx.guild.create_category(name="📊 Server Stats 📊")
        c = Globals.conn.cursor()
        c.execute("""UPDATE server_preference
                    SET member_count_category_id = :category_id
                    WHERE guild_id = :guild_id""", {"category_id": category.id, "guild_id": ctx.guild.id})
        await ctx.send(f"{ctx.author.mention} you have successfully enabled member count")
        Globals.conn.commit()

    @setup.command()
    @commands.has_permissions(administrator=True)
    async def pug(self, ctx: commands.Context, limit: int):
        c = Globals.conn.cursor()
        if limit == 6 or limit == 5 or limit == 12 or limit == 12:
            if limit == 5 or limit == 10:
                cat = await ctx.guild.create_category(name="5V5 pugs")
                text_channel = await ctx.guild.create_text_channel(name="pugs chat", category=cat)
                voice_channel = await ctx.guild.create_voice_channel(name="waiting", category=cat)
                c.execute("""insert into pug_channels(guild_id, cat_id, commands_channel_id,voice_channel_id,pug_limit)
                 values (?,?,?,?,?)""", (ctx.guild.id, cat.id, text_channel.id, voice_channel.id, 5))
            else:
                cat = await ctx.guild.create_category(name="6V6 pugs")
                text_channel = await ctx.guild.create_text_channel(name="pugs chat", category=cat)
                voice_channel = await ctx.guild.create_voice_channel(name="waiting", category=cat)
                c.execute("""insert into pug_channels(guild_id, cat_id, commands_channel_id,voice_channel_id,pug_limit)
                                 values (?,?,?,?,?)""", (ctx.guild.id, cat.id, text_channel.id, voice_channel.id, 6))
            Globals.conn.commit()
            c.execute("""select pug_player_role from server_preference
            where guild_id = :guild_id""", {"guild_id": ctx.guild.id})
            if c.fetchone()[0] is None:
                role = await ctx.guild.create_role(name="pug player")
                c.execute("""update server_preference
                                set pug_player_role = :role_id
                                where guild_id = :guild_id""", {"guild_id": ctx.guild.id, "role_id": role.id})
                Globals.conn.commit()
                await update_channels(role)
            await ctx.send(
                f"You have successful setup a pugs category to {limit if limit == 5 or limit == 6 else limit / 2}V{limit if limit == 5 or limit == 6 else limit / 2}.\n"
                f"Feel free to change permissions names and more to the channels just **do not delete them.**\n"
                f"{'We have also created a new role called pug player **please do not delete it**, you can move it the position you want (it disable them from leaving the pugs room in that server).' if c.fetchone() is None else ''} ")
        else:
            await ctx.send("you can only enable pugs of 5V5 or 6V6.")

    @setup.command()
    async def delete_pug(self, ctx: commands.Context, category_id: int):
        cat = self.client.get_channel(category_id)
        print(cat)
        if cat is not None:
            print("its not none")
            if check_if_it_commands(cat):
                for channel in cat.channels:
                    print(channel)
                    await channel.delete()
                c = Globals.conn.cursor()
                c.execute("""delete from pug_channels
                    where cat_id = :cat_id""",
                          {"cat_id": cat.id})
                Globals.conn.commit()
                await cat.delete()
                await ctx.send(f"you have successfully deleted the category and the channels of the ({cat},{cat.id}")
            else:
                await ctx.send(f"{category_id} is not a pug category or its not a category")
        else:
            await ctx.send(f"{category_id} is not an id")

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        c = Globals.conn.cursor()
        c.execute("""INSERT INTO server_preference(guild_id,prefix)
        SELECT :guild_id, :prefix
        WHERE NOT EXISTS (SELECT 1 FROM server_preference WHERE guild_id = :guild_id)""",
                  {"guild_id": guild.id, "prefix": "!"})
        Globals.conn.commit()

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        c = Globals.conn.cursor()
        c.execute("""DELETE FROM server_preference WHERE guild_id=:guild_id""",
                  {"guild_id": guild.id})
        Globals.conn.commit()

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandNotFound):
            await self.help(ctx)
        else:
            raise error


def setup(client: commands.Bot):
    client.add_cog(ServerPreference(client))
