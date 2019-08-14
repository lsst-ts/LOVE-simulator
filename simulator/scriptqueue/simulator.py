import asyncio
from lsst.ts import salobj
from lsst.ts.idl.enums.ScriptQueue import Location


async def main(index):
    print('ScriptQueue | - Creating remote (CSC, index): (ScriptQueue', ', ', index, ')')
    domain = salobj.Domain()
    r = salobj.Remote(domain=domain, name='ScriptQueue', index=index)
    timeout = 30

    await salobj.set_summary_state(remote=r, state=salobj.State.ENABLED, timeout=timeout)

    isStandard = True
    path = 'script1'
    config_path = '/usr/src/love/simulator/scriptqueue/config.yml'
    with open(config_path, "r") as f:
        config = f.read()
    location = Location.LAST

    counter = 0
    while True:
        counter += 1
        try:
            await r.cmd_add.set_start(
                isStandard=isStandard,
                path=path,
                config=config,
                location=location,
                timeout=timeout
            )
        except Exception as e:
            print(e)
        await asyncio.sleep(1)
        if counter > 15:
            break

if __name__ == '__main__':
    print('--starting scriptqueue-sim loop---')
    asyncio.get_event_loop().run_until_complete(main())
