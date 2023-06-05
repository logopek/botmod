import pyrogram
import asyncio

class Module:
    name = "tag all v2"
    short_name = "tgall2"
    activate = "tgall2"
    description = """Tag everyone from chat"""

    @classmethod
    async def act(cls, client: pyrogram.Client, message: pyrogram.types.Message, *args, **kwargs):
        all_users = client.get_chat_members(message.chat.id)
        w = ""
        x = 0
        y = message.chat.id
        await message.delete()
        async for user in all_users:
            if x >= 5:
                await client.send_message(y, w)
await asyncio.sleep(0.7)
                w = ""
                x = 0
            w += '@' + user.user.username + '\n'
            x += 1
        await client.send_message(y, w)

    @property
    async def help(self):
        return self.description
