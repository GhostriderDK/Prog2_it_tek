from gpiozero import MotionSensor
from gpiozero import LED
from time import sleep

pir = MotionSensor(4)
led = LED(27)

while True:
    pir.wait_for_motion()
    led.on()
    sleep(5)
    led.off()