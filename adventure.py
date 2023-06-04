import time
import random


def print_pause(msg_to_print):
    print(msg_to_print)
    time.sleep(2)


def intro(item, option):
    print_pause("You find yourself standing in an open field, filled "
                "with grass and white wildflowers.\n")
    print_pause("Rumor has it that a " + option + " is somewhere around "
                "here, and it has been terrifying the neighborhood.\n")
    print_pause("In front of you is a house.\n")
    print_pause("To your right is a forest.\n")
    print_pause("In your hand you hold your ( not very "
                "effective) blade.\n")


def cave(item, option):
    if "sward" in item:
        print_pause("\nYou look cautiously into the forest.")
        print_pause("\nYou've been here before, and gotten all"
                    " the good food. It's just a tree full forest"
                    " now.")
        print_pause("\nYou walk back to the field.\n")
    else:
        print_pause("\nYou look cautiously into the forest.")
        print_pause("\nIt turns out to be only a very small garden.")
        print_pause("\nYour eye catches a glint of metal behind a "
                    "rock.")
        print_pause("\nYou have found a magical Sword!")
        print_pause("\nYou discard your old blade and take "
                    "the sword with you.")
        print_pause("\nYou walk back out to the field.\n")
        item.append("sward")
    field(item, option)


def house(item, option):
    print_pause("\nYou approach the door of the house.")
    print_pause("\nYou are about to knock when the door "
                "opens and out steps a " + option + ".")
    print_pause("\nyep! This is the " + option + "'s house!")
    print_pause("\nThe " + option + " attacks you!\n")
    if "sward" not in item:
        print_pause("You feel a bit unprepared for this, "
                    " with only having a tiny blade.\n")
    while True:
        choice2 = input("Would you like to (1) fight or (2) "
                        "run away?")
        if choice2 == "1":
            if "sward" in item:
                print_pause("\nAs the " + option + " moves to attack, "
                            "you pull out your new sword.")
                print_pause("\nThe Sword shines brightly in "
                            "your hand as you brace yourself for the "
                            "attack.")
                print_pause("\nBut the " + option + "takes one look at "
                            "your shiny sword and runs away!")
                print_pause("\nYou have rid the town of the " + option +
                            ". You are victorious!\n")
            else:
                print_pause("\nYou do your best...")
                print_pause("but your blade is no match for the "
                            + option + ".")
                print_pause("\nYou have been defeated!\n")
            play_again()
            break
        if choice2 == "2":
            print_pause("\nYou run back into the field. "
                        "\nLuckily, you don't seem to have been "
                        "followed.\n")
            field(item, option)
            break


def field(item, option):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to look into the forest.")
    print_pause("What would you like to do?")
    while True:
        choice1 = input("(Please enter 1 or 2.)\n")
        if choice1 == "1":
            house(item, option)
            break
        elif choice1 == "2":
            cave(item, option)
            break


def play_again():
    again = input("Would you like to play again? (y/n)").lower()
    if again == "y":
        print_pause("\n\n\nExcellent! Restarting the game ...\n\n\n")
        play_game()
    elif again == "n":
        print_pause("\n\n\nThanks for playing! See you next time.\n\n\n")
    else:
        play_again()


def play_game():
    item = []
    option = random.choice(["Wolf", "Demon"])
    intro(item, option)
    field(item, option)


play_game()