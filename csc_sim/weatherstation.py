"""Main executable of the WeatherStation simulator."""
import asyncio
import json
from lsst.ts import weatherstation

simulator_config_path = '/home/saluser/config/config.json'

if __name__ == '__main__':
    with open(simulator_config_path) as f:
        simulator_config = json.loads(f.read())

    if 'WeatherStation' in simulator_config.keys():
        awaitables = []
        for weatherstation_config in simulator_config['WeatherStation']:
            if weatherstation_config['source'] == 'command_sim':
                salindex = None
                if 'index' in weatherstation_config:
                    salindex = weatherstation_config['index']
                print('WeatherStation csc | Launching salindex = {}'.format(salindex))
                csc = weatherstation.csc.CSC(salindex, initial_simulation_mode=True)
                awaitables.append(csc.done_task)
        asyncio.get_event_loop().run_until_complete(asyncio.wait(awaitables))
