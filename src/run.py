from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError
import  os
import deepl_api
import json

f = open('src/creidentials.json')
cred = json.load(f)
cred['telegram_api'][0]['api_id']

api_id = cred['telegram_api'][0]['api_id']
api_hash = cred['telegram_api'][0]['api_hash']
username = 'dankingbest'

user_input_channel = [
    'https://t.me/nexta_live',
    'https://t.me/liganet',
    'https://t.me/SBUkr'
]

user_output_channels = ['t.me/krnbtbot', 'https://t.me/testisla']

client = TelegramClient(f'/tmp/{username}', api_id, api_hash)

deepl = deepl_api.DeepL("4654795a-3eff-8d21-1ba2-91d704ab2415")


@client.on(events.NewMessage(chats=user_input_channel))
async def my_event_handler(event):
    newMessage = event.message.message
    sender = await event.get_sender()
    user = sender.username

    translations = deepl.translate(
        source_language="RU",
        target_language="EN-US",
        texts=newMessage
    )
    text = translations[0]['text']
    msg = f'Sent from {user}: \n {text}'
    for user_output_channel in user_output_channels:
        if event.photo:
            await client.send_file(
                user_output_channel,
                event.photo,
                caption=msg
            )
        elif event.media:
            await client.send_file(
                user_output_channel,
                event.media,
                caption=msg
            )
        else:
            await client.send_message(user_output_channel, msg)

with client:
    print('client is running')
    client.run_until_disconnected()
