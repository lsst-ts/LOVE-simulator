# Most of this was adapted from https://github.com/lsst-ts/ts_salobj/blob/develop/tests/test_csc.py
import asyncio
import json
from lsst.ts import salobj
import logging

STD_TIMEOUT = 15  # timeout for command ack
LONG_TIMEOUT = 30  # timeout for CSCs to start
EVENT_DELAY = 0.1  # time for events to be output as a result of a command
NODATA_TIMEOUT = 0.1  # timeout for when we expect no new data
SHOW_LOG_MESSAGES = False


class FailedCallbackCsc(salobj.TestCsc):
    """A CSC whose do_wait command raises a RuntimeError and whose do_fault command includes a report"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.exc_msg = "do_wait raised an exception on purpose on Test-{}".format(kwargs["index"])
        self.index = kwargs["index"]

    async def do_wait(self, data):
        raise RuntimeError(self.exc_msg)

    async def do_fault(self, data):
        """Execute the fault command with a report, code and traceback.
        Change the summary state to State.FAULT
        """
        self.log.warning("Executing fault on Test-{}".format(self.index))
        code = 52
        report = "Report for error code for Test-{}".format(self.index,)
        traceback = "Traceback for error code for Test-{}".format(self.index,)
        self.fault(code=code, report=report, traceback=traceback)


class LogMessagesMock():
    """Triggers logMessages and errorCode events in a TestCSC """

    def __init__(self, salindex, *args, **kwargs):
        self.csc = FailedCallbackCsc(index=salindex, *args, **kwargs)
        d = salobj.Domain()
        self.r = salobj.Remote(d, 'Test', salindex)
        self.salindex = salindex

    async def set_log_level(self):
        await self.r.start_task
        await self.r.cmd_setLogLevel.set_start(level=logging.DEBUG, timeout=STD_TIMEOUT)

    def log_info_message(self):
        info_message = "test info message for Test-{}".format(self.salindex,)
        self.csc.log.info(info_message)

    def log_warn_message(self):
        warn_message = "test warn message for Test-{}".format(self.salindex,)
        self.csc.log.warning(warn_message)

    async def log_error_message(self):
        await self.r.start_task
        with salobj.assertRaisesAckError():
            await self.r.cmd_wait.set_start(duration=5, timeout=STD_TIMEOUT)

    async def printmessage(self):
        await self.r.start_task
        msg = await self.r.evt_logMessage.next(flush=True)
        print('\n TestCSC', self.salindex, ' | msg:', msg.message, '\nlvl:', msg.level, '\ntrace:', msg.traceback)


async def launch(salindex, debug=False):
    mock = LogMessagesMock(salindex, initial_state=salobj.State.ENABLED)
    await mock.csc.start_task
    asyncio.ensure_future(mock.csc.done_task)
    await mock.set_log_level()
    logmessages = [
        mock.log_info_message,
        mock.log_warn_message,
        mock.log_error_message
    ]

    counter = 1

    while True:
        for index, message in enumerate(logmessages):
            if index == 2:
                await message()
            else:
                message()
            if debug:
                while True:
                    try:
                        await mock.printmessage()
                    except asyncio.TimeoutError:
                        break
            counter += 1
            await asyncio.sleep(5)

if __name__ == '__main__':
    simulator_config_path = '/home/saluser/config/config.json'
    with open(simulator_config_path) as f:
        simulator_config = json.loads(f.read())
    if 'Test' in simulator_config.keys():
        awaitables = []
        for testcsc_config in simulator_config['Test']:
            if testcsc_config['source'] == 'command_sim':
                salindex = testcsc_config['index']
                print('Test CSC | Launching salindex = {}'.format(salindex))
                awaitables.append(launch(salindex, True))

        asyncio.get_event_loop().run_until_complete(asyncio.wait(awaitables))
