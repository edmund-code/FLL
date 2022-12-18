from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
import math
import sys

hub = PrimeHub()


class FllRobot:

    def move(self, distance, speed = 50):
        self._motor_pair.move_tank(distance, 'cm', speed, speed)
    
    def turn(self, degree, speed = 30):
        factor = 0.82
        distance = self._distance_between_wheels * math.pi/360 * degree * factor
        

        self._motor_pair.move_tank(distance, 'cm', speed, -speed)

    def turn_left_arm(self, degree, speed = 50):
        self._left_motor.run_for_degrees(degree, speed)

    def start_left_arm(self, speed=50):
        self._left_motor.start(speed)    

    def stop_left_arm(self):
        self._left_motor.stop()

    def start_right_arm(self, speed=50):
        self._right_motor.start(speed)

    def stop_right_arm(self):
        self._right_motor.stop()


    def turn_right_arm(self, degree, speed = 50):
        self._right_motor.run_for_degrees(degree, speed)

    def __init__(self):
        self._wheel_diameter = 5.5
        self._distance_between_wheels = 10.0 
        self._motor_pair = MotorPair('D', 'C')
        self._left_motor = Motor('B')
        self._right_motor = Motor('A')
        #self.motor_pair.set_motor_rotation(distance_between_wheels * math.pi, 'cm')
    
myRobot = FllRobot()

#myRobot.turn_left_arm(180, 50)
# for i in range(4):
#     myRobot.move(10)
#     myRobot.turn(-90)
# myRobot.turn_left_arm(360)
# myRobot.turn_right_arm(-360)

def mission_02():
    for i in range(3):
        myRobot.move(13,30)
        wait_for_seconds(0.4)
        myRobot.move(-8,30)

#mission_02()
def mission_05():
    myRobot.move(9,30)
    myRobot.move(-6,30)
    wait_for_seconds(0.3)
    myRobot.move(-3,70)
#motor_pair.move(8.1 * pi / 2, 'cm', steering=100)

#for i in range(3):
    myRobot.move(6.5,60)
    myRobot.move(-6.5,60)

#raise SystemExit

##########Two-stick + door model##########
def OilPlatform():
    myRobot.turn_right_arm(-50, 40)
    myRobot.move(79, 100)
    myRobot.turn_right_arm(70, 40)
    myRobot.move(-79, 100)
def OilPlatform2():
    myRobot.turn_right_arm(70, 40)
    myRobot.move(62.4, 70)
    for i in range(3):
        myRobot.turn_right_arm(-40,40)
        myRobot.turn_right_arm(40, 40)
    myRobot.move(-10, 50)
    myRobot.turn(15)
    myRobot.move(20,50)
    myRobot.turn_right_arm(-50,40)

def Run1():
    #TV
    myRobot.move(29,50)
    

    myRobot.move(-13.5,50)
    #raise arm
    myRobot.turn_right_arm(-50,40)
    myRobot.turn(-66,20)
    myRobot.move(41,50) #added two cms
    #put arm down
    myRobot.turn_right_arm(50,40)
   
    myRobot.turn(103,20)   

    myRobot.move(40,60)
    for i in range(2):
        myRobot.move(-7,20)
        myRobot.move(14,40)
    #done with windmill

    myRobot.move(-29,55)
    wait_for_seconds(0.5)
    myRobot.turn(-89,20)
    myRobot.move(34,40)
    wait_for_seconds(0.7)
    myRobot.turn(10,40)
    wait_for_seconds(0.5)
    myRobot.turn_right_arm(-60,100)
    myRobot.turn_right_arm(60,100)
    myRobot.move(-10,30)
    myRobot.turn(-100,25)
    myRobot.move(55,85)
    myRobot.turn(-40,25)
    # start next mission
    myRobot.start_left_arm(-20)
    myRobot.move(10,30)
    myRobot.stop_left_arm()
    myRobot.turn_left_arm(80,80)
    myRobot.turn(20,30)
    myRobot.move(-3,30)
    myRobot.turn_left_arm(-90,90)
    myRobot.turn(40,30)
    myRobot.move(75,100)

def Run2():
    myRobot.start_right_arm(-40)
    myRobot.stop_right_arm()
    myRobot.move(-5,80)
    myRobot.move(20,60)
    myRobot.turn(35,50)
    myRobot.move(64,50)
    myRobot.turn(55,40)
    myRobot.move(-15,50)
    myRobot.move(7,50)
    myRobot.move(-8,60)
    myRobot.move(7,50)
    myRobot.move(-8,60)
    myRobot.move(6,50)
    myRobot.turn(-99,40)
    myRobot.move(3,40)
    myRobot.turn_right_arm(35,60)
    myRobot.move(-6,70)
    myRobot.turn(-16,30)
    myRobot.move(-21,90)
    myRobot.turn(50,40)
    myRobot.move(-60,90)
Run1()
