from pyrogram import Client

async def ret_chatdata(api_id: int, api_hash: str)-> list[dict]:
    """
    Example:
        result = asyncio.run(ret_chatdata(api_id=api_id, api_hash=api_hash))
    """
    chats = []
    async with Client("unmute", api_id, api_hash) as app: # "unmute" this name telegram session
        async for dialog in app.get_dialogs():
            chats.append(
                {
                    "":dialog.chat.id,
                    "name":dialog.chat.first_name or dialog.chat.title
                }
            )

    return chats