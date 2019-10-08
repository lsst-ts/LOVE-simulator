"""Main executable of the ATDome simulator."""
import asyncio
import json
from lsst.ts import ATDome

simulator_config_path = '/home/saluser/config/config.json'

if __name__ == '__main__':
    with open(simulator_config_path) as f:
        simulator_config = json.loads(f.read())

    if 'ATDome' in simulator_config.keys():
        awaitables = []
        for atdome_config in simulator_config['ATDome']:
            if atdome_config['source'] == 'command_sim':
                salindex = None
                if 'index' in atdome_config:
                    salindex = atdome_config['index']
                print('ATDome csc | Launching salindex = {}'.format(salindex))
                csc = ATDome.ATDomeCsc(initial_simulation_mode=True)
                awaitables.append(csc.done_task)
        asyncio.get_event_loop().run_until_complete(asyncio.wait(awaitables))
