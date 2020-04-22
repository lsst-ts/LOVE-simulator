import asyncio
import numpy as np
import random
import time


def randomize_single_value(value):
    if isinstance(value, (int, np.integer)):
        return random.choice([0, 1, 2, 3, 4])
    if isinstance(value, float):
        return random.random()
    if isinstance(value, str):
        return random.choice(['a', 'b', 'c'])
    return value


def randomize_params(data):

    evt_param_names = [x for x in dir(data) if not x.startswith('__')]
    for param_name in evt_param_names:
        evt_param = getattr(data, param_name)
        if isinstance(evt_param, (list, tuple, np.ndarray)):
            for i in range(len(evt_param)):
                evt_param[i] = randomize_single_value(evt_param[i])
        else:
            setattr(data, param_name, randomize_single_value(evt_param))


def emit(controller, test_seed=None):
    if(test_seed is not None):
        random.seed(test_seed)
    evt_names = controller.salinfo.event_names
    for evt in evt_names:
        evt_controller = getattr(controller, "evt_" + evt)
        data_output = evt_controller.DataType()
        randomize_params(data_output)
        evt_controller.put(data_output)


def emit_forever(controller, frequency, loop):
    asyncio.set_event_loop(loop)
    period = 1/frequency
    while True:
        time.sleep(period)
        emit(controller)
