import asyncio
import random
from lsst.ts import salobj


async def simulation_step(
    r,
    azimuth,
    azimuthMax,
    elevation,
    elevationMax,
    nasmyth1_rotator_angle,
    nasmyth1_rotator_angle_max,
    nasmyth2_rotator_angle,
    nasmyth2_rotator_angle_max,
    trackingLoops,
    loop_count,
    loop_count2,
):
    if loop_count == 1:
        t = await r.cmd_startTracking.start(timeout=10)
    r.cmd_trackTarget.set(
        azimuth=azimuth + azimuthMax / trackingLoops * loop_count,
        azimuthVelocity=3,
        elevation=elevation + elevationMax / trackingLoops * loop_count,
        elevationVelocity=3,
        nasmyth1_rotator_angle=nasmyth1_rotator_angle
        + nasmyth1_rotator_angle_max / trackingLoops * loop_count,
        nasmyth1_rotator_angleVelocity=3,
        nasmyth2_rotator_angle=nasmyth2_rotator_angle
        + nasmyth2_rotator_angleMax / trackingLoops * loop_count,
        nasmyth2_rotator_angleVelocity=3,
        taiTime=t.private_sndStamp,
        trackId=1,
    )
    if loop_count < trackingLoops:
        t = await r.cmd_trackTarget.start(timeout=10)
        await asyncio.sleep(0.25)
    if loop_count > trackingLoops:
        loop_count = 0
        await r.cmd_stopTracking.start(timeout=20)
        r.cmd_setInstrumentPort.set(port=random.choice([1, 2, 3]))
        r.evt_m3InPosition.flush()
        await r.cmd_setInstrumentPort.start(timeout=10)
        while True:
            data = await r.evt_m3InPosition.next(flush=False)
            if data.inPosition:
                break
        return 0
    return loop_count + 1


async def main_csc(name, index, domain):
    """Runs the ATMCS simulator

    Parameters
    ----------
    csc_list: `[()]`
        The list of CSCs to run as a tuple with the CSC name and index
    """
    print("\nATMCS      | **** Starting ATMCS command simulator loop *****")
    print("ATMCS      | - Creating remote (CSC, index): (", name, ", ", index, ")")
    r = salobj.Remote(domain=domain, name=name, index=index)
    await r.start_task
    try:
        await r.cmd_start.start(timeout=30)
        await r.cmd_enable.start(timeout=30)
        await r.evt_heartbeat.next(flush=True, timeout=5)
    except Exception as e:
        print(e)

    azimuth = 0
    azimuthMax = 260
    elevation = 10
    elevationMax = 70
    nasmyth1_rotator_angle = 0
    nasmyth1_rotator_angle_max = 90
    nasmyth2_rotator_angle = 0
    nasmyth2_rotator_angle_max = 90
    trackingLoops = 120
    loop_count = 0
    loop_count2 = 0

    class Object(object):
        pass

    t = Object()
    t.private_sndStamp = 0
    while True:
        try:
            loop_count = await simulation_step(
                azimuth,
                azimuthMax,
                elevation,
                elevationMax,
                nasmyth1_rotator_angle,
                nasmyth1_rotator_angle_max,
                nasmyth2_rotator_angle,
                nasmyth2_rotator_angle_max,
                trackingLoops,
                loop_count,
                loop_count2,
            )

        except Exception as e:
            print(e)
            try:
                await r.cmd_standby.start()
            except Exception as e:
                pass
            try:
                await r.cmd_start.start()
            except Exception as e:
                pass
            try:
                await r.cmd_enable.start()
            except Exception as e:
                pass
            loop_count = 0
            await asyncio.sleep(10)


async def main(csc_list, domain):
    """Runs the ATMCS simulator

    Parameters
    ----------
    csc_list: `[()]`
        The list of CSCs to run as a tuple with the CSC name and index
    """
    print("\nATMCS      | **** Starting ATMCS command simulator loop *****")
    for csc in csc_list:
        name = csc[0]
        index = None
        if csc[1] is not None:
            index = int(csc[1])
        asyncio.get_event_loop().create_task(main_csc(name, index, domain))
