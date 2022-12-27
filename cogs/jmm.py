from discord.ext import commands

class Jmm(commands.Cog):
    """jmm jumm"""
    def __init__(self, client):
        self.client = client

    # jmm jumm
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        if message.author.bot:
            return

        if "jmm" in message.content.lower():
            await message.channel.typing()
            await message.channel.send("jmm")

        if "jumm" in message.content.lower():
            await message.channel.typing()
            await message.channel.send("jumm")


async def setup(client):
    await client.add_cog(Jmm(client))

async def teardown(client):
    await client.remove_cog(Jmm(client))