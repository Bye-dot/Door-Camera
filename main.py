from machine import Pin
from time import sleep

print("hello world")
print("This is a test")

led_pin = Pin(2, Pin.OUT)

while True:
    led_pin.value(1)  # Turn the pin on
    sleep(1)      # Wait for 1 second
    led_pin.value(0)  # Turn the pin off
    sleep(1)      # Wait for 1 second