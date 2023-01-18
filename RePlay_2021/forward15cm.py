#!/usr/bin/env pybricks-micropython

import fll_briarcliff6pack

my_robot = fll_briarcliff6pack.Bri6Pack()
drive_base = my_robot.drive_base

my_robot.drive_pid(speed=150, distance=150)