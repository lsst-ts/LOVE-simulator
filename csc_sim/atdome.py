"""Main executable of the ATDome simulator."""
import asyncio
import json
from lsst.ts import ATDome

simulator_config_path = '/home/saluser/config/config.json'

async def main():
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
                csc = ATDome.ATDomeCsc(simulation_mode=True)
                awaitables.append(csc.done_task)
        await asyncio.wait(awaitables)
        
asyncio.run(main())