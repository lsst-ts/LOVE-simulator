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


async def manage_exception(exception, remote):
    """Manages exceptions raised by the remote

    Parameters
    ----------
    exception:  Raised exception
    remote:  Remote which caused the exception
    """
    print(exception)
    try:
        await remote.cmd_standby.start()
    except Exception as e:
        pass
    try:
        await remote.cmd_start.start()
    except Exception as e:
        pass
    try:
        await remote.cmd_enable.start()
    except Exception as e:
        pass
    await asyncio.sleep(10)


async def main_csc(name, index, domain):
    """Runs the ATDome simulator

    Parameters
    ----------
    csc_list: `[()]`
        The list of CSCs to run as a tuple with the CSC name and index
    """
    print("\nATDome      | **** Starting ATDome command simulator loop *****")
    print("ATDome      | - Creating remote (CSC, index): (", name, ", ", index, ")")
    r = salobj.Remote(domain=domain, name=name, index=index)
    await r.start_task
    try:
        await r.cmd_start.start(timeout=30)
        await r.cmd_enable.start(timeout=30)
        await r.evt_heartbeat.next(flush=True, timeout=5)
    except Exception as e:
        print(e)

    azimuth = 0
    shutter = "closed"

    loop_count = 0
    while True:
        try:
            loop_count += 1
            r.cmd_moveAzimuth.set(azimuth=azimuth)
            azimuth = (azimuth + 50) % 360
            if loop_count % 4 == 0.0:
                if shutter == "closed":
                    await r.cmd_openShutter.start()
                else:
                    await r.cmd_closeShutter.start()
            await r.cmd_moveAzimuth.start()
            await asyncio.sleep(10)
        except Exception as e:
            manage_exception(e, r)


async def main(csc_list, domain):
    """Runs the ATDome simulator

    Parameters
    ----------
    csc_list: `[()]`
        The list of CSCs to run as a tuple with the CSC name and index
    """
    print("\nATDome      | **** Starting ATDome command simulator loop *****")
    for csc in csc_list:
        name = csc[0]
        index = None
        asyncio.get_event_loop().create_task(main_csc(name, index, domain))
