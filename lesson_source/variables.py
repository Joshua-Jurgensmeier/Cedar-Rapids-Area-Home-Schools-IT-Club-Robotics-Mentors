#!/usr/bin/env python3
from ev3dev.motor import *
from time import sleep
left = LargeMotor('outA')
right = LargeMotor('outB')


# Integer variable
x = 49
y = 70
z = x
t = 3

# Boolean variable
robots_are_cool = True

i_like_robots = robots_are_cool

# Using variables
left.on(y)
right.on(z)
sleep(t)