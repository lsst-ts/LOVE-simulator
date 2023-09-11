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
from lsst.ts.idl.enums.ScriptQueue import Location


async def main(index):
    print(
        "ScriptQueue | - Creating remote (CSC, index): (ScriptQueue", ", ", index, ")"
    )
    domain = salobj.Domain()
    r = salobj.Remote(domain=domain, name="ScriptQueue", index=index)
    await r.start_task
    timeout = 30

    await salobj.set_summary_state(
        remote=r, state=salobj.State.ENABLED, timeout=timeout
    )
