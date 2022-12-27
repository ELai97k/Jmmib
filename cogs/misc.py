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
        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(Misc(client))

async def teardown(client):
    await client.remove_cog(Misc(client))