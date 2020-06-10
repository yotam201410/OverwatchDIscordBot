import sqlite3

from discord.ext import commands


def return_category(guild, category_to_check):
    category_dict = {}
    for i in guild.categories:
        category_dict[i.id] = i
    try:
        return category_dict[category_to_check]
    except KeyError:
        return None


class MemberCount(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, ctx):
        conn = sqlite3.connect("discord_bot.db")
        c = conn.cursor()
        c.execute("""SELECT * FROM member_count
                WHERE guild_id = :guild_id""", {"guild_id": ctx.guild.id})
        data2 = c.fetchone()
        conn.commit()
        if data2 is not None:
            channel = ctx.guild.get_channel(data2[1])
            await channel.edit(name=f"Member Count: {len(ctx.guild.members)}")
    @commands.Cog.listener()
    async def on_member_remove(self,ctx):
        conn = sqlite3.connect("discord_bot.db")
        c = conn.cursor()
        c.execute("""SELECT * FROM member_count
                        WHERE guild_id = :guild_id""", {"guild_id": ctx.guild.id})
        data2 = c.fetchone()
        conn.commit()
        if data2 is not None:
            channel = ctx.guild.get_channel(data2[1])
            await channel.edit(name=f"Member Count: {len(ctx.guild.members)}")

    @commands.group(name="mc")
    @commands.has_permissions(administrator=True)
    async def mc(self, ctx):
        pass

    @mc.command()
    @commands.has_permissions(administrator=True)
    async def member(self, ctx):
        conn = sqlite3.connect("discord_bot.db")
        c = conn.cursor()
        c.execute("""SELECT * FROM server_preference
        WHERE guild_id = :guild_id""", {"guild_id": ctx.guild.id})
        data = c.fetchone()
        c.execute("""SELECT * FROM member_count
        WHERE guild_id = :guild_id""", {"guild_id": ctx.guild.id})
        data2 = c.fetchone()
        conn.commit()
        if data[7] is not None and data2 is None:
            channel = await return_category(ctx.guild, data[7]).create_voice_channel(
                name=f"Member Count: {len(ctx.guild.members)}")
            await channel.set_permissions(ctx.guild.roles[0], connect=False)
            c.execute("""INSERT INTO member_count(guild_id, member_count_channel_id)
                                VALUES(?,?)""", (ctx.guild.id, channel.id))
            conn.commit()
        else:
            await ctx.send(f"{ctx.author.mention} you havent done the setup member_count command")
        conn.close()


def setup(client):
    client.add_cog(MemberCount(client))
