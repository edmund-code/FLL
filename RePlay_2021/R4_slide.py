#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time


# Create your objects here
ev3 = EV3Brick()

left_motor = Motor(Port.A)
right_motor = Motor(Port.B)

robot = DriveBase(left_motor, right_motor, wheel_diameter=93.5, axle_track=115)

robot.settings(600)
robot.straight(-450)
robot.stop()
time.sleep(0.5)
robot.settings(300, turn_rate = 30)
robot.straight(450)
robot.turn(-30)
robot.straight(400)
