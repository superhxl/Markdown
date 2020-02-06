# !/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Bruce Han <superhxl@gmail.com>
#
# Distributed under terms of the MIT license.

"""
CarWash example
A carwash has a limited number of washing machines and defines a wash
processes that take some random time.

Car processes arrive at the carwash at a random time. If one washing machaine
is available, they start the washing process and wait for it to finish. If
not, they wait until they can use one.
"""
import random
import simpy


RANDOM_SEED = 42
NUM_MACHINES = 2    # Number of machines in the carwash
WASHTIME = 5        # Minutes it takes to clean a car
T_INTER = 7         # Create a car every 7 minutes
SIM_TIME = 20       # Simulation time in minutes


class CarWash(object):
    """洗车店有一定数量的机器，能够并行提供洗车服务。车辆洗车需要占用一台机器
    。洗完后，机器释放并继续为等候车辆服务。
    """
    def __init__(self, env, num_machines, washtime):
        self.env = env
        self.machine = simpy.Resource(env, num_machines)
        self.washtime = washtime

    def wash(self, car):
        """洗车过程函数。通过传入一个'car'进程，提供洗车."""
        # 洗车花费WASHTIME，因此在此时间后洗车完成
        yield self.env.timeout(WASHTIME)
        print("洗车清除了车子%s的%d%%的灰尘" % (car, random.randint(50, 99)))


def car(env, name, cw):
    """车辆进程"""
    print('%s 到达洗车店时刻 %.2f.' % (name, env.now))
    with cw.machine.request() as req:
        yield req

        print('%s 开始洗车时刻 %.2f.' % (name, env.now))
        yield env.process(cw.wash(name))

        print('%s 完成洗车时刻 %.2f.' % (name, env.now))


def setup(env, num_machines, washtime, t_inter):
    """生成洗车店，店内初始有一系列待洗车辆，平均洗车时间为t_inter分钟."""
    carwash = CarWash(env, num_machines, washtime)

    # 初始有4辆汽车
    for i in range(4):
        env.process(car(env, 'Car %d' % i, carwash))

    # 仿真开始后生成更多汽车，到达间隔随机整数
    while True:
        yield env.timeout(random.randint(t_inter - 2, t_inter + 2))
        i += 1
        env.process(car(env, 'Car %d' % i, carwash))


def main():
    """The main function"""
    # Setup and start the simulation
    print("Carwash")
    random.seed(RANDOM_SEED)

    # Create an environment and start the setup process
    env = simpy.Environment()
    env.process(setup(env, NUM_MACHINES, WASHTIME, T_INTER))

    # Execute
    env.run(until=SIM_TIME)


if __name__ == "__main__":
    main()
