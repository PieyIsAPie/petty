import discord
import os
import requests
import logging

logging.basicConfig(level=logging.INFO)

bot = discord.Bot(intents=discord.Intents.all())

@bot.slash_command(name="kitty", description="ooo a kitty! I LOVE KITTY!")
async def kitty(ctx):
    try:
        response = requests.get("https://api.thecatapi.com/v1/images/search")
        data = response.json()
        image_url = data[0]['url']
        await ctx.respond(image_url)
    except Exception as e:
        await ctx.respond("Failed to fetch a kitty image!")
        logging.error(f"Error fetching kitty image: {e}")

@bot.slash_command(name="ducky", description="DUCK DUCK I LOVE DUCKS ASADSDSADASDSADAJAV")
async def ducky(ctx):
    try:
        response = requests.get("https://random-d.uk/api/v1/random")
        data = response.json()
        image_url = data['url']
        await ctx.respond(image_url)
    except Exception as e:
        await ctx.respond("Failed to fetch a ducky image!")
        logging.error(f"Error fetching ducky image: {e}")

@bot.slash_command(name="doggie", description="I LOVE DOGS!!!")
async def doggy(ctx):
    try:
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        data = response.json()
        image_url = data['message']
        await ctx.respond(image_url)
    except Exception as e:
        await ctx.respond("Failed to fetch a doggie image!")
        logging.error(f"Error fetching doggie image: {e}")

@bot.event
async def on_ready():
    logging.info(f'We have logged in as {bot.user}')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the ducks"))

if __name__ == "__main__":
    try:
        logging.info("Starting the bot")
        TOKEN = os.getenv("TOKEN")
        if not TOKEN:
            raise ValueError("No token provided")
        logging.info(f"Token found: {TOKEN[:4]}...{TOKEN[-4:]}")  # Log part of the token for verification
        bot.run(TOKEN)
    except Exception as e:
        logging.error(f"Failed to start bot: {e}")
