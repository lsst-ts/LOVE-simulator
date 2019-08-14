import asyncio
import json
from lsst.ts import scriptqueue

standardpath = '/home/saluser/repos/ts_scriptqueue/tests/data/standard/'
externalpath = '/home/saluser/repos/ts_scriptqueue/tests/data/external'

simulator_config_path = '/home/saluser/config/config.json'
with open(simulator_config_path) as f:
    simulator_config = json.loads(f.read())

if 'ScriptQueue' in simulator_config.keys():
    awaitables = []
    for scriptqueue_config in simulator_config['ScriptQueue']:
        if scriptqueue_config['source'] == 'command_sim':
            salindex = scriptqueue_config['index']
            print('ScriptQueue csc | Launching salindex = {}'.format(salindex))
            csc = scriptqueue.ScriptQueue(index=salindex,
                                          standardpath=standardpath,
                                          externalpath=externalpath)
            awaitables.append(csc.done_task)

asyncio.get_event_loop().run_until_complete(asyncio.wait(awaitables))
