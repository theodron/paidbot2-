# plugins/search.py
from pyrogram import Client, filters
import re
from TechVJ.bot import TechVJBot
from info import CHANNELS  # If needed for search

app = TechVJBot

# Command handler for /start
@app.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply("Welcome to Bhuji Bot! I'm here to help you search for movies and series. Type a movie or series name to get started (e.g., 'Jawan 2023' or 'Loki S01').")

# Message handler for text (excluding commands, ignoring @ and links)
@app.on_message(filters.text)
async def handle_message(client, message):
    query = message.text

    # Skip if the message is a command (e.g., /start)
    if query.startswith('/'):
        return

    # Ignore messages with @ or links
    if re.search(r'@\w+|http[s]?://\S+|www\.\S+', query):
        return

    # Existing search logic (replace with your actual logic)
    search_message = await message.reply(f"Searching For\n{query}")
    results = await search_in_index(query)  # Replace with your search function
    if results:
        await search_message.edit_text(f"Found results:\n{results}")
    else:
        await search_message.edit_text("No results found.")

async def search_in_index(query: str) -> list:
    # Replace with your actual search logic
    return []
