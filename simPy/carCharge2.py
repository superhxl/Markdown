# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Bruce Han <superhxl@gmail.com>
#
# Distributed under terms of the MIT license.
"""
汽车充电仿真，汽车可以在为充满电的情况下中断充电而开始驾驶
中断：一类特殊的事件
"""
import simpy


class Car():
    """汽车类Car. """

    def __init__(self, env):
        """初始化. """
        self.env = env

    def run(self):
        """驾驶"""
        while True:
            print('开始停车充电，当前时刻 %d' % self.env.now)
            charge_duration = 5
            try:
                yield self.env.process(self.charge(charge_duration))
            except simpy.Interrupt:
                print('充电中断，希望电量够用')

            print('开始行驶，当前时刻 %d' % self.env.now)
            trip_duration = 2
            yield self.env.timeout(trip_duration)

    def charge(self, duration):
        """充电"""
        yield self.env.timeout(duration)


def driver(env, proc):
    """司机中断充电"""
    yield env.timeout(3)
    proc.interrupt()


if __name__ == "__main__":
    env = simpy.Environment()
    car1 = Car(env)
    action = env.process(car1.run())
    env.process(driver(env, action))
    env.run(until=15)
