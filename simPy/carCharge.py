#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Bruce Han <superhxl@gmail.com>
#
# Distributed under terms of the MIT license.
"""
汽车停车、充电仿真。相比第一个例子，定义了汽车类，具有两个动作：run和charge。
"""
import simpy


class Car(object):
    """汽车类Car. """

    def __init__(self, env):
        """初始化函数.
        :env:环境对象
        """
        self.env = env

    def run(self):
        """汽车行驶过程。"""
        while True:
            print("汽车开始停车充电，当前时刻%d" % self.env.now)
            charge_duraion = 5
            yield self.env.process(self.charge(charge_duraion))

            print("汽车开始行驶，当前时刻%d" % self.env.now)
            trip_duration = 2
            yield self.env.timeout(trip_duration)

    def charge(self, duration):
        """汽车充电过程"""
        yield self.env.timeout(duration)


def main():
    """主函数。"""
    env = simpy.Environment()
    # 实例化一辆汽车
    car = Car(env)
    # 汽车开始行驶
    env.process(car.run())
    env.run(until=15)


if __name__ == "__main__":
    main()
