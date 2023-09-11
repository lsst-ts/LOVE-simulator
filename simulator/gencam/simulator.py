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


async def main():
    while True:
        try:
            print("Starting GenericCamera Simulator")
            r = salobj.Remote(salobj.Domain(), "GenericCamera", index=1)
            await r.start_task
            await salobj.set_summary_state(r, salobj.State.ENABLED)
            await r.cmd_startLiveView.set_start(expTime=0.5)
            break
        except Exception as e:
            print("Error starting GenericCamera Simulator. Retrying in 1 second")
            await asyncio.sleep(1)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
