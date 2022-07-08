#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
lm = Motor(Port.C)
rm = Motor(Port.B)
ultra = UltrasonicSensor(Port.S1)
touch = TouchSensor(Port.S2)

def move(speed = 900, dir = "forward"):
    if dir == "forward":
        lm.run(900)
        rm.run(900)
    if dir == "backward":
        lm.run(-900)
        rm.run(-900)
    if dir == "left":
        lm.run(-900)
        rm.run(900)
    if dir == "right":
        lm.run(900)
        rm.run(-900)
while 1:
    if touch.pressed():
        move(speed = 1020, dir = "forward")
    if ultra.distance() <=200:
        lm.run_angle(900, 180)
        rm.run_angle(-900, 180)
        move(speed = 1020, dir = "forward")
    if Button.CENTER in ev3.buttons.pressed():
        lm.stop()
        rm.stop()
