import asyncio
import threading
from lsst.ts import salobj
from .emitter import emit_forever
from .event_emitter import emit_forever as emit_event_forever


def add_controller_in_thread(csc_name, loop, index):
    asyncio.set_event_loop(loop)
    controller = create_controller(csc_name, index)
    launch_emitters_forever(loop, controller)


def create_controller(csc_name, index):
    print("make controller", csc_name)
    controller = salobj.Controller(csc_name, index)

    return controller


def launch_emitters_forever(loop, controller):
    """
        Launches an emitter that fills the data to be read
        later in the salobj remote
    """
    freq = 0.5
    t1 = threading.Thread(target=emit_forever, args=[controller, freq, loop])
    t1.start()
    t2 = threading.Thread(target=emit_event_forever, args=[controller, freq, loop])
    t2.start()


async def main(loop):
    print('--main--')
    csc_list = [line.rstrip('\n') for line in open('/usr/src/love/sallibs.config')]
    for i in range(len(csc_list)):
        csc_params = csc_list[i].split(' ')
        csc_name = csc_params[0]
        index = 0
        print(csc_params)
        if len(csc_params) > 1:
            [csc_name, index] = csc_params
        index = int(index)
        t = threading.Thread(target=add_controller_in_thread, args=[csc_name, loop, index])
        t.start()
