#
print('Welcome to Camel!')
print('You have stolen a camel to make your way across the Mobi desert.')
print('The natives want their camel back and are chasing you down! Survive your desert trek and out run the natives.')

#Values
done = False
distance = 0
thirst = 0
fatigue = 0
drinks = 3
nativdist = -20
thirstmsg1 = "You are starting to feel dehydrated."
thirstmsg2 = "You are feeling very ill. Find water now."
tiremsg1 = "Your camel is getting tired."
tiremsg2 = "Your camel struggles to continue. Find rest now."
from random import randint
nativtrav = randint(5, 15)

#Main game
while done == False:
    if thirst == 7:
        print("You've died of thirst.")
        done = True
        break
    if fatigue > 8:
        print("Your camel collapses and stops moving.")
        print("The natives will find you soon, but with no camel to return.")
        done = True
        break
    if nativdist >= 0:
        print("You've been found by the natives.")
        done = True
        break
    if distance >= 200 and not thirst == 7 and not fatigue > 8:
        print("You've successfully crossed the border with your camel.")
        done = True
        break
    print('A. Drink from your canteen.\nB. Ahead moderate speed.\nC. Ahead full speed.\nD. Stop for the night.\nE. Status check.\nQ. Quit.')
    nextac = raw_input('What do you choose to do? ')

    #Quit
    if nextac.upper() == "Q":
        done = True

    #Status check
    elif nextac.upper() == "E":
        print('Miles traveled: ' + str(distance))
        print('Drinks in canteen: ' + str(drinks))
        print('The natives are ' + str(nativdist) + ' miles behind you.')
        if thirst >= 4 and thirst < 6:
            print(thirstmsg1)
        if thirst == 6:
            print(thirstmsg2)
        if fatigue >= 5 and fatigue < 8:
            print(tiremsg1)
        if fatigue == 8:
            print(tiremsg2)
        cont = raw_input('Press G to continue. ')
        if cont.upper() in ["G"]:
            continue

    #Rest
    elif nextac.upper() == "D":
        fatigue = 0
        print('Your camel is no longer fatigued, but the natives still persist.')
        from random import randint
        nativdist = nativdist + nativtrav
        cont = raw_input('Press G to continue. ')
        if cont.upper() in ["G"]:
            continue

    #Fast travel
    elif nextac.upper() == "C":
        from random import randint
        milegain = randint(12, 20) - fatigue
        distance = distance + milegain
        if milegain <= 12:
            print('Your travel was arduous.\nYou traveled ' + str(milegain) + ' miles.')
        elif milegain >= 16:
            print('You' + "'" + 've traveled with great ease.\nYou traveled ' + str(milegain) + ' miles.')
        else:
            print('You traveled ' + str(milegain) + ' miles.')
        thirst = thirst + 1
        fatigue = fatigue + randint(1, 3)
        nativdist = nativdist + nativtrav - milegain
        oasis = randint(1, 20)
        if oasis == 20 and not nativdist >= 0:
            print("You've found an oasis.")
            print("Your canteen has been refilled.\nYour camel is rested.\nYou drink from the oasis.")
            drinks = 3
            fatigue = 0
            thirst = 0
        if thirst >= 4 and thirst < 6:
            print(thirstmsg1)
        if thirst == 6:
            print(thirstmsg2)
        if fatigue >= 5 and fatigue < 8:
            print(tiremsg1)
        if fatigue == 8:
            print(tiremsg2)        
        cont = raw_input('Press G to continue. ')
        if cont.upper() in ["G"]:
            continue

    #Slow travel
    elif nextac.upper() == "B":
        from random import randint
        milegain = randint(3, 11) - (fatigue / 2)
        if milegain < 1:
            milegain = 1
        distance = distance + milegain
        if milegain <= 3:
            print('Your travel was difficult, but taken slowly.\nYou traveled ' + str(milegain) + ' miles.')
        elif milegain >= 8:
            print('Even at a slowed pace, good progress had been made.\nYou traveled ' + str(milegain) + ' miles.')
        else:
            print('You traveled ' + str(milegain) + ' miles.')
        thirst = thirst + 1
        fatigue = fatigue + 1
        nativdist = nativdist + nativtrav - milegain
        oasis = randint(1, 30)
        if oasis == 30 and not nativdist >= 0:
            print("You've found an oasis.")
            print("Your canteen has been refilled.\nYour camel is rested.\nYou drink from the oasis.")
            drinks = 3
            fatigue = 0
            thirst = 0        
        if thirst >= 4 and thirst < 6:
            print(thirstmsg1)
        if thirst == 6:
            print(thirstmsg2)
        if fatigue >= 5 and fatigue < 8:
            print(tiremsg1)
        if fatigue == 8:
            print(tiremsg2)        
        cont = raw_input('Press G to continue. ')
        if cont.upper() in ["G"]:
            continue

    #Drink
    elif nextac.upper() == "A":
        if drinks != 0:
            print("You take a drink from your canteen.")
            drinks = drinks - 1
            thirst = 0
        if drinks == 0:
            print("You have no water left.")
        cont = raw_input('Press G to continue. ')
        if cont.upper() in ["G"]:
            continue