import os
import discord
from discord import app_commands
import requests
from discord.ext import commands

# Load your tokens from environment variables or replace with your actual tokens
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN', 'YOUR_DISCORD_BOT_TOKEN')
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY', 'YOUR_OPENWEATHERMAP_API_KEY')

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

guild_id = None  # Optionally set your guild/server ID for faster command registration

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    try:
        synced = await bot.tree.sync(guild=discord.Object(id=guild_id)) if guild_id else await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(f'Error syncing commands: {e}')

@bot.tree.command(name="weather", description="Get weather for a city")
@app_commands.describe(city="City name to get weather for")
async def weather(interaction: discord.Interaction, city: str):
    await interaction.response.defer()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=en"
    resp = requests.get(url)
    if resp.status_code != 200:
        await interaction.followup.send(f"Could not get weather for '{city}'. Please check the city name.")
        return
    data = resp.json()
    weather_desc = data['weather'][0]['description'].capitalize()
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    country = data['sys']['country']
    embed = discord.Embed(title=f"Weather in {city.title()}, {country}", color=0x1e90ff)
    embed.add_field(name="Description", value=weather_desc, inline=False)
    embed.add_field(name="Temperature", value=f"{temp}°C (feels like {feels_like}°C)", inline=False)
    embed.add_field(name="Humidity", value=f"{humidity}%", inline=True)
    embed.add_field(name="Wind Speed", value=f"{wind_speed} m/s", inline=True)
    await interaction.followup.send(embed=embed)

if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)
