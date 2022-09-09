import discord
from discord.ext import commands

class Info(commands.Cog):
    """Custom help command embed."""
    def __init__(self, client):
        self.client = client

    # custom help command
    @commands.command()
    async def info(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        embed = discord.Embed (
            title = "This is a list of Jmmib's commands",
            color=0xffc90d
        )

        # default help command
        embed.add_field (
            name = "help",
            value = "Displays the bot's default help command.",
            inline=False
        )

        # info
        embed.add_field (
            name = "info",
            value = "Alternate help command embed that you're looking at right now.",
            inline=False
        )

        # rank
        embed.add_field (
            name = "rank",
            value = "Displays your Jmmib level and exp.",
            inline=False
        )

        # bot versiom
        embed.add_field (
            name = "version / botversion / botver",
            value = "Python version for the bot.",
            inline=False
        )

        # user info
        embed.add_field (
            name = "userinfo",
            value = "Command to fetch user info.",
            inline=False
        )
        
        # footer
        embed.set_footer(text="jmm")

        await ctx.channel.trigger_typing()
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Info(client))