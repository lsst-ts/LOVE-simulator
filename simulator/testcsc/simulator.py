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


async def main(salindex):
    d = salobj.Domain()
    r = salobj.Remote(d, "Test", salindex)
    await r.start_task

    cmds = [
        r.cmd_enable,
        r.cmd_fault,
        r.cmd_standby,
        r.cmd_start,
    ]
    while True:
        for command in cmds:
            try:
                await command.start()
            except Exception as e:
                print("Test CSC error:", e)
            await asyncio.sleep(5)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main(1))
