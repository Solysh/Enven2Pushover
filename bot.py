import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from pushover import send_pushover_notification

# Load environment variables
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Global variable to store the last embed
last_embed = None

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    global last_embed

    if message.author == bot.user:
        return

    if message.embeds:
        last_embed = message.embeds[0].to_dict()
        # Send embed content to Pushover
        formatted_message = format_pushover_message(message.embeds[0])
        send_pushover_notification(formatted_message)

    await bot.process_commands(message)

def format_pushover_message(embed):
    asin_value = None # Variable to store the ASIN value if found

    # Function to strip strikethrough text represented in Markdown
    def strip_strikethrough(text):
        while '~~' in text:
            start = text.find('~~')
            end = text.find('~~', start + 2)
            if end != -1:
                text = text[:start] + text[end+2:]
            else:  # Handle case where closing ~~ is missing
                text = text[:start] + text[start+2:]
        return text
    
    for field in embed.fields:
        if field.name == "ASIN":
            asin_value = field.value  # Store the Amazon ASIN
            break # Exit loop once ASIN is found
    
    # Title
    message = f"<b>{embed.title}</b>\n\n" if embed.title else "No Title\n"

    # Description
    message += f"{embed.description}\n\n" if embed.description else f"http://www.amazon.com/gp/product/{asin_value}\n\n"

    # Fields
    for field in embed.fields:
        field_value = field.value.replace("||", "")
        field_value = strip_strikethrough(field_value)
        message += f"<b>{field.name}:</b> {field_value}\n"

    # Footer and Author (Optional)
    if embed.footer:
        message += f"\n<b>Footer:</b> {embed.footer.text}"
    if embed.author:
        message += f"\nAuthor: {embed.author.name}"

    # Include the embed image URL if available
    if embed.image:
        message += f"\nImage: {embed.image.url}"

    return message


@bot.command(name='showlast')
async def show_last_embed(ctx):
    global last_embed
    if last_embed:
        await ctx.send(embed=discord.Embed.from_dict(last_embed))
        # Optionally, also send this to Pushover
        send_pushover_notification(format_pushover_message(discord.Embed.from_dict(last_embed)))
    else:
        await ctx.send("No embed stored previously.")

@bot.command(name='readmessage')
async def read_specific_message(ctx, channel_id: int, message_id: int):
    channel = bot.get_channel(channel_id)
    if channel:
        try:
            message = await channel.fetch_message(message_id)
            # Send message content to Pushover
            if message.embeds:
                last_embed = message.embeds[0].to_dict()
                # Send embed content to Pushover
                await ctx.send(embed=discord.Embed.from_dict(last_embed))
                send_pushover_notification(format_pushover_message(discord.Embed.from_dict(last_embed)))
        except discord.NotFound:
            await ctx.send("Message not found.")
        except discord.Forbidden:
            await ctx.send("I don't have permission to read that message.")
        except discord.HTTPException as e:
            await ctx.send(f"An HTTP error occurred: {e}")
    else:
        await ctx.send("Channel not found.")

bot.run(DISCORD_TOKEN)