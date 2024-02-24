import asyncio
from pyrogram import Client
from pyrogram.raw.functions.account import UpdateNotifySettings
from pyrogram.raw.types import InputNotifyPeer, InputPeerNotifySettings

from datetime import datetime
from time import sleep

from getpass import getpass
from json import load

api_id = int(getpass(prompt="ID: "))
api_hash = getpass(prompt="HASH: ")

vart: int

async def main(days: int = 660):
    # 660 minuts in hours = 13

    with open("chats.json") as f:
        src = load(f)

    async with Client("unmute", api_id, api_hash) as app: # "unmute" this name telegram session
        for ID in src:
            await disable_notify(chat_id=ID['ID'], app=app, minutse=days)

async def disable_notify(chat_id: int, app: Client, minutse: int = 10) -> None:
    global vart
    peer = await app.resolve_peer(chat_id) # returns the data of the chat object
    vart = int(datetime.timestamp(datetime.now())+(60*minutse))

    await app.invoke(UpdateNotifySettings(
        peer=InputNotifyPeer(peer=peer),
        settings=InputPeerNotifySettings(mute_until=vart) # unix time
    ))

if __name__ == '__main__':
    print("\nStart\n")
    count_day = 0

    while True:
        now = datetime.now()

        # add one accounte every day
        count_day += 1
        
        if now.hour == 9 and now.minute == 5: # the time at which the trigger will occur
            if count_day > 4: # if more than 4 days have passed
                # disable notification on two days

                asyncio.run(main(days=3300)) # 3300 it's minuts for 2 days

                while vart > int(datetime.timestamp(now)): # wait 2 days
                    sleep(60**2)
                count_day = 0 # resetting the counter
                continue
            
            asyncio.run(main())
        
            print("Disable notification...\n")

        sleep(30)
