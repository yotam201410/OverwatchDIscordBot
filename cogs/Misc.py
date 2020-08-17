import discord
from discord.ext import commands


class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def find(self, ctx: commands.Context, member: discord.Member):
        try:
            voice = member.voice.channel
            await ctx.send(f"{member} is in {voice}")
            invite = await voice.create_invite(max_age=700)
            await ctx.send(f"{invite}")
        except AttributeError:
            await ctx.send(f"{member} is not in a voice channel")

    @commands.command()
    async def screenshare(self, ctx: commands.Context):
        server_id = ctx.guild.id
        format_1 = 'https://discordapp.com/channels/'
        voice_channel = ctx.author.voice.channel.id
        await ctx.send(f"{format_1}{server_id}/{voice_channel}")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"{round(self.client.latency * 1000)}ms")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def delete_channels(self, ctx: commands.Context):
        for channel in ctx.guild.channels:
            await channel.delete()


def setup(client):
    client.add_cog(Misc(client))
