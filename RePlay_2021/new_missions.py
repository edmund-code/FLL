#!/usr/bin/env pybricks-micropython

import fll_briarcliff6pack
from pybricks.parameters import Stop
import time

my_robot = fll_briarcliff6pack.Bri6Pack()
drive_base = my_robot.drive_base

# You can only change the settings while the robot is stopped. 
# This is either before you begin driving or after you call stop().

run_m12 = True
run_m13 = True

#my_robot.drive_pid(915, 1500)
#my_robot.drive_pid(250, 250)
#time.sleep(1)
#my_robot.drive_pid(70, -270)

# M12 Row Machine
if run_m12:
    drive_base.stop()
    drive_base.settings(straight_speed=100, turn_rate=100)
    drive_base.turn(-45)
    drive_base.straight(70)
    my_robot.small_motor_left.run_angle(200, 325)  
    drive_base.straight(-75)

    drive_base.stop()
    drive_base.settings(straight_speed=100, turn_rate=50)
    drive_base.straight(10)
    drive_base.turn(-50)
    drive_base.straight(25)
    my_robot.small_motor_left.run_angle(200, -100)   # lift the arm
    drive_base.turn(-40)
    drive_base.straight(210)
    drive_base.turn(52.5)
#    my_robot.small_motor_left.run_angle(-150, -109)  
#    my_robot.small_motor_left.run_angle(-155, 130)

# M13 Weight Machine
if run_m13:
    drive_base.stop()
    drive_base.settings(straight_speed=100, turn_rate=100)
    my_robot.small_motor_left.run_angle(190, 75, wait=False)   # lower the arm
    drive_base.straight(360)
    
    my_robot.small_motor_left.run_angle(80, -250) # raise the arm
    drive_base.stop()
    drive_base.settings(straight_speed=250)
    drive_base.straight(-360)
    drive_base.turn(-35)
    drive_base.straight(-500)
    drive_base.straight(120)
    drive_base.turn(90)
    drive_base.stop()
    drive_base.settings(straight_speed=700)
    drive_base.straight(-1600)

   