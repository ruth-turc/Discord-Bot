import discord
from discord.ext import commands

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    # How bot responds when there is a message
    async def on_message(self, message):

        username = str(message.author).split("#")[0]
        user_message = str(message.content)
        channel = str(message.channel.name)

        #stops the bot from responding to iteslf
        if message.author == client.user:
            return
        
        #if user sends message containing "Hello There," bot responds
        if "hello there" in user_message.lower():
            await message.channel.send(f'You are a bold one, roger roger')
            return
        
        # if user sends message containing "clanker," bot responds
        if "clanker" in user_message.lower():
            await message.channel.reply(f'Watch your language, roger roger')
            return
        
    # greets new members   
    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Welcome {member.mention} to {guild.name}, roger roger'
            await guild.system_channel.send(to_send)



intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run('')