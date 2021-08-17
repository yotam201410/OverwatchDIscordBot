import discord
from discord.ext import commands

from Globals import Globals


def return_category(guild: discord.Guild, category_id_to_check: int):
    category_dict = {i.id: i for i in guild.categories}
    if category_id_to_check in category_dict:
        return category_dict[category_id_to_check]
    return None


class ServerStats(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        c = Globals.conn.cursor()
        c.execute("""SELECT * FROM member_count
                WHERE guild_id = :guild_id""", {"guild_id": member.guild.id})
        data2 = c.fetchone()
        if data2 is not None:
            channel = member.guild.get_channel(data2[1])
            await channel.edit(name=f"Member Count: {len(member.guild.members)}")

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        c = Globals.conn.cursor()
        c.execute("""SELECT * FROM member_count
                        WHERE guild_id = :guild_id""", {"guild_id": member.guild.id})
        data2 = c.fetchone()
        if data2 is not None:
            channel = member.guild.get_channel(data2[1])
            await channel.edit(name=f"Member Count: {len(member.guild.members)}")

    @commands.group(name="server_stats", aliases=["ss", "st", "mc", "member_count"])
    @commands.has_permissions(administrator=True)
    async def server_stats(self, ctx: commands.Context):
        pass

    @server_stats.command()
    @commands.has_permissions(administrator=True)
    async def member(self, ctx: commands.Context):  # no category, category doesnt exist, already have a channel
        c = Globals.conn.cursor()
        c.execute("""SELECT prefix,member_count_category_id FROM server_preference
         WHERE guild_id = :guild_id""", {"guild_id": ctx.guild.id})
        server_preference_data = c.fetchone()
        prefix = server_preference_data[0]
        category_id = server_preference_data[1]
        c.execute("""SELECT member_count_channel_id FROM member_count
          where guild_id = :guild_id""", {"guild_id": ctx.guild.id})
        server_stats_data = c.fetchone()
        if server_stats_data:
            server_stats_data = server_stats_data[0]
        print(server_stats_data)
        if server_preference_data and return_category(ctx.guild, category_id):
            print(ctx.guild.get_channel(server_stats_data).category_id)
            if not server_stats_data:
                channel = await return_category(ctx.guild, category_id).create_voice_channel(
                    name=f"Member Count: {len(ctx.guild.members)}")
                await channel.set_permissions(ctx.guild.roles[0], connect=False)
                c.execute("""INSERT INTO member_count(guild_id, member_count_channel_id)
                                         VALUES(?,?)""", (ctx.guild.id, channel.id))
                Globals.conn.commit()
            elif not ctx.guild.get_channel(server_stats_data):
                print(ctx.guild.get_channel(server_stats_data))
                channel = await return_category(ctx.guild, category_id).create_voice_channel(
                    name=f"Member Count: {len(ctx.guild.members)}")
                await channel.set_permissions(ctx.guild.roles[0], connect=False)
                c.execute("""update member_count
                set member_count_channel_id = :channel_id 
                where guild_id = :guild_id""", {"channel_id": channel.id, "guild_id": ctx.guild.id})
                Globals.conn.commit()
            elif ctx.guild.get_channel(server_stats_data).category_id != category_id:
                await ctx.guild.get_channel(server_stats_data).edit(category=return_category(ctx.guild, category_id))
            else:
                await ctx.send(f"{ctx.author.mention} you all ready have a channel")
        else:
            await ctx.send(f"{ctx.author.mention} you have to use {prefix}setup server_stats")


def setup(client):
    client.add_cog(ServerStats(client))
