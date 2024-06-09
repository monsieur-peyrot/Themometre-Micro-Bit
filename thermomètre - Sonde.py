from microbit import *
import radio

radio.on()

while True:
    mesure = 0
    N = 100
    for i in range(N):
        lecture = pin1.read_analog()
        mesure += lecture
    resultat = int(mesure / N)
    resultat = int(resultat / 1.2)
    temperature = int(A * resultat + B)
    message = "Température : " + str(temperature) + "°C"
    print(message)
    radio.send(message)
    display.show(Image.HAPPY)
    sleep(100)
    display.clear()
    sleep(4900)
