#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Bruce Han <superhxl@gmail.com>
#
# Distributed under terms of the MIT license.
"""
电动汽车在电池充电站充电仿真：充电站有两个充电点，汽车充电需占用充电点，充电完
成后释放，为后续汽车继续充电。
"""
import simpy


def car(env, name, bcs, driving_time, charge_duration):
    """汽车：
    bcs，充电站
    """
    # 汽车向充电站行驶，行驶时间为driving_time
    yield env.timeout(driving_time)

    print('%s 到达充电站，当前时刻 %d' % (name, env.now))
    # 请求占用充电资源：有空闲充电站则占用，否则等待直至有可用充电点
    with bcs.request() as req:
        yield req

        # Charge the battery
        print("%s starting to charge at %s" % (name, env.now))
        yield env.timeout(charge_duration)
        print("%s leaving the bcs at %s" % (name, env.now))
