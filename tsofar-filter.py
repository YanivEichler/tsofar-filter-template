import logging
import asyncio
from telegram import Bot
from telethon import TelegramClient, events

# Settings

### Replace with your details ###
API_ID = 0
API_HASH = ''
BOT_TOKEN = ''
PHONE = ''
CHANNEL = '@tzevaadomm'
heads_up_word = 'מבזק פיקוד העורף'

### Replace with relevant Chat IDs ###
GROUPCHAT_ID = 0
BOT_CHAT_ID = 0
DEBUG_CHAT_ID = 0

### Insert locations ###
emergency_word = ''               # insert you home location here
critical_words = []               # insert critical areas
nearby_words = []                 # insert nearby areas
area_of_interest_words = []       # insert any other locations you wish to be notified about
heads_up_words = []               # insert critical areas for heads up



# Code

### Logging ###
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='output.log'
)


### Set up client & bot ###
client = TelegramClient('session_name', API_ID, API_HASH)
bot = Bot(BOT_TOKEN)


### Handler ###
@client.on(events.NewMessage(chats=(CHANNEL, DEBUG_CHAT_ID)))
async def handler(event):
    message_content = event.message.message
    if event.chat.id != DEBUG_CHAT_ID:
        if emergency_word in message_content:
            await bot.send_message(chat_id=GROUPCHAT_ID,
                                       text=f'!!!EMERGENCY ALERT!!!\nTsofar triggered with keywords: {emergency_word}')
        detected_heads_up_words = [keyword for keyword in heads_up_words if (keyword in message_content)]
        if (heads_up_word in message_content) and detected_heads_up_words:
            await bot.send_message(chat_id=GROUPCHAT_ID,
                                   text=f'!!!HEADS UP ALERT!!!\nTsofar triggered with keywords: {detected_heads_up_words}')
        detected_critical_words = [keyword for keyword in critical_words if (keyword in message_content)]
        if detected_critical_words:
            await bot.send_message(chat_id=GROUPCHAT_ID,
                                       text=f'!CRITICAL ALERT!\nTsofar triggered with keywords: {detected_critical_words}')
        detected_nearby_words = [keyword for keyword in nearby_words if (keyword in message_content)]
        if detected_nearby_words:
            await bot.send_message(chat_id=GROUPCHAT_ID,
                                       text=f'Nearby Alert\nTsofar triggered with keywords: {detected_nearby_words}')
        detected_aoi_words = [keyword for keyword in area_of_interest_words if (keyword in message_content)]
        if detected_aoi_words:
            await bot.send_message(chat_id=GROUPCHAT_ID,
                                       text=f'Area of Interest Alert\nTsofar triggered with keywords: {detected_aoi_words}')
        return
    else:
        await bot.send_message(chat_id=GROUPCHAT_ID, text=f'ECHO:\n{message_content}')
        return



### Code used to retrieve Chat IDs ###
#@client.on(events.NewMessage())
#async def handler(event):
#    # Print the chat ID when a message is received
#    print(f'Chat ID: {event.chat.id}')


# main
async def main():
    await client.start(phone=PHONE)
    print("Listening for messages...")
    await client.run_until_disconnected()


# loop
if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(main())