# ! DISCORD
import discord
from discord.ext import commands
from discord import app_commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Check if the bot is online.")
    async def ping(self, interaction: discord.Interaction):
        bot_latency = round(self.bot.latency * 1000)
        postgres_latency = await self.bot.check_postgres_ping()

        # Determine emojis based on latencies
        if bot_latency < 150:
            bot_emoji = "<:goodconnection:1290420027526479892>"  # Green for good latency
        elif bot_latency < 300:
            bot_emoji = "<:idleconnection:1290420075047817328>"  # Yellow for moderate latency
        else:
            bot_emoji = "<:lowconnection:1290420111077019720>"  # Red for high latency

        if postgres_latency is not None:
            if postgres_latency < 150:
                postgres_emoji = "<:goodconnection:1290420027526479892>"
            elif postgres_latency < 300:
                postgres_emoji = "<:idleconnection:1290420075047817328>"
            else:
                postgres_emoji = "<:lowconnection:1290420111077019720>"
        else:
            postgres_emoji = "❓"  # Unknown latency if the check fails

        # Create an embed with both latencies and emojis
        embed = discord.Embed(color=discord.Color.green())
        embed.add_field(name=f"{bot_emoji} Bot Latency", value=f"{bot_latency} ms", inline=False)
        embed.add_field(name=f"{postgres_emoji}  PostgreSQL Latency", value=f"{round(postgres_latency) if postgres_latency is not None else 'N/A'} ms", inline=False)

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Ping(bot))
