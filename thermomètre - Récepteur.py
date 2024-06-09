from microbit import *
import radio

radio.on()
print()
print()
print()
print()
print()
print()
print("Thermomètre à micro:bit")
print()

while True:
    message = radio.receive()
    if message != None:
        print(message)
