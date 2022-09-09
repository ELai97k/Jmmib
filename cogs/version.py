import discord
from discord.ext import commands

class Version(commands.Cog):
    """Displays the Python version for the bot."""
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["botver", "botversion"])
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