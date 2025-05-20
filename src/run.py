from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError
import  os
import deepl_api
import json


with open('src/creidentials.json') as f:
    cred = json.load(f)

api_id = cred['telegram_api'][0]['api_id']
api_hash = cred['telegram_api'][0]['api_hash']
username = ''

user_input_channel = [
    'https://t.me/znua_live',
    'https://t.me/ukraina_novosti',
    'https://t.me/truexanewsua',
    'https://t.me/grey_zone',
    'https://t.me/rian_ru',
]

pro_ru = ['grey_zone', 'rian_ru']
pro_ua = [
    'znua_live',
    'ukraina_novosti',
    'truexanewsua'
]

user_output_channels = [
    'https://t.me/krntrbsltbt'
]

client = TelegramClient(None, api_id, api_hash)

deepl = deepl_api.DeepL("")


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

        flag = ''
        if user in pro_ru:
            flag = '🇷🇺'
        elif user in pro_ua:
            flag = '🇺🇦'
        if flag:
            msg = 'Pro' + flag + ' ' + msg

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
