import discord
from discord.ext import commands

class Info(commands.Cog):
    """Alternate help command for the bot."""
    def __init__(self, client):
        self.client = client

    # custom help command
    @commands.command(help="This is the bot's custom help embed.")
    async def info(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        embed = discord.Embed (
            title = "This is a list of Jmmib's commands",
            color=0xffc90d
        )

        # info
        embed.add_field (
            name = "info",
            value = "Custom help command embed that you're looking at right now.",
            inline=False
        )

        # default help command
        embed.add_field (
            name = "help",
            value = "Displays the bot's default help command.",
            inline=False
        )

        # rank
        embed.add_field (
            name = "rank",
            value = "Displays your Jmmib level and exp.",
            inline=False
        )

        # user info
        embed.add_field (
            name = "userinfo",
            value = "Command to fetch user info.",
            inline=False
        )

        # server info
        embed.add_field (
            name = "serverinfo",
            value = "Command to fetch server info.",
            inline=False
        )
        
        # footer
        embed.set_footer(text="jmm")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Info(client))
