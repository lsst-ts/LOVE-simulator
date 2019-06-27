import asyncio
import atdome.simulator as atdome
import emitters.simulator as emitters
import scriptqueue.simulator as scriptqueue
if __name__ == '__main__':
    """ Runs the emitters and simulators """
    print('***** Starting Simulator *****')
    config_filepath = '/usr/src/love/config/config.json'
    print('Using config from: ', config_filepath)

    loop = asyncio.get_event_loop()
    asyncio.get_event_loop().run_until_complete(asyncio.wait([
        emitters.main(loop, config_filepath),
        atdome.main(config_filepath),
        scriptqueue.main()
    ]))
