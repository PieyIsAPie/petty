import discord
import os
import requests
import logging

logging.basicConfig(level=logging.INFO)

SCRIPTDIR = os.path.dirname(os.path.realpath(__file__))
bot = discord.Bot(intents=discord.Intents.all())

class CatView(discord.ui.View):
    @discord.ui.button(label="Get another kitty! :3", style=discord.ButtonStyle.primary)
    async def button_callback(self, button, interaction):
        try:
            response = requests.get("https://api.thecatapi.com/v1/images/search")
            data = response.json()
            image_url = data[0]['url']
            await interaction.response.edit_message(content=image_url, view=self)
        except Exception as e:
            await interaction.response.send_message("Failed to fetch a kitty image!", ephemeral=True)
            logging.error(f"Error fetching kitty image: {e}")

class DuckView(discord.ui.View):
    @discord.ui.button(label="Get another ducky! :duck:", style=discord.ButtonStyle.primary)
    async def button_callback(self, button, interaction):
        try:
            response = requests.get("https://random-d.uk/api/v1/random")
            data = response.json()
            image_url = data['url']
            await interaction.response.edit_message(content=image_url, view=self)
        except Exception as e:
            await interaction.response.send_message("Failed to fetch a ducky image!", ephemeral=True)
            logging.error(f"Error fetching ducky image: {e}")

class DogView(discord.ui.View):
    @discord.ui.button(label="Get another doggie! :D", style=discord.ButtonStyle.primary)
    async def button_callback(self, button, interaction):
        try:
            response = requests.get("https://dog.ceo/api/breeds/image/random")
            data = response.json()
            image_url = data['message']
            await interaction.response.edit_message(content=image_url, view=self)
        except Exception as e:
            await interaction.response.send_message("Failed to fetch a doggie image!", ephemeral=True)
            logging.error(f"Error fetching doggie image: {e}")

@bot.slash_command(name="kitty", description="ooo a kitty! I LOVE KITTY! :3")
async def kitty(ctx):
    try:
        response = requests.get("https://api.thecatapi.com/v1/images/search")
        data = response.json()
        image_url = data[0]['url']
        view = CatView()
        await ctx.respond(image_url, view=view)
    except Exception as e:
        await ctx.respond("Failed to fetch a kitty image!")
        logging.error(f"Error fetching kitty image: {e}")

@bot.slash_command(name="ducky", description="DUCK DUCK I LOVE DUCKS ASADSDSADASDSADAJAV")
async def ducky(ctx):
    try:
        url = "https://random-d.uk/api/v1/random"
        response = requests.get(url)
        data = response.json()
        image_url = data['url']
        view = DuckView()
        await ctx.respond(image_url, view=view)
    except Exception as e:
        await ctx.respond("Failed to fetch a ducky image!")
        logging.error(f"Error fetching ducky image: {e}")

@bot.slash_command(name="doggie", description="I LOVE DOGS!!!")
async def doggy(ctx):
    try:
        url = "https://dog.ceo/api/breeds/image/random"
        response = requests.get(url)
        data = response.json()
        image_url = data['message']
        view = DogView()
        await ctx.respond(image_url, view=view)
    except Exception as e:
        await ctx.respond("Failed to fetch a doggie image!")
        logging.error(f"Error fetching doggie image: {e}")

@bot.event
async def on_message(message):
    # Ignore messages sent by the bot
    if message.author == bot.user:
        return

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
