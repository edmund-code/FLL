#!/usr/bin/env pybricks-micropython
import fll_briarcliff6pack
from pybricks.parameters import Stop
import time
from pybricks.ev3devices import (ColorSensor)
from pybricks.parameters import Port, Color
my_robot = fll_briarcliff6pack.Bri6Pack()
drive_base = my_robot.drive_base
# Initialize the color sensor.
#line_sensor1 = ColorSensor(Port.S1)
#line_sensor2 = ColorSensor(Port.S2)
drive_base.settings(straight_acceleration=400, turn_acceleration=200)
drive_base.straight(-5)

my_robot.drive_pid(speed=300, distance=840)

drive_base.straight(-25)
my_robot.small_motor_left.control.stall_tolerances(speed=15, time=1000)
#my_robot.small_motor_left.control.limits(actuation=100)

rotated = 0
my_robot.small_motor_left.reset_angle(angle=0)
fail_count = 0
while rotated <= 602:
    my_robot.small_motor_left.run_time(speed=700, time=200, then=Stop.HOLD, wait=False)
    rotated = my_robot.small_motor_left.angle()
    if my_robot.small_motor_left.control.stalled():
        # TODO: add a max counter to bail out
        print("stalled")
        print("rotated:" + str(rotated))
        if fail_count < 10:
            my_robot.small_motor_left.run_time(speed=-1000, time=500, then=Stop.COAST, wait=True)
        else:
            my_robot.small_motor_left.run_time(speed=-500, time=200, then=Stop.COAST, wait=True)
        rotated = my_robot.small_motor_left.angle()
        print("rotated:" + str(rotated))
        fail_count = fail_count + 1
rotated = my_robot.small_motor_left.angle()
print("final rotated:" + str(rotated))

#lower boom
my_robot.small_motor_left.run_time(speed=-1000, time=300, then=Stop.COAST, wait=True)
#reverse to mission 08
drive_base.straight(-50)
drive_base.turn(-15)
drive_base.straight(-150)
drive_base.turn(41)

# lower the orange boom for mission 8
my_robot.small_motor_left.run_time(speed=-1000, time=700, then=Stop.COAST, wait=False)
# GOTO mission 08
drive_base.straight(200)
# lift the orange boom
my_robot.small_motor_left.run_time(speed=1000, time=1000, then=Stop.COAST, wait=True)
drive_base.stop()
drive_base.settings(straight_speed=100000, straight_acceleration=1000)
drive_base.straight(-900)