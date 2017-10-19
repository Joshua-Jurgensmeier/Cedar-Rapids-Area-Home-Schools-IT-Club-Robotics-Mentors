#!/usr/bin/env python3
import ev3dev.ev3 as ev3

# Motor setup
left_motor = ev3.LargeMotor('outA')
right_motor = ev3.LargeMotor('outB')

# Motor commands
left_motor.run_timed(speed_sp=9000, time_sp=3000, stop_action="coast")
right_motor.run_timed(speed_sp=9000, time_sp=3000, stop_action="coast")
left_motor.wait_while("running")
