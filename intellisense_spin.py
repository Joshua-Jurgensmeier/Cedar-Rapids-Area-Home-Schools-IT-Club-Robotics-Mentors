#!/usr/bin/env python3

import ev3dev.ev3 as ev3

right_motor = ev3.LargeMotor('outC')
left_motor = ev3.LargeMotor('outB')

right_motor.run_timed(time_sp=3000, stop_action='coast', speed_sp=500)
left_motor.run_timed(time_sp=3000, stop_action='coast', speed_sp=-500)

left_motor.wait_while('running')
