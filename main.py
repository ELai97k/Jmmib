import discord
import os
import asyncio
from discord.ext import commands

intents = discord.Intents.default().all()
intents.members = True

# custom help command
class CustomHelpCommand(commands.HelpCommand):
    # cogs and commands
    async def send_bot_help(self, mapping):
        command_prefix = "+"
        embed = discord.Embed(title=f"{client.user.name}'s Cogs & Commands", color=0xffc90d)
        description = self.context.bot.description
        if description:
            embed.description = description

        for cog, commands in mapping.items():
            if cog is not None:
                name = cog.qualified_name
                filtered = await self.filter_commands(commands, sort=True)

                if filtered:
                    value = '\u2002 '.join('`' + c.name + '`' for c in commands if not c.hidden)

                    if cog and cog.description:
                        value = '{0}\n{1}'.format(cog.description, value)

                    embed.add_field(name=name, value=value, inline=True)
                    embed.set_footer(text=f"Use {command_prefix}help [cog] or {command_prefix}help [command] for more info.")

        await self.get_destination().send(embed=embed)

    # cog info
    async def send_cog_help(self, cog):
        command_prefix = "+"
        embed = discord.Embed (
            title = f"{cog.qualified_name} Commands",
            description = f"{cog.description}\n```{[command.name for command in cog.get_commands()]}```",
            color=0xffc90d
        )
        embed.set_footer(text=f"Use {command_prefix}help [command] for more info on a command.")
        await self.get_destination().send(embed=embed)

    # command info
    async def send_command_help(self, command):
        embed = discord.Embed (
            color=0xffc90d
        )
        embed.add_field (
            name=f"{command.name}",
            value=command.help,
            inline=False
        )
        await self.get_destination().send(embed=embed)

client = commands.Bot(command_prefix="+", 
help_command=CustomHelpCommand(), 
case_insensitive=True, 
intents=intents)

# cogs
async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f'cogs.{filename [:-3]}')

async def main():
    await load_extensions()
asyncio.run(main())

# on ready event
@client.event
async def on_ready():
    # bot login
    print(f"{client.user} logged in successfully!")

    # bot status
    await client.change_presence (
        activity = discord.Activity (
            type = discord.ActivityType.watching, name = "for goldjmmibs"
        )
    )

client.run(os.getenv("TOKEN"))