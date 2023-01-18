from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *
from spike import Motor
from spike import MotorPair
import sys
import math 
import hub

########################################
# settings
########################################
wheel_diameter = 5.6
distance_between_wheels = 9.71

motor_pair = MotorPair('A', 'B')
# Set the default speed of the motor_pair
motor_left = Motor('A')
motor_right = Motor('B')
motor_pair.set_default_speed(20) 
# Set the distance that the robot travels for one rotation of its wheels
motor_pair.set_motor_rotation(wheel_diameter * math.pi, 'cm')
motor_front = Motor('C')
motor_back = Motor('D')

motor_front_async = hub.port.C.motor
#color_sensor = ColorSensor('E')
hub = PrimeHub()

########################################
# functions
########################################
def angleToDistance(degree):
    factor = 1.02
    return distance_between_wheels * math.pi * degree / 360.0 * factor

def get_distance():
    factor = 1.2
    left_rotation_degree = -motor_left.get_degrees_counted()
    right_rotation_degree = motor_right.get_degrees_counted()
    average_rotation_degree = (left_rotation_degree + right_rotation_degree) / 2.0
    distance = wheel_diameter * factor * math.pi * average_rotation_degree / 360.0

    return distance

def reset_lr_motor_degree_count():
    motor_left.set_degrees_counted(0)
    motor_right.set_degrees_counted(0)   

# speed is always positive
# negative distance is backward
def move_pid(distance, speed = 50):
    reset_lr_motor_degree_count()
    hub.motion_sensor.reset_yaw_angle()

    # get direction
    isForward = distance > 0
    distance = abs(distance)
    speed = abs(speed)
    sign = -1
    if not isForward:
        speed = -speed
        sign = 1

    motor_pair.set_stop_action('hold')

    wP = 5
    wI = 0.01
    wD = 0.01
    while (abs(get_distance()) < distance):
        dP = hub.motion_sensor.get_yaw_angle()
        steering = sign * int(dP * wP)

        motor_pair.start(steering=steering, speed=speed)
        
        print("dist={0}, yaw={1}, steering={2}, {3}".format(get_distance(), dP, steering, speed))
    motor_pair.stop()
 
def turn(degree, speed = 40):
    motor_pair.move(angleToDistance(degree), 'cm', steering=100, speed=speed)

########################################
# Mission 1
########################################
def mission_1():
    for i in range(2):
        #positive is clockwise
        #steering always 100(turn in place) 
        #speed is from 0-100
        turn(90,50) 
        
########################################
# Mission 2
########################################
def mission_2():
    for i in range(4):
        move_pid(20, 40)
        turn(90, 25)

########################################
# Mission 3
########################################
def mission_3():
    for i in range(2):
        move_pid(120, 40)
        move_pid(-120, 40)
        


########################################
# Mission Hammer
########################################
def mission_hammer():
    #left wheel at 12
    move_pid(65)

    turn(-90, speed=20)
    move_pid(7)
    move_pid(-10)
    
    angle = 150
    motor_front.run_for_degrees(-angle, 100)
    motor_front.run_for_degrees(angle, 100)

    move_pid(-2)
    turn(82)
    move_pid(47)
    turn(-125, speed=25)

    move_pid(9)
    move_pid(-13)

    motor_front.run_for_degrees(-angle, 100)
    motor_front.run_for_degrees(angle, 100)

    turn(-34)
    move_pid(120, 90)


########################################
# Color Sensor
########################################

#black is 35%
cs_black = 35
#white is 99%
cs_white = 100

#def lineFollow(distance = 120, spd = 25, stop_action = 'coast'):
def lineFollow(dist_spd_list):
    # brake, hold, coast
    motor_pair.set_stop_action('coast')

    for i in range(5):
        print("============================================================")
    
    wP = 0.3
    wI = 0
    wD = 0

    dI = 0
    prev_dP = 0

    steering = 0
    threshold = 10
    cs_mid = (cs_black + cs_white) / 2.0


    for pair in dist_spd_list:
        dist = pair[0]
        spd = pair[1]
        
        #reset distance count
        reset_lr_motor_degree_count()

        while (dist > get_distance()):
            cs_here = color_sensor.get_reflected_light()

            dP = cs_here - cs_mid
            dI += dP
            dD = dP - prev_dP

            delta = dP * wP + dI * wI + dD * wD

            if abs(delta) < 5:
                delta = 0

            powerL = int(spd - delta)
            powerR = int(spd + delta)

  #          print("cs_here={0}, P={1}, I={2}, D={3} powerL={4}, powerR={5}".format(cs_here, dP * wP, dI * wI, dD * wD, powerL, powerR))
            motor_pair.start_tank_at_power(powerL, powerR)
    
            prev_dP = dP

        print("dist={0}, get_distance={1}, speed={2}".format(dist, get_distance(), spd))

    motor_pair.stop()

