import discord
from discord.ext import commands
from discord import app_commands

class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

        try:
            guild = discord.Object(id=1467243643869069314)
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}')
        except Exception as e:
            print(f'Error syncing commands: {e}')


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
            await message.channel.send(f'Watch your language, roger roger')
            return
        
    # greets new members   
    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Welcome {member.mention} to {guild.name}, roger roger'
            await guild.system_channel.send(to_send)



intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)

GUILD_ID = discord.Object(id=1467243643869069314)

@client.tree.command(name="hello", description="Say hello", guild=GUILD_ID)
async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message("Greetings, roger roger!")


@client.tree.command(name="echo", description="Echoes what you type with a roger roger", guild=GUILD_ID)
async def echo(interaction: discord.Interaction, printer: str):
    if "clanker" in printer.lower():
        await interaction.response.send_message("HOW DARE YOU MAKE ME SAY THAT FOWL WORD, roger roger")
    else: 
        await interaction.response.send_message(printer + " roger roger")



client.run('MTQ2NzI0MDgwODIyNTgzMzI3Mg.GtDtdT.sMimh0032pOh0xLztsC_Gf7eRd28gvGeRp-94s')