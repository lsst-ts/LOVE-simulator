import asyncio
import json
import atdome.simulator as atdome
import emitters.simulator as emitters
import scriptqueue.simulator as scriptqueue


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
                    csc_list.append((csc, csc_instance['index']))
        else:
            return []
    else:
        for csc_key, csc_value in data.items():
            for csc_instance in csc_value:
                if source and csc_instance['source'] == source:
                    csc_list.append((csc_key, csc_instance['index']))
    return csc_list


if __name__ == '__main__':
    """ Runs the emitters and simulators """
    print('***** Starting Simulator *****')
    path = '/usr/src/love/config/config.json'
    print('Reading config file: ', path)
    emitters_list = read_config(path, 'emitter')
    atdome_list = read_config(path, 'command_sim', 'ATDome')
    print('AATOMDE LIST:', atdome_list)
    sq_list = read_config(path, 'command_sim', 'ScriptQueue')
    print('List of emitters to start:', emitters_list)
    print('List of ATDomes to start:', atdome_list)
    print('List of ScriptQueues to start:', sq_list)

    loop = asyncio.get_event_loop()
    coroutines = []
    if len(emitters_list) > 0:
        loop.create_task(emitters.main(loop, emitters_list))
    if len(atdome_list) > 0:
        loop.create_task(atdome.main(atdome_list))
    if len(sq_list) > 0:
        for sq in sq_list:
            loop.create_task(scriptqueue.main(sq[1]))

    loop.run_forever()
