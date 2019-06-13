import asyncio
from lsst.ts import salobj

import SALPY_ATDome

async def main():
    r = salobj.Remote(SALPY_ATDome, index=1)

    await r.evt_heartbeat.next(flush=True, timeout=5)


    await r.cmd_start.start(timeout=30)
    await salobj.set_summary_state(r, salobj.State.ENABLED)

    azimuth = 0

    while True:
        r.cmd_moveAzimuth.set(azimuth=azimuth)
        azimuth = (azimuth+90) % 360
        await r.cmd_moveAzimuth.start()
        asyncio.sleep(5)

if __name__ == '__main__':
    print('starting loop')
    asyncio.get_event_loop().run_until_complete(main())
