# plugins/search.py
from pyrogram import Client, filters
import re
from TechVJ.bot import TechVJBot
from info import CHANNELS  # If needed for search

app = TechVJBot

# Message handler with filter for @ and links
@app.on_message(filters.text & ~filters.command)
async def handle_message(client, message):
    query = message.text

    # Check for usernames (@) or links
    if re.search(r'@\w+|http[s]?://\S+|www\.\S+', query):
        return  # Ignore the message if it contains @ or a link

    # Existing logic (replace with your actual handler logic)
    search_message = await message.reply(f"Searching For\n{query}")
    results = await search_in_index(query)  # Replace with your search function
    if results:
        await search_message.edit_text(f"Found results:\n{results}")
    else:
        await search_message.edit_text("No results found.")

async def search_in_index(query: str) -> list:
    # Replace with your actual search logic
    return []
