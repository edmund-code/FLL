from spike import PrimeHub, LightMatrix, Button, App, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
import math
import sys

hub = PrimeHub()

'''
A class is a code template for creating objects.
Objects have member variables and have behavior associated with them.

The FllRobot class provides a template to stores the properties and status of a robot,
e.g. distance between wheels, wheel size, how motors are connected to the robot, ...etc.,
and functions to control the robot.
'''
class FllRobot:
    '''
    All classes have a function called __init__(), which is always executed when the class is being initiated.
    Use the __init__() function to assign values to object properties
    '''
    def __init__(self):
        self._wheel_diameter = 5.5  # unit: cm
        self._distance_between_wheels = 10.0    # unit: cm
        self._motor_pair = MotorPair('D', 'C')
        self._left_motor = Motor('B')
        self._right_motor = Motor('A')
        #self.motor_pair.set_motor_rotation(distance_between_wheels * math.pi, 'cm')

    def move(self, distance, speed = 50):
        # use the build-in move_tank() function to take advantage of the built-in PID
        # this function set the same speed for both motors so it moves straight
        self._motor_pair.move_tank(distance, 'cm', speed, speed)

    def turn(self, degree, speed = 30):
        factor = 0.82 # in a perfect world this should be 1.0
        distance = self._distance_between_wheels * math.pi/360 * degree * factor

        # motors rotate in opposite direction so the robot turns in a tank-like motion
        self._motor_pair.move_tank(distance, 'cm', speed, -speed)

    # For left arm, negative is down
    def turn_left_arm(self, degree, speed = 50):
        self._left_motor.run_for_degrees(degree, speed)

    def right_arm_stop_action(self, action):
        self._right_motor.set_stop_action(action)

    # For right arm, negative is up
    def turn_right_arm(self, degree, speed = 50):
        self._right_motor.run_for_degrees(degree, speed)

    '''
    unlike run_for_degrees(), start() is not blocking
    this is useful if we want to drive the robot while the arm is moving
    '''
    def start_left_arm(self, speed=70):
        self._left_motor.start(speed)

    def stop_left_arm(self):
        self._left_motor.stop()

    def start_right_arm(self, speed=50):
        self._right_motor.start(speed)

    def stop_right_arm(self):
        self._right_motor.stop()


'''
===================================================================
Beginning of the code for the Super Power season
===================================================================
'''

# create a new FllRobot object.
myRobot = FllRobot()

#raise SystemExit

'''
Run 1 attempts the following missions:
    M08: Watch Television
    M15: Rechargeable Battery (collect 1 rechargeble battery)
    M07: Wind Turbine (collect 3 energy units)
    M06: Hybrid Car
    M10: Power Plant (release 3 energy units)
    M09: Dinosaur Toy (deliver to site B)
'''
def run_1():
    # move back to align with the wall (reduce error)
    myRobot.move(-0.5, 20)

    # M08: Watch Television
    myRobot.move(48.5, 55)
    myRobot.move(-14, 45)

    # raise right arm
    myRobot.turn_right_arm(-50, 40)

    # navigate to battery in circle
    myRobot.turn(-64, 20)
    myRobot.move(42, 50)

    # put arm down to collect rechargable battery
    myRobot.turn_right_arm(50, 40)
    myRobot.move(4.5, 30)
    myRobot.turn(106, 20)
    myRobot.move(-1.5, 10)    #align

    # move to wind turbine
    myRobot.move(40, 60)
    for i in range(2):
        myRobot.move(-7, 20)
        myRobot.move(14, 40)
    # done with windmill mission

    # drive to hybrid car
    myRobot.move(-28, 55)
    wait_for_seconds(0.5)# a small pause allow the robot to come to a complete stop
    myRobot.turn(-91, 20)
    myRobot.move(33, 40)
    wait_for_seconds(0.7)
    myRobot.turn(6, 40)
    wait_for_seconds(0.5)

    # lift car lever up
    myRobot.turn_right_arm(-50, 100)
    myRobot.turn_right_arm(50, 100)
    myRobot.turn(-5, 30)

    # navigate to final mission (Power Plant)
    myRobot.move(-8, 40)
    myRobot.turn(-90, 20)
    myRobot.move(52, 60)
    wait_for_seconds(0.5)
    myRobot.turn(-45, 20)

    myRobot.move(-40, 40)   # align
    
    # lower arm for mission
    myRobot.turn_left_arm(degree = -100, speed = 50)
 
    # move to mission
    myRobot.move(55, 40)
    
    # lift side bar up
    myRobot.turn(-5, 20)
    myRobot.turn_left_arm(degree = 45, speed = 70)

    # push middle bar down
    myRobot.turn(20, 30)
    myRobot.move(-3, 30)
    myRobot.turn_left_arm(degree = -55, speed = 90)

    # go to site B
    myRobot.move(-7, 40)
    myRobot.turn(60, 40)
    myRobot.move(90, 100)

    # raise the right arm; prepare for run 2
    myRobot.right_arm_stop_action('brake')
    myRobot.turn_right_arm(-45, 80)

'''
Run 2 attempts the following missions:
    M02: Oil Platform
    M03: Energy Storage
    M11: Hydroelectric Dam
'''
def run_2():
    myRobot.right_arm_stop_action('brake')
    myRobot.turn_right_arm(-1, 50)
    myRobot.move(-5, 80)
    myRobot.move(20, 60)
    myRobot.turn(35, 50)
    myRobot.move(64, 50)
    myRobot.turn(55, 40)
    myRobot.move(-15, 50)
    myRobot.move(7, 70)
    myRobot.move(-8, 55)
    myRobot.move(7, 70)
    myRobot.move(-8, 55)
    myRobot.move(6, 70)
    myRobot.turn(-99, 40)
    myRobot.move(4, 40)
    myRobot.turn_right_arm(45, 60)
    myRobot.move(-7, 70)
    myRobot.turn(-16, 30)
    myRobot.move(-21, 90)
    myRobot.turn(50, 40)
    myRobot.move(-60, 90)

'''
Run 3 attempts the following missions:
    M04: Solar Farm
    M05: Smart Grid (hand)
    M01: Innovation Project Model
'''
def run_3():
    myRobot.move(-5, 80)
    myRobot.move(17, 60)
    myRobot.turn(33, 50)
    myRobot.move(75, 50)
    myRobot.turn(65, 50)
    myRobot.move(30, 60)
    #works so far

    myRobot.turn(58, 40)
    myRobot.turn_left_arm(-72, 60)
    myRobot.move(6, 40)
    myRobot.turn(-56, 20)
    wait_for_seconds(0.5)

    myRobot.turn(95, 30)
    myRobot.move(36, 45)

'''
Select Run to execute
'''
run_1()
#run_2()
#run_3()
