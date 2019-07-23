import asyncio
from lsst.ts import salobj


async def simulate_one(csc, salindex):
    """Simulates changes in the summaryState of a given component

    Parameters
    ----------
    csc_list: `[()]`
        The list of CSCs to run as a tuple with the CSC name and index
    """
    print('SummaryState| - Creating remote (CSC, index): (', csc, ', ', salindex, ')')
    d = salobj.Domain()
    r = salobj.Remote(d, csc, salindex)
    flag = False
    while True:
        try:
            if flag:
                await r.cmd_enable.start()
            else:
                await r.cmd_disable.start()
        except Exception as e:
            print(e)

        flag = not flag
        await asyncio.sleep(6)


async def simulate_many(cscList):
    for (csc, salindex) in cscList:
        asyncio.create_task(simulate_one(csc, salindex))
    while True:
        await asyncio.sleep(1)


if __name__ == '__main__':
    cscList = [
        ['ATDome', 1],
        ['ScriptQueue', 1]

    ]
    asyncio.get_event_loop().run_until_complete(simulate_many(cscList))
