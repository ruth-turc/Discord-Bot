import discord

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        # prints user message in the terminal 
        print(f'Message from {message.author}: {message.content}')

        username = str(message.author).split("#")[0]
        user_message = str(message.content)
        channel = str(message.channel.name)

        if message.author == client.user:
            return
        
        if "hello there" in user_message.lower():
            await message.channel.send(f'You are a bold one, roger roger')
            return
        
        if "clanker" in user_message.lower():
            await message.channel.send(f'Watch your language, roger roger')
            return
        
        if "general grevious" in user_message.lower():
            await message.channel.send(f'I LOVE THAT GUY!!! :D')
            await message.channel.send(f'roger roger')
            return
        
        if "roger roger" in user_message.lower():
            await message.channel.send(f'roger roger')
            return
        


intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run('')