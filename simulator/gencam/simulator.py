import asyncio
from lsst.ts import salobj

async def main():
    r = salobj.Remote(salobj.Domain(), "GenericCamera", index=1)
    await salobj.set_summary_state(r, salobj.State.ENABLED)    
    await r.cmd_startLiveView.set_start(expTime=0.5) 



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
