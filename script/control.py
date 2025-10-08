from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

import sub

hub = PrimeHub()
hub.system.set_stop_button(Button.CENTER)

while True:
    buttons_pressed = hub.buttons.pressed()
    sub.perform_button_action(hub, buttons_pressed=buttons_pressed)

