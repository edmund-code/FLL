#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from time import sleep
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.
# Create your objects here.
ev3 = EV3Brick()
# Write your program here.
ev3.speaker.beep()
# Initialize the motors.
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
ir_sensor = InfraredSensor(Port.S4)
ir_sensor.beacon(1)
while True:
    buttons = ir_sensor.keypad()
    if len(buttons) == 1:
        print(buttons[0])
        if (buttons[0] == Button.LEFT_UP):
            print("###")
            robot.straight(-30)
        elif (buttons[0] == Button.RIGHT_UP):
            pass
        elif (buttons[0] == Button.LEFT_DOWN):
            pass
        elif (buttons[0] == Button.RIGHT_DOWN):
            pass
    elif len(buttons) == 2:
        print(str(buttons[0]) + " and " + str(buttons[1]))
    else:
        continue
    sleep(0.1)