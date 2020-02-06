#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Bruce Han <superhxl@gmail.com>
#
# Distributed under terms of the MIT license.

"""
GasStation simulation with simPy
"""

import simpy

class GasStation():
    def __init__(self, env):
        self.fuel_dispensers = simpy.Resource(env, capacity=2)
        self.gas_tank = simpy.Container(env, capacity=1000, init=100)
        self.mon_proc = env.process(self.monitor_tank(env))

    def monitor_tank(self, env):
        while True:
            if self.gas_tank.level < 100:
                print("Calling tanker at %s" % env.now)
                env.process(tanker(env, self))

            yield env.timeout(15)

def tanker(env, gas_station):
    yield env.timeout(10)   # Need 10 minutes to arrive
    print("Tanker arriving at %s" % env.now)
    amount = gas_station.gas_tank.capacity - gas_station.gas_tank.level
    yield gas_station.gas_tank.put(amount)

def car(name, env, gas_station):
    print("Car %s arriving at %s" % (name, env.now))
    with gas_station.fuel_dispensers.request() as req:
        yield req
        print('Car %s starts refueling at %s' % (name, env.now))
        yield gas_station.gas_tank.get(40)
        yield env.timeout(5)
        print("Car %s done refueling at %s" % (name, env.now))


def car_generator(env, gas_station):
    for i in range(4):
        env.process(car(i, env, gas_station))
        yield env.timeout(5)


def main():
    env = simpy.Environment()
    gas_station = GasStation(env)
    car_gen = env.process(car_generator(env, gas_station))
    env.run(35)

if __name__ == "__main__":
    main()


        
