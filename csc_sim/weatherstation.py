# This file is part of LOVE-simulator.
#
# Copyright (c) 2023 Inria Chile.
#
# Developed by Inria Chile.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or at
# your option any later version.
#
# This program is distributed in the hope that it will be useful,but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.


"""Main executable of the WeatherStation simulator."""
import asyncio
import json
from lsst.ts import weatherstation

simulator_config_path = '/home/saluser/config/config.json'

async def main():
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
                csc = weatherstation.csc.CSC(salindex, simulation_mode=True)
                awaitables.append(csc.done_task)
        await asyncio.wait(awaitables)

asyncio.run(main())