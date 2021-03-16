# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.


import numpy as np
from nevergrad.parametrization import parameter
from ..base import ExperimentFunction
import gym


class GymAnm(ExperimentFunction):
    def __init__(self) -> None:
        super().__init__(gym_anm, parametrization=parameter.Array(shape=(100, 6)))


def gym_anm(x: np.ndarray):

    env = gym.make("gym_anm:ANM6Easy-v0")
    env.seed(0)
    _ = env.reset()  # output value = "o"

    reward = 0.0
    for i, val in enumerate(x):
        a = 10.0 * x[i]
        # o, r, done, info = env.step(a)
        try:
            _, r, _, _ = env.step(a)
        except AssertionError:  # Illegal action.
            return 1e20 / (1.0 + i)  # We encourage late failures rather than early failures.
        reward += r
        # print(f"action={a} (type={type(a)}), reward={r}")
        # env.render()
    return -reward
