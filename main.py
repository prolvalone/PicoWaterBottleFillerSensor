from machine import Pin
import utime
from ultrasonic import Ultrasonic

while True:
    utime.sleep(.3)
    u1 = Ultrasonic()

    if u1.getDistance() < 10:
        u1._setPumpPin(True)
    else:
        u1._setPumpPin(False)
