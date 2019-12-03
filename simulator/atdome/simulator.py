import asyncio
from lsst.ts import salobj


async def main_csc(name, index, domain):
    """ Runs the ATDome simulator

    Parameters
    ----------
    csc_list: `[()]`
        The list of CSCs to run as a tuple with the CSC name and index
    """
    print('\nATDome      | **** Starting ATDome command simulator loop *****')
    print('ATDome      | - Creating remote (CSC, index): (', name, ', ', index, ')')
    r = salobj.Remote(domain=domain, name=name, index=index)
    try:
        await r.cmd_start.start(timeout=30)
        await r.cmd_enable.start(timeout=30)
        await r.evt_heartbeat.next(flush=True, timeout=5)
    except Exception as e:
        print(e)

    azimuth = 0
    shutter = 'closed'

    loopCount = 0
    while True:
        try:
            loopCount += 1
            r.cmd_moveAzimuth.set(azimuth=azimuth)
            azimuth = (azimuth+50) % 360
            if loopCount % 4 == 0.:
                if shutter == 'closed':
                    await r.cmd_openShutter.start()
                else:
                    await r.cmd_closeShutter.start()
            await r.cmd_moveAzimuth.start()
            await asyncio.sleep(10)
        except Exception as e:
            print(e)


async def main(csc_list, domain):
    """ Runs the ATDome simulator

    Parameters
    ----------
    csc_list: `[()]`
        The list of CSCs to run as a tuple with the CSC name and index
    """
    print('\nATDome      | **** Starting ATDome command simulator loop *****')
    for csc in csc_list:
        name = csc[0]
        index = None
        asyncio.get_event_loop().create_task(main_csc(name, index, domain))

if __name__ == '__main__':
    print('***** Running ATDome command simulator as standalone *****')
    asyncio.get_event_loop().run_forever(main())
