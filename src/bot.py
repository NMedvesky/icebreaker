import datetime
import os
import platform
import time
from typing import Literal

import discord
from colorama import Back, Fore, Style
from discord import Interaction
from discord.ext import commands

TOKEN: str = os.environ["ICEBREAKER_TOKEN"]
ADMIN_IDS: list[int] = []


def prfx() -> str:
    return (
        Back.BLACK
        + Fore.GREEN
        + time.strftime("%H:%M:%S UTC", time.gmtime())
        + Back.RESET
        + Fore.WHITE
        + Style.BRIGHT
    )


class Client(commands.Bot):
    def __init__(self) -> None:
        super().__init__(
            command_prefix="!*!",  # Setting command_prefix to !*! so it is unlikly to be triggered
            intents=discord.Intents().all(),
        )

        self.my_cogs = ["question_commands", "trivia_commands"]

    async def setup_hook(self):
        for ext in self.my_cogs:
            await self.load_extension(ext)
            print(f"{prfx()} Loaded {Fore.YELLOW}{ext} Extension")

    async def on_ready(self):
        await client.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name="the night sky",
                url="https://youtu.be/dQw4w9WgXcQ",
            )
        )

        print(f"{prfx()} Logged in as {Fore.YELLOW}{client.user.name}")
        print(f"{prfx()} Bot ID {Fore.YELLOW}{client.user.id}")
        print(f"{prfx()} Discord Version {Fore.YELLOW}{discord.__version__}")
        print(f"{prfx()} Python Version {Fore.YELLOW}{platform.python_version()}")

        synced = await client.tree.sync()
        print(f"{prfx()} Tree Commands Synced {Fore.YELLOW}{len(synced)} Commands")

        client.start_time = time.time()
        print(f"{prfx()} Bot Online")


client = Client()


@client.tree.command(name="ping")
async def ping_command(interaction: Interaction):
    """Checks the bot's latency in ms."""
    bot_lag = round(client.latency * 1000)
    await interaction.response.send_message(f"Pong! I'm late by {bot_lag}ms.")


@client.tree.command(name="uptime")
async def uptime_command(interaction: Interaction):
    """Checks the bot's uptime."""
    uptime = str(
        datetime.timedelta(seconds=int(round(time.time() - client.start_time)))
    )
    await interaction.response.send_message(f"Bot online for **{uptime}**")


@client.tree.command(name="reload")
async def reload_command(
    interaction: Interaction,
    cog: Literal["question_commands", "trivia_commands"],
):
    """[DEV] Reload an extension"""

    if interaction.user.id not in ADMIN_IDS:
        await interaction.response.send_message(
            "You do not have permission to run this command!", ephemeral=True
        )
        return

    await interaction.response.defer(thinking=True)

    await client.reload_extension(cog)

    print(
        f"{prfx()} Reloaded {Fore.YELLOW}{cog} Extension {Fore.WHITE}by {Fore.MAGENTA}{interaction.user}"
    )
    await interaction.followup.send(f"Reloaded **{cog}** Extension")


client.run(TOKEN)
