import asyncio

import numpy as np

from poke_env import AccountConfiguration, ShowdownServerConfiguration
from poke_env.player import RandomPlayer
from teams import custom_builder

async def main():
    player = RandomPlayer(
        account_configuration=AccountConfiguration("proppabanter", "wokechud"),
        server_configuration=ShowdownServerConfiguration,
        battle_format="gen9ou", team=custom_builder, max_concurrent_battles=2
    )

    await player.ladder(5)



if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
