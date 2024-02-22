from pyrogram import Client, filters
from pyrogram.types import Message
import logging
from config import Config

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AutoCaption(Client):
    
    def __init__(self):
        super().__init__(
            session_name="Captioner",
            bot_token=Config.BOT_TOKEN,
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            workers=20,
            plugins=dict(
                root="plugins"
            )
        )

    async def on_message(self, message: Message):
        # Your message handling logic here
        pass

if __name__ == "__main__":
    AutoCaption().run()
