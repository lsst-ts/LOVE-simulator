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
import threading
from lsst.ts import salobj
from .emitter import emit_forever
from .event_emitter import emit_forever as emit_event_forever


def add_controller_in_thread(csc_name, loop, index):
    asyncio.set_event_loop(loop)
    controller = salobj.Controller(csc_name, index)
    launch_emitters_forever(loop, controller)


def launch_emitters_forever(loop, controller):
    """Launches an emitter that fills the data to be read later in the salobj remote

    Parameters
    ----------
    loop: `EventLoop`
        The Event loop where the simulator will be executed
    controller: `Controller`
        The controller of the emitter
    """
    freq = 0.5
    t1 = threading.Thread(target=emit_forever, args=[controller, freq, loop])
    t1.start()
    t2 = threading.Thread(target=emit_event_forever, args=[controller, freq, loop])
    t2.start()


async def main(loop, csc_list):
    """Runs the emitters in a given loop

    Parameters
    ----------
    loop: `EventLoop`
        The Event loop where the simulator will be executed
    csc_list: `[()]`
        The list of CSCs to run as a tuple with the CSC name and index
    """

    print("\nEmitters    | *** Starting Emitters Loop ***")
    print("\nEmitters    | Launching emitters:")
    for i in range(len(csc_list)):
        csc_params = csc_list[i]
        csc_name = csc_params[0]
        index = 0
        if len(csc_params) > 1:
            [csc_name, index] = csc_params
        index = int(index)
        print("Emitters | - Launching (CSC, index): (", csc_name, ", ", index, ")")
        t = threading.Thread(
            target=add_controller_in_thread, args=[csc_name, loop, index]
        )
        t.start()
