# Apex Sigma: The Database Giant Discord Bot.
# Copyright (C) 2017  Lucia's Cipher
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import asyncio

from sigma.modules.games.warframe.commons.cycles.generic import send_to_channels
from sigma.modules.games.warframe.commons.parsers.invasion_parser import get_invasion_data, generate_invasion_embed


async def invasion_clockwork(ev):
    ev.bot.loop.create_task(invasion_cycler(ev))


async def invasion_cycler(ev):
    while ev.bot.is_ready():
        try:
            invasions, triggers = await get_invasion_data(ev.db)
            if invasions:
                response = await generate_invasion_embed(invasions)
                await send_to_channels(ev, response, 'WarframeInvasionChannel', triggers)
        except Exception:
            pass
        await asyncio.sleep(2)
