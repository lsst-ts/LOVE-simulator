import asyncio
from lsst.ts import salobj
from lsst.ts.idl.enums.ScriptQueue import Location


async def main(index):
    print('ScriptQueue | - Creating remote (CSC, index): (ScriptQueue', ', ', index, ')')
    domain = salobj.Domain()
    r = salobj.Remote(domain=domain, name='ScriptQueue', index=index)
    await r.start_task
    timeout = 30

    await salobj.set_summary_state(remote=r, state=salobj.State.ENABLED, timeout=timeout)