#######################################
# Bridge Mission
#######################################
def bridge_mission():
    #move_pid(10, 30)
    #lineFollow([(26, 40), (15, 20), (66, 40)])
    lineFollow([(30, 40)])
    motor_front.run_for_degrees(120)
    motor_front.run_for_degrees(-120)
    
    #finishes bridge
    #move_pid(2, 25)
    motor_spinny.run_for_degrees(90)
    turn(-90, 20)
    move_pid(33, 60)
    move_pid(-8, 90)

    #done with load cargo

    turn(-90, 25)
    motor_spinny.run_for_degrees(-90)
    move_pid(-35, 20)
    motor_spinny.run_for_degrees(90)
    move_pid(-25, 40)

    #lineFollow([(15, 20), (61, 60)])
    #move_pid(-5,30)
    #turn(-100)
    #move_pid(-15,40)
    #move_pid(-50,40)
    #motor_front.run_for_degrees(10)

# moving back
# move_pid(-70, 60)
# turn(20, 50)
# move_pid(-100, 90)


#turn(410, 70)


#######################################
# Load Cargo
########################################
def helicopter_run():
    #9 tiles to the right
    move_pid(90,70)
    move_pid(15.5,40)
    turn(90,20)
    move_pid(8,20)
    motor_front.run_for_degrees(270, 40)
    #starting cargo
    move_pid(-6,20)
    turn(-42,20)
    move_pid(-28,25)
    motor_back.run_for_degrees(131,50)
    motor_back.run_for_degrees(-12,50)
     #starting push cargo in green circle
    turn(20,20)
    move_pid(25,30)

    #starting push the blue box off
    motor_back.run_for_degrees(-119,50)
    move_pid(-13,30)
    turn(-25,20)
    move_pid(-77,50)
    #reset
    motor_front.run_for_degrees(-180, 45)

    #motor_front.run_for_degrees(-180, 60)


def run_final():
    move_pid(-10,30)
    turn(-55,20)
    move_pid(48,30)
    motor_front.run_for_degrees(-60, 20)

 
#######################################
#Platoon Mission Demo
#######################################
def innovation_platoon(distance = 100, speed = 20):
    # resets the estimated driven distance and angle to 0
    reset_lr_motor_degree_count()
    hub.motion_sensor.reset_yaw_angle()
    traveled_distance = abs(get_distance())
    print("started distance={} travelled={}".format(distance, traveled_distance))
    while (traveled_distance < distance):
        dist_left = distance_left.get_distance_cm()
        dist_right = distance_right.get_distance_cm()
        if (dist_left is None or dist_right is None):
            continue
        lr_diff = dist_left - dist_right
        avg_diff = (dist_left + dist_right)/2
        # let's keep avg_diff within 10 cm
        dspeed = speed
        if (avg_diff > 20):
            dspeed = int( speed * (1 + avg_diff/20) )
        else:
            dspeed = int( speed * (1 - avg_diff/20) )
        dsteer = int( ( lr_diff / max(dist_left, dist_right) ) * 90)
        motor_pair.move(amount=5, unit='cm', steering = dsteer, speed = dspeed)
        traveled_distance = abs(get_distance())
        print("dist_left={} dist_right={} lr_diff={} avg_diff={} dspeed={} dsteer={} traveled={}".format(dist_left,dist_right,lr_diff,avg_diff,dspeed,dsteer,traveled_distance))

def getTurnDir(ld, rd):
    if (ld - rd > 10):
        return 1
    elif (ld - rd ):
        return -1

def last_run():
    #jig on 7
    move_pid(75,40)
    turn(45,15)
    move_pid(64,35)
    turn(-90,15)
    move_pid(18,20)
    move_pid(-5,25)
    motor_front.run_for_degrees(180,25)
    move_pid(11,25)
    move_pid(-15,30)
    #next
    turn(-45,25)
    move_pid(48,30)
    turn(-45,25)
    move_pid(5,5)
        

def test_thread():
    thread.start_new_thread(move_pid(100,30))
    thread.start_new_thread(motor_front.run_for_degrees(100,5))


def innovation_platoon1():
    distance_left.light_up_all()
    distance_right.light_up_all()
    motor_left.set_default_speed(-50)
    motor_right.set_default_speed(50)
    while True:
        distance_left.wait_for_distance_farther_than(10, 'cm')
        motor_left.start()
        motor_right.start()
        
        distance_left.wait_for_distance_closer_than(10, 'cm')
        motor_left.stop()
        motor_right.stop()

        turnDir = getTurnDir(distance_left.get_distance_cm(), distance_right.get_distance_cm())

        if (turnDir > 0):
            motor_left.set_default_speed(-50)
            motor_right.set_default_speed(50)


        # distance_right.wait_for_distance_farther_than(10, 'cm')
        # motor_right.start()

        # distance_right.wait_for_distance_closer_than(10, 'cm')
        # motor_right.stop()

def run_catapult():
    motor_front.run_for_degrees(-90,100)

         
########################################
#mission_2()
#mission_hammer()
#bridge_mission()

#move_pid(-30, 20)
#move_pid(-8, 90)
#move_pid(30, 45)
#innovation_platoon(distance = 100, speed = 20)
#innovation_platoon1()

#9 tiles right
#helicopter_run()
#left wheel on 11
#mission_hammer()
#jig
#last_run()

#mission_hammer()
#test_thread()
# raise SystemExit

def asyncMove():
    
  #  motor_front.run_for_degrees(-360,40)
    motor_front_async.run_for_degrees(-360,20)
    move_pid(20, 20)

    return

asyncMove()
raise SystemExit
