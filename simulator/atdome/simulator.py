import asyncio
from lsst.ts import salobj


async def main():
    domain = salobj.Domain()
    r = salobj.Remote(domain=domain, name='ATDome', index=1)

    await r.cmd_start.start(timeout=30)
    await salobj.set_summary_state(r, salobj.State.ENABLED)
    await r.evt_heartbeat.next(flush=True, timeout=5)

    azimuth = 0
    shutter = 'closed'

    loopCount = 0
    while True:
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

if __name__ == '__main__':
    print('--------starting atdome loop----')
    asyncio.get_event_loop().run_until_complete(main())
