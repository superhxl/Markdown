#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Bruce Han <superhxl@gmail.com>
#
# Distributed under terms of the MIT license.
"""
First example using simPy
"""
import simpy


def car(env):
    """汽车进程：停车一段时间后驶出"""
    while True:
        print("开始停车，当前时刻%d" % env.now)
        parking_duration = 5
        yield env.timeout(parking_duration)

        print("开始行驶，当前时刻%d" % env.now)
        trip_duration = 2
        yield env.timeout(trip_duration)


def main():
    # 创建环境实例
    env = simpy.Environment()
    env.process(car(env))
    env.run(until=15)


if __name__ == "__main__":
    main()
