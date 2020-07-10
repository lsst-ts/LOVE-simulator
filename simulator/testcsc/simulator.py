import asyncio
from lsst.ts import salobj


async def main(salindex):
    d = salobj.Domain()
    r = salobj.Remote(d, 'Test', salindex)
    await r.start_task

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
                print('Test CSC error:', e)
            await asyncio.sleep(5)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main(1))
