import discord
from discord.ext import commands

class Version(commands.Cog):
    """Bot's Python version cog."""
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["ver", "botver", "botversion"], help="Command for the bot's current Python version.")
    async def version(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return
            
        embed = discord.Embed (
            title = "Current version",
            description = "```python-3.10.7```",
            color=0xffc90d
        )
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Version(client))