import sqlite3
import discord
from discord.ext import commands


class HelpCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(name="help", invoke_without_command=True)
    async def help(self, ctx, *args):
        await ctx.message.delete()
        channel1 = ctx.author.voice.channel
        invite = await channel1.create_invite(max_age=60)
        conn = sqlite3.connect(
            "discord_bot.db")
        c = conn.cursor()
        c.execute("""SELECT * FROM server_preference
                       WHERE guild_id = :guild_id""",
                  {"guild_id": ctx.guild.id})
        conn.commit()
        data = c.fetchone()
        role = data[4]
        if args is not []:
            reason = " ".join(args)
        else:
            reason = "Unspecified"
        if role is not None:
            role = f'<@&{role}>'
            await ctx.send(f"{ctx.author.mention} needs help at {invite} {role} for {reason}")
        else:
            await ctx.send(f"{ctx.author.mention} needs help at {invite} for {reason}")

    @help.command()
    async def voice(self, ctx):
        conn = sqlite3.connect("discord_bot.db")
        c = conn.cursor()
        c.execute("""select prefix,join_to_create_a_room_channel_id from server_preference
        where guild_id = :guild_id""", {"guild_id": ctx.guild.id})
        data = c.fetchone()
        conn.close()
        prefix = data[0]
        embed = discord.Embed(title="voice help", colour=0xFFFF00)
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
        await ctx.send(f"you create a channel by joining {data[1]}", embed=embed)

    @help.command()
    @commands.has_permissions(administrator=True)
    async def setup(self, ctx):
        conn = sqlite3.connect("discord_bot.db")
        c = conn.cursor()
        c.execute("""select prefix,join_to_create_a_room_channel_id from server_preference
        where guild_id = :guild_id""", {"guild_id": ctx.guild.id})
        data = c.fetchone()
        conn.close()
        prefix = data[0]
        embed = discord.Embed(title="setup help", colour=0xff0000)
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
        embed.add_field(name="**" + prefix + "setup pug**", value="sets/update the pug limit",
                        inline=False)
        await ctx.send(embed=embed)

    @help.error
    async def help_error(self, ctx, error):  # error has to be in there
        if commands.MissingRequiredArgument != AttributeError:
            conn = sqlite3.connect(
                "discord_bot.db")
            c = conn.cursor()
            c.execute("""SELECT * FROM server_preference
                           WHERE guild_id = :guild_id""",
                      {"guild_id": ctx.guild.id})
            conn.commit()
            data = c.fetchone()
            conn.close()
            role = data[4]
            if role is not None:
                role = f'<@&{role}>'
                await ctx.send(f"{ctx.author.mention} needs help at an unknown place {role}")
            else:
                await ctx.send(f"{ctx.author.mention} needs help at an unknown place")


def setup(client):
    client.add_cog(HelpCommands(client))
