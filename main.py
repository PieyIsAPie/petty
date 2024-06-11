import discord
import os
import requests

bot = discord.Bot(intents=discord.Intents.all())

SCRIPTDIR = os.path.dirname(os.path.realpath(__file__))

#Who used the weld tool on my fuckin cat?
@bot.slash_command(guild_ids=[790642397373005855, 1085739941658628147], name="kitty", description="ooo a kitty! I LOVE KITTY!")
async def kitty(ctx):
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    data = response.json()
    image_url = data[0]['url']
    await ctx.respond(image_url)

@bot.slash_command(guild_ids=[790642397373005855, 1085739941658628147], name="ducky", description="DUCK DUCK I LOVE DUCKS ASADSDSADASDSADAJAV")
async def ducky(ctx):
    response = requests.get("https://random-d.uk/api/v1/random")
    data = response.json()
    image_url = data['url']
    await ctx.respond(image_url)

@bot.slash_command(guild_ids=[790642397373005855, 1085739941658628147], name="doggie", description="I LOVE DOGS!!!")
async def doggy(ctx):
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    data = response.json()
    image_url = data['message']
    await ctx.respond(image_url)

    
@bot.event
async def on_message(message):
    # Ignore messages sent by the bot
    if message.author == bot.user:
        return

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the ducks"))
    #bot.process_application_commands()

bot.run(open("token.txt", "r").read())