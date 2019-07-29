import asyncio
import json
from lsst.ts import salobj


async def launch(salindex):
    csc = salobj.TestCsc(index=salindex)
    asyncio.ensure_future(csc.done_task)
    while True:
        code = 52
        report = "Report for error code"
        traceback = "Traceback for error code"
        csc.fault(code=code, report=report, traceback=traceback)
        await asyncio.sleep(5)

simulator_config_path = '/home/saluser/config/config.json'
with open(simulator_config_path) as f:
    simulator_config = json.loads(f.read())
if 'Test' in simulator_config.keys():
    awaitables = []
    for testcsc_config in simulator_config['Test']:
        if testcsc_config['source'] == 'command_sim':
            salindex = testcsc_config['index']
            print('Test CSC | Launching salindex = {}'.format(salindex))
            awaitables.append(launch(salindex))

asyncio.get_event_loop().run_until_complete(asyncio.wait(awaitables))
