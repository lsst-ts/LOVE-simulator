# This file is part of LOVE-simulator.
#
# Copyright (c) 2023 Inria Chile.
#
# Developed by Inria Chile.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or at
# your option any later version.
#
# This program is distributed in the hope that it will be useful,but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.


import random
import time
import numpy as np
import asyncio


def randomize_single_value(value):
    if isinstance(value, (int, np.integer)):
        return random.choice([0, 1])
    if isinstance(value, float):
        return random.random()
    if isinstance(value, str):
        return random.choice(["a", "b", "c"])
    return value


def randomize_params(data):

    tel_param_names = [x for x in dir(data) if not x.startswith("__")]
    for param_name in tel_param_names:
        tel_param = getattr(data, param_name)
        if isinstance(tel_param, (list, tuple, np.ndarray)):
            for i in range(len(tel_param)):
                tel_param[i] = randomize_single_value(tel_param[i])
        else:
            setattr(data, param_name, randomize_single_value(tel_param))


def emit(controller, test_seed=None):
    if test_seed is not None:
        random.seed(test_seed)
    tel_names = controller.salinfo.telemetry_names
    for tel in tel_names:
        tel_controller = getattr(controller, "tel_" + tel)
        data_output = tel_controller.DataType()
        randomize_params(data_output)
        tel_controller.put(data_output)


def emit_forever(controller, frequency, loop):
    asyncio.set_event_loop(loop)
    period = 1 / frequency
    while True:
        time.sleep(period)
        emit(controller)
