#!/usr/bin/env python3
# The above shebang allows the program to be run from the robot interface

# Say hello and then spin in circles.

from time import sleep

# The ev3dev Python library
from ev3dev.ev3 import *

#                     the output port
# Setup motors             V
left_motor = LargeMotor('outB')
right_motor = LargeMotor('outC')


# A text to speech method from the ev3dev Python library

Sound.speak('Hello World!').wait()

#        keyword argument for speed set point (-1000-1000)
#                           V
left_motor.run_forever(speed_sp=1000)
right_motor.run_forever(speed_sp=-1000)

sleep(3)

left_motor.stop(stop_action="coast")
right_motor.stop() # Uses the value set by the previous call to stop.
