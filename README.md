# Discord Weather Bot Setup Instructions

1. **Install dependencies:**
   Open a terminal in the `discord_weather_bot` folder and run:
   ```powershell
   pip install -r requirements.txt
   ```

2. **Get API keys:**
   - **Discord Bot Token:** Create a bot at https://discord.com/developers/applications and copy the token.
   - **OpenWeatherMap API Key:** Sign up at https://openweathermap.org/api and get your API key.

3. **Set your tokens:**
   - You can set the `DISCORD_TOKEN` and `WEATHER_API_KEY` as environment variables, or edit `bot.py` and replace `'YOUR_DISCORD_BOT_TOKEN'` and `'YOUR_OPENWEATHERMAP_API_KEY'` with your actual keys.

4. **Run the bot:**
   ```powershell
   python bot.py
   ```

5. **Invite the bot to your server:**
   - Use the OAuth2 URL Generator in the Discord Developer Portal. Add the `applications.commands` and `bot` scopes, and give it the `Send Messages` permission.

6. **Use the command:**
   - In your Discord server, type `/weather cityname` (e.g., `/weather London`).

---

**Note:**
- The first time you run the bot, it may take a few minutes for the slash command to appear in your server.
- For faster command registration, set your server's guild ID in `bot.py` (see the `guild_id` variable).
