from machine import Pin
import utime
class Ultrasonic:
    def __init__(self):
        self.__pumpPin = Pin(14, Pin.OUT)
        self.__triggerPin = Pin(2, Pin.OUT)
        self.__echoPin = Pin(3, Pin.IN)

    def getDistance(self):
        self.__triggerPin.low()
        utime.sleep_us(5)
        self.__triggerPin.high()
        utime.sleep_us(10)
        self.__triggerPin.low()

        while self.__echoPin.value() == 0:
            signaloff = utime.ticks_us()

        while self.__echoPin.value() == 1:
            signalon = utime.ticks_us()

        totalTime = signalon - signaloff

        # Calculate distance in centimeters
        distance = (totalTime * 0.0343) / 2

        print("Distance: " + str(distance) + " CM")

        return distance
    
    def _getPumpPin(self):
        return self.__pumpPin

    def _setPumpPin(self, value):
        self.__pumpPin.value(value)
        
    def _getTriggerPin(self):
        return self.__triggerPin

    def _setTriggerPin(self, value):
        self.__triggerPin.value(value)

    def _getEchoPin(self):
        return self.__echoPin

    def _setEchoPin(self, value):
        self.__echoPin.value(value)