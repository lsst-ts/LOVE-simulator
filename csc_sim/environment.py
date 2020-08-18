"""Main executable of the Environment simulator."""
import asyncio
import json
from lsst.ts import environment

simulator_config_path = '/home/saluser/config/config.json'

if __name__ == '__main__':
    with open(simulator_config_path) as f:
        simulator_config = json.loads(f.read())

    if 'Environment' in simulator_config.keys():
        awaitables = []
        for environment_config in simulator_config['Environment']:
            if environment_config['source'] == 'command_sim':
                salindex = None
                if 'index' in environment_config:
                    salindex = environment_config['index']
                print('Environment csc | Launching salindex = {}'.format(salindex))
                csc = environment.csc.CSC(salindex, initial_simulation_mode=True)
                awaitables.append(csc.done_task)
        asyncio.get_event_loop().run_until_complete(asyncio.wait(awaitables))
