import asyncio
from lsst.ts import salobj


async def main_csc(name, index, domain):
    """ Runs the ATMCS simulator

    Parameters
    ----------
    csc_list: `[()]`
        The list of CSCs to run as a tuple with the CSC name and index
    """
    print('\nATMCS      | **** Starting ATMCS command simulator loop *****')
    print('ATMCS      | - Creating remote (CSC, index): (', name, ', ', index, ')')
    r = salobj.Remote(domain=domain, name=name, index=index)
    try:
        await r.cmd_start.start(timeout=30)
        await r.cmd_enable.start(timeout=30)
        await r.evt_heartbeat.next(flush=True, timeout=5)
    except Exception as e:
        print(e)

    azimuth = 0
    azimuthMax = 260
    elevation = 10
    elevationMax = 70
    nasmyth1RotatorAngle = 0
    nasmyth1RotatorAngleMax = 90
    nasmyth2RotatorAngle = 0
    nasmyth2RotatorAngleMax = 90
    trackingLoops = 120
    loopCount = 0
    loopCount2 = 0

    class Object(object):
        pass

    t = Object()
    t.private_sndStamp = 0
    while True:
        try:
            loopCount += 1
            if loopCount == 1:
                t = await r.cmd_startTracking.start(timeout=10)
            r.cmd_trackTarget.set(azimuth=azimuth+azimuthMax/trackingLoops*loopCount, azimuthVelocity=3,
                                    elevation=elevation+elevationMax/trackingLoops*loopCount, elevationVelocity=3,
                                    nasmyth1RotatorAngle=nasmyth1RotatorAngle+nasmyth1RotatorAngleMax/trackingLoops*loopCount, nasmyth1RotatorAngleVelocity=3,
                                    nasmyth2RotatorAngle=nasmyth2RotatorAngle+nasmyth2RotatorAngleMax/trackingLoops*loopCount, nasmyth2RotatorAngleVelocity=3,
                                    time=t.private_sndStamp, trackId=1)
            if loopCount < trackingLoops:
                t = await r.cmd_trackTarget.start(timeout=10)
                await asyncio.sleep(0.25)
            if loopCount > trackingLoops:
                loopCount2 = loopCount2 + 1
                loopCount=0
                await r.cmd_stopTracking.start(timeout=20)
                r.cmd_setInstrumentPort.set(port=(loopCount2 % 3+1))
                r.evt_m3InPosition.flush()
                await r.cmd_setInstrumentPort.start(timeout=10)
                while True:
                    data = await r.evt_m3InPosition.next(flush=False)
                    if data.inPosition:
                        break
        except Exception as e:
            print(e)
            try:
                await r.cmd_standby.start()
            except Exception as e:
                pass
            try:
                await r.cmd_start.start() 
            except Exception as e:
                pass
            try:
                await r.cmd_enable.start()
            except Exception as e:
                pass
            loopCount=0
            await asyncio.sleep(10)


async def main(csc_list, domain):
    """ Runs the ATMCS simulator

    Parameters
    ----------
    csc_list: `[()]`
        The list of CSCs to run as a tuple with the CSC name and index
    """
    print('\nATMCS      | **** Starting ATMCS command simulator loop *****')
    for csc in csc_list:
        name = csc[0]
        index = None
        if csc[1] is not None:
            index = int(csc[1])
        asyncio.get_event_loop().create_task(main_csc(name, index, domain))

if __name__ == '__main__':
    print('***** Running ATMCS command simulator as standalone *****')
    asyncio.get_event_loop().run_forever(main())
