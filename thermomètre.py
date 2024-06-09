from microbit import *

print()
print()
print()
print("Appuyez sur le bouton A pour faire une mesure de température")
print()

while True:
    display.clear()
    if button_a.is_pressed():
        display.show("M")
        print()
        mesure = 0
        N = 1000
        for i in range(N):
            lecture = pin1.read_analog()
            mesure += lecture
        resultat = int(mesure / N)
        temperature = int(-1.70 * resultat + 1010)
        print("Température =", temperature)
        print()
        while button_a.is_pressed():
            pass
