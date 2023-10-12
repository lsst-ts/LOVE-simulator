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
import random


async def main(index):
    """main changes in the ATSpectrograph CSC
    Parameters
    ----------
    index: int
        CSC index
    """
    print("LATISS - Creating remote")
    d = salobj.Domain()
    r = salobj.Remote(d, "ATSpectrograph", index)
    await r.start_task
    fw_options = [0, 1, 2, 2, 2, 2, 2, 3]
    gw_options = [0, 1, 2, 2, 2, 2, 2, 3]
    try:
        await r.cmd_start.start(timeout=30)
        await salobj.set_summary_state(r, salobj.State.ENABLED)
    except Exception as e:
        print(e)

    while True:
        print("True")
        try:
            # change filter
            fw_choice = random.choice(fw_options)
            r.cmd_changeFilter.set(filter=fw_choice, name="Filter " + str(fw_choice))
            await r.cmd_changeFilter.start()
            # change disperser
            gw_choice = random.choice(gw_options)
            r.cmd_changeDisperser.set(
                disperser=gw_choice, name="Grating " + str(gw_choice)
            )
            await r.cmd_changeDisperser.start()
            # move linear stage
            r.cmd_moveLinearStage.set(distanceFromHome=int(random.random() * 73))
            a = await r.cmd_moveLinearStage.start()
            print(a)
        except Exception as e:
            print(e)

        await asyncio.sleep(5)
