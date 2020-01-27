"""Main executable of the LOVE-simulator."""
import asyncio
import json
import atdome.simulator as atdome
import atmcs.simulator as atmcs
import emitters.simulator as emitters
import scriptqueue.simulator as scriptqueue
import testcsc.simulator as testCsc
import watcher.simulator as watcherCsc
import gencam.simulator as gencamCsc
from lsst.ts import salobj


def read_config(path, source=None, csc=None):
    """ Reads a given config file and returns the lists of CSCs to listen to.
    It can read the full file (by default), or read only a specific key

    Parameters
    ----------
    path: `string`
        The full path of the config file
    source: `string`
        optional source to filter, the results will only consider values with the given source
    csc: `string`
        optional CSC to filter, the results will only consider values with the given CSC

    Returns
    -------
    csc_list: `[()]`
        The list of CSCs to run as a tuple with the CSC name and index
    """
    data = json.load(open(path, 'r'))
    csc_list = []
    if csc:
        if csc in data:
            for csc_instance in data[csc]:
                if source and csc_instance['source'] == source:
                    index = None
                    if 'index' in csc_instance:
                        index = csc_instance['index']
                    csc_list.append((csc, index))
        else:
            return []
    else:
        for csc_key, csc_value in data.items():
            for csc_instance in csc_value:
                if source and csc_instance['source'] == source:
                    index = None
                    if 'index' in csc_instance:
                        index = csc_instance['index']
                    csc_list.append((csc_key, index))
    return csc_list


if __name__ == '__main__':
    """ Runs the emitters and simulators """
    print('***** Starting Simulator *****')
    path = '/usr/src/love/config/config.json'
    print('Reading config file: ', path)
    emitters_list = read_config(path, 'emitter')
    atdome_list = read_config(path, 'command_sim', 'ATDome')
    atmcs_list = read_config(path, 'command_sim', 'ATMCS')
    sq_list = read_config(path, 'command_sim', 'ScriptQueue')
    testcsc_list = read_config(path, 'command_sim', 'Test')
    watcher_list = read_config(path, 'command_sim', 'Watcher')
    gencam_list = read_config(path, 'command_sim', 'GenericCamera')

    print('List of emitters to start:', emitters_list)
    print('List of ATDomes to start:', atdome_list)
    print('List of ATMCSs to start:', atmcs_list)
    print('List of ScriptQueues to start:', sq_list)
    print('List of TestCSCs to start:', testcsc_list)
    print('List of Watchers to start:', watcher_list)
    print('List of GenericCameras to start:', gencam_list)

    domain = salobj.Domain()
    loop = asyncio.get_event_loop()
    coroutines = []
    if len(emitters_list) > 0:
        loop.create_task(emitters.main(loop, emitters_list))
    if len(atdome_list) > 0:
        loop.create_task(atdome.main(atdome_list, domain))
    if len(atmcs_list) > 0:
        loop.create_task(atmcs.main(atmcs_list, domain))
    if len(sq_list) > 0:
        for sq in sq_list:
            loop.create_task(scriptqueue.main(sq[1]))
    if len(testcsc_list) > 0:
        for testcsc in testcsc_list:
            loop.create_task(testCsc.main(testcsc[1]))
    if len(watcher_list) > 0:
        loop.create_task(watcherCsc.main(watcher_list))
    if len(gencam_list) > 0:
        loop.create_task(gencamCsc.main())

    loop.run_forever()
