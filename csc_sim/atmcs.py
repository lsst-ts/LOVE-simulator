"""Main executable of the ATMCS simulator."""
import asyncio
import json
from lsst.ts import ATMCSSimulator

simulator_config_path = '/home/saluser/config/config.json'

if __name__ == '__main__':
    with open(simulator_config_path) as f:
        simulator_config = json.loads(f.read())

    if 'ATMCS' in simulator_config.keys():
        awaitables = []
        for atmcs_config in simulator_config['ATMCS']:
            if atmcs_config['source'] == 'command_sim':
                salindex = None
                print('ATMCS csc | Launching salindex = {}'.format(salindex))
                csc = ATMCSSimulator.ATMCSCsc()
                awaitables.append(csc.done_task)
                break
        asyncio.get_event_loop().run_until_complete(asyncio.wait(awaitables))
