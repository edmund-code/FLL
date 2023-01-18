#!/usr/bin/env pybricks-micropython

import fll_briarcliff6pack
from pybricks.parameters import Stop
import time

my_robot = fll_briarcliff6pack.Bri6Pack()
drive_base = my_robot.drive_base

run_m02 = True
run_m08 = True
run_m06 = True

# M02 Step Counter
if run_m02:
    my_robot.drive_pid(speed=380, distance=1220)
    time.sleep(0.2)
    
    # turn counter clockwise and prepare to go through the gate
    # You can only change the settings while the robot is stopped. 
    # This is either before you begin driving or after you call stop().
    drive_base.stop()
    drive_base.settings(straight_speed=100, turn_rate=100)
    drive_base.straight(-95)
    drive_base.turn(-100)

    drive_base.straight(-130)    # move backward to align with the wall
    my_robot.drive_pid(speed=200, distance=785)   # go through the gate
    drive_base.stop()

# M08 Boccia
if run_m08:
    drive_base.settings(straight_speed=30, turn_rate=30)
    drive_base.straight(-50)
    drive_base.turn(37)
    drive_base.stop()
    drive_base.settings(straight_speed=100, turn_rate=100)
    drive_base.straight(175)
    drive_base.straight(-40)
    drive_base.stop()
    drive_base.settings(straight_speed=30, turn_rate=30)
    drive_base.turn(-50)
    drive_base.straight(100)
    my_robot.small_motor_left.run_angle(-50, -100)   # dump the cubes
    drive_base.stop()

# M06 Pull-up Bar
if run_m06:
    my_robot.small_motor_right.run_angle(400, 900, wait=False)
    drive_base.settings(straight_speed=100, turn_rate=100)
    drive_base.turn(4)
    drive_base.straight(-470)
    my_robot.small_motor_right.run_angle(-400, 500, then=Stop.HOLD, wait=True)
    my_robot.small_motor_right.hold()
