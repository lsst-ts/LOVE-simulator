import asyncio
from lsst.ts import salobj

csc = salobj.TestCsc(index=1)

asyncio.get_event_loop().run_until_complete(csc.done_task)