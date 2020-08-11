import time
import random


def print_pause(message):
    print(message)
    time.sleep(1)


def waiting(message):
    print(message)
    time.sleep(5)


def intro():
    print_pause("Welcome to the wonderful world of Warri")
    print_pause("This is where your dating dreams come true!")
    print_pause("All the tools to be perfect for a date are here "
                "in Warri at different levels")
    print_pause("Enjoy your time here and We hope you get a date")


def level_one(items):
    print_pause("You are in the hair department.")
    print_pause("Our top hairdressers will have your hair looking super fly!")
    if "hair" in items:
        print_pause("Your hair is already done you look around "
                    "to see what else the Warri has to offer")
    else:
        print_pause("Tara is here to do your hair")
        items.append("hair")
    print_pause("Your hair looks great! Where to next?")
    explore_warri(items)


def beauty(items):
    choices = random.choice(["fenty", "charlotte tilbury", "MAC"])
    if "fenty" in choices:
        print_pause("You recieved a makeover using Fenty products!")
        items.append("ready")
    elif "MAC" in choices:
        print_pause("You recieved a makeover using MAC products!")
        items.append("ready")
    elif "charlotte" in choices:
        print_pause("You recieved a make over using "
                    "Charlotte Tilbury Products")
        items.append("ready")


def level_two(items):
    print_pause("You are in the beauty department")
    if "makeup" in items:
        print_pause("make already had already done")
    elif "hair" in items:
        print_pause("You had your hair done you so its "
                    "only natural you should now do your makeup")
        print_pause("There are many brands you could use ")
        beauty(items)
    else:
        print_pause("It doesnt make sense to do your make up "
                    "before you have had your hair done.")
        print_pause("You can get your hair done on level 1")
    explore_warri(items)


def date():
    date = random.choice(["yes", "no"])
    if "no" in date:
        print_pause("Unfortunately your blind date turned down your offer")
    elif "yes" in date:
        print_pause("Congratulations you have a date!!")


def play_again():
    play_again = input("would you like to play again?\n""Y\n""or N\n")
    if play_again == "Y":
        play_game()
    elif play_again == "N":
        print_pause("Thanks for playing!")
    else:
        print_pause("Please choose either Y or N")
        replay()


def level_three(items):
    print_pause("You are at the First Dates Restaurant")
    print_pause("This is where we set you up with with a blind date")
    print_pause("Someone will be here to check you out soon")
    print_pause("This is your moment! Good luck!!")
    if "ready" in items:
        print_pause("You had your hair done it looks great")
        print_pause("So far so good")
        print_pause("Your makeup looks good too")
        print_pause("Congratulatons! We think you are ready for a date!")
        waiting("Please wait while we check with the potential date")
        date()
        play_again()
    elif "hair" in items:
        print_pause("Your hair looks great but you could do with "
                    "a bit of makeup!"
                    "You need to have both your hair and make up done "
                    "before we consider you date ready")
        print_pause("Your makeup can be done on level 2")
        explore_warri(items)
    else:
        print_pause("Unfortunately, we like our guests to have "
                    "both hair and make up done.")
        print_pause("Why not take advantage of ALL Warri has to offer!")
        print_pause("You can get your hair done on level 1 and "
                    "you can get your makeup done on level 2 ")
        explore_warri(items)


def explore_warri(items):
    print_pause("Where would you like to go?:")
    level = input("1. Hair department\n"
                  "2. Makeup department\n"
                  "3. First Dates Restaurant\n")
    if level == "1":
        level_one(items)
    elif level == "2":
        level_two(items)
    elif level == "3":
        level_three(items)
    else:
        print_pause("Please choose level 1, 2, or 3")
        explore_warri(items)


def play_game():
    items = []
    intro()
    explore_warri(items)


def replay():
    play_again()


play_game()
