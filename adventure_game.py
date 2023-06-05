import time
import random


def print_pause(print_the_message):
    print(print_the_message)
    time.sleep(2)


def intro(rumor, option):
    print_pause("You find yourself standing in the bus station,"
                "all alone.\n")
    print_pause("The neighborhood you are standing at has " + rumor + " around "
                "as for that there is no much people at this time 8:00 PM \n")
    print_pause("There is somone wearing red coat just across the street.\n")
    print_pause("you tride to see the person face but he/she is giving you his/her back \n")



def move(rumor, option):
    if "person" in rumor:
        print_pause("\nYou took a glance to this person")
        print_pause("\nYou've been curious, and started to think"
                    " could it be what you think of or you are just overthinking"
                    )
        print_pause("\nThe bus has arrived and you took it to go home.\n")
    else:
        print_pause("\nAlthough you descide to stay in your place but you got curiouse so you decided to walk out of the station")
        print_pause("\nwhile you were walking, the person took steps further from you")
        print_pause("\nyou stopped once you noticed the move ")
        print_pause("\nYou heard a soft voice whispering")
        print_pause("\nDon't try to come near, it is not good to you ")
        print_pause("\nSo you went back to the station in fear\n")
        
        play_again()
   


def check(rumor, option):
    print_pause("\nYou went close to the person to check.")
    print_pause("\nWhile you were walking it started to" + option + "")
    print_pause("\nThe " + option + " slowed your walking as it started heavy\n")
   
    while True:
        choice2 = input("Would you like to (s) shout out or (t) "
                        "turn back?")
        if choice2 == "s":
            if "s" in choice2:
                print_pause("\nwhile it kept " + option + " you shouted out loud HELLO! "
                            "do you need any help?")
                print_pause("\nThe person turned out to you "
                            "without talking" )
                print_pause("\nBut the " + option + "slowly become lighter"
                            "so you kept on moving toward him/her")
                print_pause("\nYou reach where he'she was standing but " + option +
                            ". started to pour heavy again that your scream wasn't heard at all\n")
            
        if choice2 == "t":
            print_pause("\nYou tride to shout before turning back")
            print_pause("\nbut your your voice wasn't hearable beacuse of" + option + ".")
            print_pause("\nYou Regret it later as you find out just before the bus move it is a pregnant women that was in pain")
        play_again()

            


def scenario(rumor, option):
    print_pause("Statemnt 1 to check")
    print_pause("Statemnt 2 to wait for the bus")
    print_pause("What is your decision?")
    while True:
        choice1 = input("(Please enter 1 or 2.)\n")
        if choice1 == "1":
            check(rumor, option)
            break
        elif choice1 == "2":
            move(rumor, option)
            break


def play_again():
    again = input("Would you like to play again? (y/n)").lower()
    if again == "y":
        print_pause("\n\n\nOkay! Restarting the game ...\n\n\n")
        play_game()
    elif again == "n":
        print_pause("\n\n\nThanks for playing!.\n\n\n")
    else:
        play_again()


def play_game():
    rumor = "Ghost"
    option = random.choice(["Snowing", "Raining"])
    intro(rumor, option)
    scenario(rumor, option)


play_game()