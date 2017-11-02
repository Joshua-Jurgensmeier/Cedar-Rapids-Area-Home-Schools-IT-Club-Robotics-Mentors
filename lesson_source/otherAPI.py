#!/usr/bin/env python3
from ev3dev.motor import *
from time import sleep
left = LargeMotor('outA')
right = LargeMotor('outB')

left.on(100)
right.on(100)
sleep(3)

# right.on(-100)
# sleep(3)
# left.on(-100)
# sleep(3)