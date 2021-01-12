import asyncio
from lsst.ts import salobj


async def main():
    while True:
        try:
            print("Starting GenericCamera Simulator")
            r = salobj.Remote(salobj.Domain(), "GenericCamera", index=1)
            await r.start_task
            await salobj.set_summary_state(r, salobj.State.ENABLED)
            await r.cmd_startLiveView.set_start(expTime=0.5)
            break
        except Exception as e:
            print("Error starting GenericCamera Simulator. Retrying in 1 second")
            await asyncio.sleep(1)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
