# This file is part of LOVE-simulator.
#
# Copyright (c) 2023 Inria Chile.
#
# Developed by Inria Chile.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or at
# your option any later version.
#
# This program is distributed in the hope that it will be useful,but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.


import asyncio
from lsst.ts import salobj


async def main_csc(name, index, domain):
    """Runs the WeatherStation simulator

    Parameters
    ----------
    csc_list: `[()]`
        The list of CSCs to run as a tuple with the CSC name and index
    """
    print(
        "\nWeatherStation      | **** Starting WeatherStation command simulator loop *****"
    )
    print(
        "WeatherStation      | - Creating remote (CSC, index): (",
        name,
        ", ",
        index,
        ")",
    )
    r = salobj.Remote(domain=domain, name=name, index=index)
    await r.start_task
    evt = await r.evt_summaryState.aget()
    state = salobj.State(evt.summaryState)
    if state == salobj.State.STANDBY:
        await r.cmd_start.start(timeout=30)
        await r.cmd_enable.start(timeout=30)
    await r.evt_heartbeat.next(flush=True)


async def main(csc_list, domain):
    """Runs the WeatherStation simulator

    Parameters
    ----------
    csc_list: `[()]`
        The list of CSCs to run as a tuple with the CSC name and index
    """
    print(
        "\nWeatherStation      | **** Starting WeatherStation command simulator loop *****"
    )
    for csc in csc_list:
        name = csc[0]
        index = csc[1]
        asyncio.get_event_loop().create_task(main_csc(name, index, domain))
