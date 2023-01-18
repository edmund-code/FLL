#!/usr/bin/env pybricks-micropython

import fll_briarcliff6pack
import sys
import time

# Initialize the drive base.
my_robot = fll_briarcliff6pack.Bri6Pack()
drive_base = my_robot.drive_base

drive_base.settings(turn_rate=60)
my_robot.drive_pid(speed=100, distance=355)
shake_factor = 1
drive_base.turn(-14 * shake_factor)
drive_base.turn(12.5 * shake_factor)

drive_base.straight(200)
drive_base.stop()
drive_base.settings(straight_speed=150)
drive_base.straight(-500)