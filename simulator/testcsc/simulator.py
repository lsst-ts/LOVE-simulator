import asyncio
from lsst.ts import salobj


async def main():
    d = salobj.Domain()
    r = salobj.Remote(d, 'Test', 1)

    cmds = [
        r.cmd_enable,
        r.cmd_fault,
        r.cmd_standby,
        r.cmd_start,
    ]
    while True:
        for command in cmds:
            try:
                await command.start()
            except Exception as e:
                print(e)
            await asyncio.sleep(5)


asyncio.get_event_loop().run_until_complete(main())