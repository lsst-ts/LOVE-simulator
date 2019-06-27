import asyncio
import os
import atdome.simulator as atdome
import emitters.simulator as emitters

if __name__ == '__main__':
    """ Runs the emitters and simulators """
    print('***** Starting Simulator *****')
    config_filepath = '/usr/src/love/config/config.json'
    sal_base_index = int(os.environ.get('SAL_BASE_INDEX', 0))
    print('Using config from: ', config_filepath)
    print('Using base SAL index: ', sal_base_index)

    loop = asyncio.get_event_loop()
    asyncio.get_event_loop().run_until_complete(asyncio.wait([
        emitters.main(loop, config_filepath, sal_base_index),
        atdome.main(config_filepath, sal_base_index)
    ]))
