import discord
from discord.ext import commands

import os
from dotenv import load_dotenv
load_dotenv()

class Bot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(command_prefix = "$", intents = discord.Intents.all())

    async def setup_hook(self):
        #await self.load_extension("cog.")
        await self.tree.sync()

    async def on_ready(self):
        print(f"{self.user.display_name} # {self.user.discriminator} is online")

TOKEN = os.getenv("TOKEN")
bot = Bot()
bot.run(TOKEN)