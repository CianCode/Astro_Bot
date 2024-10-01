# ! DISCORD
import discord
from discord.ext import commands
from discord import app_commands

# ! OTHER
import os
import time
import asyncpg  # Import asyncpg for PostgreSQL connections

from colorama import Fore, Style
from dotenv import load_dotenv

# ! Load the environment variables
load_dotenv()


class Astro(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=discord.Intents.all(),
            activity=discord.Activity(type=discord.ActivityType.custom, name="Roaaahhhh"),
            help_command=None
        )
        self.cog_list = os.listdir('./cogs')
        self.database_url = os.getenv("DATABASE_URL")  # Get DATABASE_URL from environment
        self.pool = None  # Initialize connection pool


    async def setup_hook(self):
        """Set up the bot and create the PostgreSQL connection pool."""
        self.pool = await asyncpg.create_pool(self.database_url, statement_cache_size=0)  # Create the connection pool

    async def load_cogs(self):
        for folder in self.cog_list:
            if folder != "__pycache__" and folder != "utils":
                files = os.listdir(f'./cogs/{folder}')
                for file in files:
                    if file.endswith('.py'):
                        try:
                            await self.load_extension(f'cogs.{folder}.{file[:-3]}')
                            print(
                                Fore.MAGENTA + Style.BRIGHT + 'Fichier' + Fore.WHITE + Style.BRIGHT + f' {file[:-3]} ' + Fore.MAGENTA + Style.BRIGHT + 'chargé' + Style.RESET_ALL)
                        except Exception as e:
                            print(Fore.RED + Style.DIM + f'{e}' + Style.RESET_ALL)

    async def check_postgres_ping(self):
        try:
            start_time = time.time()
            # Connect to PostgreSQL database
            conn = await asyncpg.connect(self.database_url)
            await conn.execute('SELECT 1')  # Simple query to check connection
            ping_time = (time.time() - start_time) * 1000  # Convert to milliseconds
            await conn.close()  # Close the connection
            return ping_time
        except Exception as e:
            print(Fore.RED + Style.DIM + f'PostgreSQL connection error: {e}' + Style.RESET_ALL)
            return None

    async def on_ready(self):
        await self.change_presence(status=discord.Status.online,
                                   activity=discord.Activity(type=discord.ActivityType.watching, name=f"🚀 Eclipse"))
        print('-------------------------------')
        print(Fore.WHITE + Style.BRIGHT + f'{self.user.name}' + Fore.CYAN + Style.BRIGHT + ' est en ligne.' + Style.RESET_ALL)
        print('-------------------------------')

        # Get bot latency
        bot_latency = round(self.latency * 1000)
        print(Fore.CYAN + Style.BRIGHT + "Latence du bot: " + Fore.WHITE + Style.BRIGHT + f"{bot_latency} ms" + Style.RESET_ALL)

        # Get PostgreSQL ping
        postgres_ping = await self.check_postgres_ping()
        if postgres_ping is not None:
            print(Fore.CYAN + Style.BRIGHT + "Latence de PostgreSQL: " + Fore.WHITE + Style.BRIGHT + f"{round(postgres_ping)} ms" + Style.RESET_ALL)
        else:
            print(Fore.RED + Style.DIM + "Impossible de vérifier la latence de PostgreSQL." + Style.RESET_ALL)

        print('------------------------')
        await self.load_cogs()
        await self.tree.sync()


astro = Astro()

if __name__ == '__main__':
    astro.run(os.getenv('DISCORD_TOKEN'))
