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
