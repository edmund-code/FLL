#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port
from pybricks.parameters import Direction
from pybricks.robotics import DriveBase
import math
import time

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
gyro_sensor = GyroSensor(Port.S3)
small_motor_left = Motor(Port.C, positive_direction=Direction.CLOCKWISE, gears=None)
robot = DriveBase(left_motor, right_motor, wheel_diameter=93.5, axle_track=120)

drive_distance = 0.0

def move_straight(speed, distance):

    right_motor.reset_angle(0)
    left_motor.reset_angle(0)
    gyro_sensor.reset_angle(0)
    
    while True:
        # motor_avg_distance = (right_motor.angle() + left_motor.angle()) / 2.0 / 360 * math.pi * 93.5
        # print("{}:{}:{}".format(motor_avg_distance, robot.distance(), distance))
        global drive_distance
        if abs(robot.distance()) >= abs(distance):
            robot.stop()
            break

        if check_stall(robot):
            return robot.distance()

        #reset PID controller
        err_p = 0.0
        err_i = 0.0
        err_d = 0.0

        err_prev = 0.0
        i = 0
        i += 1
        err_prev = err_p

   
        err_p = gyro_sensor.angle()
        err_i += err_p
        err_d = err_p - err_prev

        kp = 5.0
        ki = 0.0
        kd = 0.0


        turn_rate = kp * err_p + ki * err_i + kd * err_d

        if (abs(turn_rate) > 30):
            err_i *= 0.5
            turn_rate *= 0.5

        if (i % 20 == 0):
            print("Time={}, turn rate={}, P={}, I={}, D={}".format(i, turn_rate, err_p, err_i, err_d))

        robot.drive(-speed, turn_rate)
    drive_distance += robot.distance()

target_distance = 200
speed = 20

robot.distance_control.stall_tolerances(speed, 100)
robot.distance_control.limits(actuation = 40)

def check_stall(robot):
    if robot.distance_control.stalled():
        print("STALLED")
        robot.stop()
        return True

move_straight(200, 600)
move_straight(15, 250)
move_straight(-200, 700)
move_straight(200, 650)
traveled_distance = abs(move_straight(40, target_distance))
if traveled_distance <= target_distance: #stalled
        small_motor_left.run_angle(200, -75, wait=True)
for i in range(5):
    if traveled_distance <= target_distance: #stalled
        move_straight(-20, 25)
        move_straight(20, target_distance - traveled_distance)
small_motor_left.run_angle(200, 75, wait=True)
move_straight(-200, 800)