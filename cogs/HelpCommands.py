from discord.ext import commands

from Globals import Globals


async def help_error(ctx, *args):  # error has to be in there
        c = Globals.conn.cursor()
        c.execute("""SELECT * FROM server_preference
                       WHERE guild_id = :guild_id""",
                  {"guild_id": ctx.guild.id})
        data = c.fetchone()
        role = data[4]
        if args is not ():
            reason = " ".join(args)
        else:
            reason = "an unspecified reason"
        if role is not None:
            role = f'<@&{role}>'
            await ctx.send(f"{ctx.author.mention} needs help at an unknown place for {reason} {role}")
        else:
            await ctx.send(f"{ctx.author.mention} needs help at an unknown place for {reason}")


class HelpCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(name="help", ivoke_without_command=False)
    async def help(self, ctx, *args):
        try:
            await ctx.message.delete()
            channel1 = ctx.author.voice.channel
            invite = await channel1.create_invite(max_age=60)
            c = Globals.conn.cursor()
            c.execute("""SELECT * FROM server_preference
                           WHERE guild_id = :guild_id""",
                      {"guild_id": ctx.guild.id})
            data = c.fetchone()
            role = data[4]
            print(args)
            if args is not ():
                reason = " ".join(args)
            else:
                reason = "an unspecified reason"
            if role is not None:
                role = f'<@&{role}>'
                await ctx.send(f"{ctx.author.mention} needs help at {invite} {role} for {reason}")
                await ctx.send(f"{ctx.author.mention} if you meant to get the commands do help ")
            else:
                await ctx.send(f"{ctx.author.mention} needs help at {invite} for {reason}")
        except AttributeError:
            await help_error(ctx,*args)


def setup(client):
    client.add_cog(HelpCommands(client))
