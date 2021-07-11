# Alien Hand Cricket
# By : Sankhojyoti Halder

import random

# USELESS INTRODUCTION
print("$$#HJ456in&&*$!@`~ *GVy()*Blml")
print("Some weird language appeared today...")
a = input("type e and hit enter to encrypt in into english: ")
while True:
    if a == "e":
        print("31.9.2018. \n galaxy.milky_way() / region.sun_class() \n planet.earth() \n resident_alien.homo sepiense \n status.commensing challange")
        print("we challenge you earthlings to a hands cricket match..your time..your place..your format..we'll be there")
        break
    else:
        print("this is really important to save humanity")

# RULES
print("Here are the rules.... \n you choose a number between 1 to 6.. i chose one too... \n no.1: If our numbers are same, the square of that number is added to the total(This is known as POWER HIT) \n no.2: If your and my numbers have a difference of 1, then the batsman is declared out \n no.3: In any other cases, The batsman's number is added to the total. That's all!")

# required variables. functions of balls, runs_player and runs_ai are self explanetory. 'spam' is used to check if team batiing second has won.
balls = 0
spam = 0
runs_player = 0
runs_ai = 0

# Taking the Number of overs
overs = int(input("Select number of overs: "))

# Implementaion of the tos..with random selction from the PC
print("It's time for the toss... The captains are ready \n It's your Call.!!")
toss_choice = input("What do you choose,Cap ? \n type (head or tail): ")
toss_outcome = random.choice(["head", "tail"])
print("And...the coin says ", toss_outcome)
# Deciding to bat or bowl first
if toss_outcome == toss_choice:
    decision = input("You won the toss \n but i'll still win and rule your planet \n what you wanna do ? type(bat or bowl): ")
else:
    decision1 = random.choice(["bat", "bowl"])
    print("Huh..I win the toss.. \n morning shows the day \n and I choose to ", decision1, "first")
    if decision1 == "bat":
        decision = "bowl"
    else:
        decision = "bat"

# Commensing 1st innings
if decision == "bat":
    print("The homo sepienses are coming out to bat first....  \n ******** \n     ")
    while spam == 0 and balls <= (overs * 6):
        player = int(input("Enter your number of choice: "))
        if player % 1 == 0 and player <= 6:
            random1 = random.randint(1, 6)
            if player == random1:
                runs_player += player ** 2
                balls += 1
                print("CRAP!!.. you got the Power Hit")
                print("Your current score is ", runs_player, "(not out)", " in ", (balls // 6), ".", (balls % 6), " overs")
            elif player - random1 == 1 or random1 - player == 1:
                balls += 1
                print("OUT!! You are dismissed! \n ... better luck next time")
                print("Your current score is ", runs_player, " in ", (balls // 6), ".", (balls % 6), " overs")
                break
            else:
                runs_player += player
                balls += 1
                print("Your current score is ", runs_player, "(not out)", " in ", (balls // 6), ".", (balls % 6), " overs")
        else:
            print("Enter a valid number..or i'll smash your head right now")

    print("you're done? at such a low score..?? Haha .. you made my win easy!! \n    ")
    print("It's the aliens getting their hands ready to chase the total... \n after all..it's hand cricket!! ")

    spam = 0
    balls = 0

# Commensing 2nd innings. We have to keep in mind to check the victory of AI after every ball
    while spam == 0 and balls <= (overs * 6):
        player = int(input("Enter your number of choice: "))
        if player % 1 == 0 and player <= 6:
            random1 = random.randint(1, 6)
            if player == random1:
                runs_ai += player ** 2
                balls += 1
                print("NICE!!.. I got the Power Hit")
                print("i chose ", random1, "too")
                print("My current score is ", runs_ai, "(not out)", " in ", (balls // 6), ".", (balls % 6), " overs")
                if runs_ai > runs_player:
                    break
            elif player - random1 == 1 or random1 - player == 1:
                balls += 1
                print("OUT!! I am dismissed! \n ... NOOOOOOOO")
                print("i chose", random1)
                print("Your current score is ", runs_ai, " in ", (balls // 6), ".", (balls % 6), " overs")
                break
            else:
                runs_ai += random1
                balls += 1
                print("i chose", random1)
                print("My current score is ", runs_ai, "(not out)", " in ", (balls // 6), ".", (balls % 6), " overs")
                if runs_ai > runs_player:
                    break
        else:
            print("Enter a valid number..or i'll smash your head right now")
    if runs_ai > runs_player:
        print("HAHAHA.It was an easy win earthlings \n ********* ")
    elif runs_ai < runs_player:
        print("YOU WON?!?!! how is this even possible..?")
    else:
        print("DAMN! It's a tie..!!")
# Commensing 1st Innings
else:
    print("It's the aliens getting their hands ready to bat.. \n . after all..it's hand cricket!! ")
    while spam == 0 and balls <= (overs * 6):
        player = int(input("Enter your number of choice: "))
        if player % 1 == 0 and player <= 6:
            random1 = random.randint(1, 6)
            if player == random1:
                runs_ai += player ** 2
                balls += 1
                print("NICE!!.. I got the Power Hit")
                print("I chose ", random1, "too")
                print("Your current score is ", runs_ai, "(not out)", " in ", (balls // 6), ".", (balls % 6), " overs")
            elif player - random1 == 1 or random1 - player == 1:
                balls += 1
                print("OUT!! I am dismissed! \n ... NOOOO")
                print("I chose ", random1,)
                print("Your current score is ", runs_ai, " in ", (balls // 6), ".", (balls % 6), " overs")
                break
            else:
                runs_ai += random1
                balls += 1
                print("I chose ", random1,)
                print("Your current score is ", runs_ai, "(not out)", " in ", (balls // 6), ".", (balls % 6), " overs")
        else:
            print("Enter a valid number..or i'll smash your head right now")
    print("CHASE THAT!! You'll be gone first ball.. \n    ")
    print("The homo sepienses are coming out to bat and chase the target down .... \n ******** \n     ")
    print("THE TARGET IS: ", runs_ai + 1)
    spam = 0
    balls = 0

# Commensing 2nd innings. We have to keep in mind to check the victory of player after every ball
    while spam == 0 and balls <= (overs * 6):
        player = int(input("Enter your number of choice: "))
        if player % 1 == 0 and player <= 6:
            random1 = random.randint(1, 6)
            if player == random1:
                runs_player += player ** 2
                balls += 1
                print("DAMN!!.. You got the Power Hit")
                print("i chose ", random1, "too")
                print("Your current score is ", runs_player, "(not out)", " in ", (balls // 6), ".", (balls % 6), " overs")
                if runs_player > runs_ai:
                    break
            elif player - random1 == 1 or random1 - player == 1:
                balls += 1
                print("OUT!! You are dismissed! \n ... YESSSS")
                print("i chose", random1)
                print("Your current score is ", runs_player, " in ", (balls // 6), ".", (balls % 6), " overs")
                break
            else:
                runs_player += random1
                balls += 1
                print("i chose", random1)
                print("YOur current score is ", runs_player, "(not out)", " in ", (balls // 6), ".", (balls % 6), " overs")
                if runs_player > runs_ai:
                    break
        else:
            print("Enter a valid number..or i'll smash your head right now")
    if runs_ai > runs_player:
        print("HAHAHA.It was an easy win earthlings \n ********* ")
    elif runs_ai < runs_player:
        print("You Won?!?!?how is this even possible..?")
    else:
        print("DAMN! It's a tie..!!")
