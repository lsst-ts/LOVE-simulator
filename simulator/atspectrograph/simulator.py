import asyncio
from lsst.ts import salobj
import random


async def main(index):
    """main changes in the ATSpectrograph CSC
    Parameters
    ----------
    index: int
        CSC index
    """
    print('LATISS - Creating remote')
    d = salobj.Domain()
    r = salobj.Remote(d, 'ATSpectrograph', index)
    await r.start_task
    fwOptions = [0, 1, 2, 2, 2, 2, 2, 3]
    gwOptions = [0, 1, 2, 2, 2, 2, 2, 3]
    try:
        await r.cmd_start.start(timeout=30)
        await salobj.set_summary_state(r, salobj.State.ENABLED)
    except Exception as e:
        print(e)

    while True:
        print('True')
        try:
            # change filter
            fwChoice = random.choice(fwOptions)
            r.cmd_changeFilter.set(filter=fwChoice, name='Filter ' + str(fwChoice))
            await r.cmd_changeFilter.start()
            # change disperser
            gwChoice = random.choice(gwOptions)
            r.cmd_changeDisperser.set(disperser=gwChoice, name='Grating ' + str(gwChoice))
            await r.cmd_changeDisperser.start()
            # move linear stage
            r.cmd_moveLinearStage.set(distanceFromHome=int(random.random()*73))
            a = await r.cmd_moveLinearStage.start()
            print(a)
        except Exception as e:
            print(e)

        await asyncio.sleep(5)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(simulate(csc_list))
