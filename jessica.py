# defining functions for later use in the program

def dayavg(suglvl1, suglvl2, suglvl3):
    return (suglvl1 + suglvl2 + suglvl3) / 3


# defining the variables used later in the program

Suglvl1 = int(input(print('Enter first blood sugar level reading.')))

Suglvl2 = int(input(print('Enter second blood sugar level reading')))

Suglvl3 = int(input(print('Enter third blood sugar level reading')))
dailyAvg = dayavg(Suglvl1, Suglvl2, Suglvl3)
low = int(80)
high = int(150)

# program body starts here

while True:
    if dailyAvg <= low:
        print("Jessica, your daily average blood sugar of ", int(dailyAvg), ", is lower than normal!")
        input(print("press enter to exit"))
        break

    elif dailyAvg < high:
        print("Jessica, your daily average blood sugar level of ", int(dailyAvg), ", is within normal ranges.")
        input(print("press enter to exit"))
        break
    else:
        print("Jessica, your daily average blood sugar level of", int(dailyAvg), ", is higher than normal!")
        print("")
        print("")
        input(print("press enter to exit"))
        break
