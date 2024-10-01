# ! DISCORD
import discord
from discord.ext import commands
from discord import app_commands

class Setup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="set_channel", description="Set up the channel.")
    @app_commands.describe(type_channel='Type of value to chose from')
    @app_commands.choices(type_channel=[
        discord.app_commands.Choice(name="Facts", value=1),
        discord.app_commands.Choice(name="Daily Question", value=2)
    ])
    async def set_channel(self, interaction: discord.Interaction, channel: discord.TextChannel, type_channel: discord.app_commands.Choice[int]):
        embed_success = discord.Embed(title="Success", description=f"{channel.mention} is now the channel for {type_channel.name}.", color=discord.Color.green())
        embed_error = discord.Embed(title="Error", description="The channel must be a text channel.", color=discord.Color.red())

        if channel.type == discord.ChannelType.text:
            # Insert into the database using the connection pool
            async with self.bot.pool.acquire() as conn:
                if type_channel.value == 1:
                    await conn.execute("INSERT INTO setup (guild_id, facts_channel_id) VALUES ($1, $2) ON CONFLICT (guild_id) DO UPDATE SET facts_channel_id = $2",
                                       interaction.guild.id, channel.id)
                elif type_channel.value == 2:
                    await conn.execute("INSERT INTO setup (guild_id, daily_channel_id) VALUES ($1, $2) ON CONFLICT (guild_id) DO UPDATE SET daily_channel_id = $2",
                                       interaction.guild.id, channel.id)

            await interaction.response.send_message(embed=embed_success)
        else:
            await interaction.response.send_message(embed=embed_error)


    @app_commands.command(name="set_frequency", description="Set up the frequency.")
    @app_commands.describe(type_channel='Type of value to chose from')
    @app_commands.choices(type_channel=[
        discord.app_commands.Choice(name="Facts", value=1),
        discord.app_commands.Choice(name="Daily Question", value=2)
    ])
    async def set_frequency(self, interaction: discord.Interaction, frequency: int, type_channel: discord.app_commands.Choice[int]):
        embed_success = discord.Embed(title="Success", description=f"{frequency} hours is now the frequency for {type_channel.name}.", color=discord.Color.green())
        embed_error = discord.Embed(title="Error", description="The frequency must be a positive integer.", color=discord.Color.red())

        if frequency > 0:
            # Insert or update the frequency in the database using the connection pool
            async with self.bot.pool.acquire() as conn:
                if type_channel.value == 1:
                    await conn.execute("INSERT INTO setup (guild_id, facts_frequency) VALUES ($1, $2) ON CONFLICT (guild_id) DO UPDATE SET facts_frequency = $2",
                                       interaction.guild.id, frequency)
                elif type_channel.value == 2:
                    await conn.execute("INSERT INTO setup (guild_id, daily_frequency) VALUES ($1, $2) ON CONFLICT (guild_id) DO UPDATE SET daily_frequency = $2",
                                       interaction.guild.id, frequency)

            await interaction.response.send_message(embed=embed_success)
        else:
            await interaction.response.send_message(embed=embed_error)


async def setup(bot):
    await bot.add_cog(Setup(bot))
