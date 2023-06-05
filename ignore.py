import pyrogram


class Module:
    name = "Ignore"
    short_name = "ignore"
    activate = "ignore"
    description = """Tag everyone from chat"""

	muted_people = []
    @classmethod
    async def act(cls, client: pyrogram.Client, message: pyrogram.types.Message, *args, **kwargs):
        

    @property
    async def help(self):
        return self.description
        
    @classmethod
    async def sched(cls, client: pyrogram.Client, message: pyrogram.types.Message, *args, **kwargs):
    	if message.from_user.id in muted_people:
    		message.reply_to_message(”User are gnoring you”)