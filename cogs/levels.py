import discord
import json
import random
from discord.ext import commands
from discord.ext.commands import MissingPermissions
from datetime import datetime

class Levels(commands.Cog):
    """Level and EXP system."""
    def __init__(self, client):
        self.client = client

    # add new member to users.json
    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open('users.json', 'r') as f:
            users = json.load(f)

        await self.update_data(users, member)

        with open('users.json', 'w') as f:
            json.dump(users, f)

    # messages as exp
    @commands.Cog.listener()
    async def on_message(self, message):
      if not message.author.bot:
        with open('users.json','r') as f:
            users = json.load(f)
        await self.update_data(users, message.author)

        if(users[str(message.author.name)]['LastMessage'] < await self.to_integer(datetime.now())):
            await self.add_experience(users, message.author)
        await self.level_up(users, message.author, message.channel)

        with open('users.json', 'w') as f:
            json.dump(users, f)

    # update users' exp, level, and last message into users.json
    async def update_data(self, users, user):
        if not str(user.name) in users:
            users[str(user.name)] = {}
            users[str(user.name)]['experience'] = 0
            users[str(user.name)]['level'] = 1
            users[str(user.name)]['LastMessage'] = await self.to_integer(datetime.now())

    # add exp to users
    async def add_experience(self, users, user):
        users[str(user.name)]['experience'] += random.randint(15,25)
        users[str(user.name)]['LastMessage'] = await self.to_integer(datetime.now())

    # define exp, level start and level end
    async def level_up(self, users, user, message):
        experience = users[str(user.name)]['experience']
        lvl = users[str(user.name)]['level']
        lvl_end = 5 * (lvl ** 2) + (50 * lvl) + 100

        # print Discord user, exp and current level everytime they send a message
        print(user)
        print(f"Jmmib Level: {lvl}")
        print(f"Current EXP: {experience}")
        print(f"Max EXP for level {lvl}: {lvl_end}")

        # when user level up
        if lvl_end <= experience:
            # jmm channel for level up announcement
            channel=self.client.get_channel(946705507220078672)

            # embed
            embed = discord.Embed (
                color=0xffc90d
            )
            embed.set_author(name=str(user), icon_url=user.avatar_url)
            embed.add_field (
                name = f"Congratulations {user.name}!",
                value = f"You are now **Jmmib Level {lvl}** <:level_up:921018339843797022>",
                inline=False
            )
            embed.set_thumbnail(url=f"{user.avatar_url}")
            await channel.send(embed=embed)
            #await channel.send(f"Congratulations {user.mention}! You are now **Jmmib Level {lvl}** <:level_up:921018339843797022>")

            users[str(user.name)]['level'] = lvl+1
            users[str(user.name)]['experience'] -= lvl_end

    async def to_integer(self, dt_time):
        answer = 100000000 * dt_time.year + 1000000 * dt_time.month + 10000 * dt_time.day + 100 * dt_time.hour + dt_time.minute
        return int(answer)


    # rank command
    @commands.command(help="Command for user's current level and EXP.")
    async def rank(self, ctx, *, user: discord.Member = None):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        with open('users.json','r') as f:
            users = json.load(f)

        if user is None:
            if not str(ctx.author.name) in users:
                users[str(ctx.author.name)] = {}
                users[str(ctx.author.name)]['experience'] = 0
                users[str(ctx.author.name)]['level'] = 1
                users[str(ctx.author.name)]['LastMessage'] = await self.to_integer(datetime.now())

            user = ctx.author
            lvl = int(users[str(ctx.author.name)]['level'])
            exp = int(5 * (lvl ** 2) + (50 * lvl) + 100)

            # rank embed for ctx author
            embed = discord.Embed (
                title = f"**{user.name}'s Rank**",
                color=0xffc90d
            )
            embed.set_thumbnail(url=f"{user.avatar_url}")
            embed.add_field(name="Jmmib Level:", value=f"**{users[str(user.name)]['level']}**", inline=False)
            embed.add_field(name="Goldjmmibs:", value=f"<:gold_jmmib:1008380332787122256> **{str(int(users[str(user.name)]['experience']))} / {exp}**",inline=False)
            embed.set_footer(text="Chat more to earn more goldjmmibs!")
          
            await ctx.send(embed=embed)

        else:
            if not str(user.name) in users:
                users[str(user.name)] = {}
                users[str(user.name)]['experience'] = 0
                users[str(user.name)]['level'] = 1
                users[str(user.name)]['LastMessage'] = await self.to_integer(datetime.now())

            lvl = int(users[str(user.name)]['level'])
            exp = int(5 * (lvl ** 2) + (50 * lvl) + 100)

            # rank embed if member name is mentioned
            embed = discord.Embed (
              title=f"**{user.name}'s Rank**",
              color=0xffc90d
            )
            embed.set_thumbnail(url=f"{user.avatar_url}")
            embed.add_field(name="Jmmib Level:", value=f"**{users[str(user.name)]['level']}**", inline=False)
            embed.add_field(name="Goldjmmibs:", value=f"<:gold_jmmib:1008380332787122256> **{str(int(users[str(user.name)]['experience']))} / {exp}**",inline=False)
            embed.set_footer(text="Chat more to earn more goldjmmibs!")
            
            await ctx.send(embed=embed)

        with open('users.json', 'w') as f:
            json.dump(users, f)


    #add database
    @commands.command(help="Add a new or existing user to the level system database.")
    @commands.has_permissions(administrator=True)
    async def add_database(self, ctx, *, user: discord.Member):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return
            
        with open('users.json', 'r') as f:
            users = json.load(f)
            
        if not str(user.name) in users:
            users[str(user.name)] = {}
            users[str(user.name)]['experience'] = 0
            users[str(user.name)]['level'] = 1
            users[str(user.name)]['LastMessage'] = await self.to_integer(datetime.now())
            await ctx.send(f"{user.name} added to database!")
        else:
            await ctx.send(f"{user.name} already in database!")

        with open('users.json', 'w') as f:
            json.dump(users, f)

    @add_database.error
    async def add_database_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You do not have permission to use this command!")


def setup(client):
    client.add_cog(Levels(client))

def teardown(client):
    client.remove_cog(Levels(client))