import asyncio
import json
import threading
from lsst.ts import salobj
from .emitter import emit_forever
from .event_emitter import emit_forever as emit_event_forever


def add_controller_in_thread(csc_name, loop, index):
    asyncio.set_event_loop(loop)
    controller = salobj.Controller(csc_name, index)
    launch_emitters_forever(loop, controller)


def launch_emitters_forever(loop, controller):
    """ Launches an emitter that fills the data to be read later in the salobj remote

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


def read_emitters_from_config(path):
    """ Reads a given config file and returns the list of CSCs to run

    Parameters
    ----------
    path: `string`
        The full path of the config file

    Returns
    -------
    csc_list: `[()]`
        The list of CSCs to run as a tuple with the CSC name and index
    """
    print('Emitters | Reading config file: ', path)
    data = json.load(open(path, 'r'))
    csc_list = []
    for csc_key, csc_value in data.items():
        for csc_instance in csc_value:
            if csc_instance['source'] == 'emitter':
                csc_list.append((csc_key, csc_instance['index']))
    return csc_list


async def main(loop, path):
    """ Runs the emitters in a given loop

    Parameters
    ----------
    loop: `EventLoop`
        The Event loop where the simulator will be executed
    path: `string`
        The full path of the config file
    """

    print('\nEmitters | *** Starting Emitters Loop ***')
    csc_list = read_emitters_from_config(path)
    print('Emitters | List of emitters to start:', csc_list)
    print('\nEmitters | Launching emitters:')
    for i in range(len(csc_list)):
        csc_params = csc_list[i]
        csc_name = csc_params[0]
        index = 0
        if len(csc_params) > 1:
            [csc_name, index] = csc_params
        index = int(index)
        print('Emitters | - Launching (CSC, index): (', csc_name, ', ', index, ')')
        t = threading.Thread(target=add_controller_in_thread, args=[csc_name, loop, index])
        t.start()
