#!/usr/bin/env pybricks-micropython
import fll_briarcliff6pack
my_robot = fll_briarcliff6pack.Bri6Pack()

# initializing 6 sec

# run time 13 sec
import R1_basketball    
my_robot.reset_motors()
my_robot.count_down(8)

# run time 9.5 sec
import R2_bench 
my_robot.reset_motors()
my_robot.count_down(8)

# run time 6 sec
import R4_slide 
my_robot.reset_motors()
my_robot.count_down(18)

# run time  sec
import R5_final_run 
my_robot.say("I will not fall")
my_robot.say("Briarcliff Six Pack Rocks")