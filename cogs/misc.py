import discord
from discord.ext import commands

class Misc(commands.Cog):
    """Cog for basic and misc commands."""
    def __init__(self, client):
        self.client = client

    # test command
    @commands.command(help="This is a test command.")
    async def test(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        await ctx.send("This is a test command.")
        print("This is a test command and it works.")


    # ping command
    @commands.command(help="Ping command for bot latency.")
    async def ping(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        await ctx.send(f"Pong. Latency is {round (self.client.latency * 1000)} ms.")


    # test embed
    @commands.command(help="This is a test embed.")
    async def embed(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        embed = discord.Embed (
            title = "Hello world",
            description = "This is a test embed.",
            color=0xffc90d
        )
        embed.set_footer(text="Thank you for reading")
        await ctx.send(embed=embed)


    # bot python version
    @commands.command(help="Command for the bot's Python version.")
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
    client.add_cog(Misc(client))