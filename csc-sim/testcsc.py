import asyncio
from lsst.ts import salobj

csc = salobj.TestCsc(index=1)


async def make_error():
    while True:
        code = 52
        report = "Report for error code"
        traceback = "Traceback for error code"
        csc.fault(code=code, report=report, traceback=traceback)
        await asyncio.sleep(5)
    

loop = asyncio.get_event_loop()

asyncio.ensure_future(csc.done_task)
loop.create_task(make_error())
loop.run_forever()
