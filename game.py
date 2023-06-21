"""Choose Your Own Adventure experience!"""
from random import randint

__author__ = "730561652"


SPARKLE: str = "\U00002728"
BAGUETTE: str = "\U0001F956"
HEART: str = "\U0001F48C"
CROISSANT: str = "\U0001F950"
SEQUENCE: str = (SPARKLE + BAGUETTE + HEART + CROISSANT) * 4
PHONE: str = "\U0001F4DE"
PLANE: str = "\U0001F6EB"
METRO: str = "\U0001F687"
MONEY: str = "\U0001F4B5"
SAD: str = "\U0001F625"
UBER: str = "\U0001F4F2"
STRANGER: str = "\U0001F9CD"
DICTIONARY: str = "\U0001F4D6"


points: int = 15
player: str = ""


def greet() -> None:
    """Is the greet function! Introduces the player to the game."""
    global player 
    player = input("Welcome to the game! What is your name? ")
    print()
    print(f"Welcome {player}! Let's get started!")
    print()
    print(f"*****{SEQUENCE}*****")
    print(f"Megan, you  have just taken a vacation to Paris, France {PLANE}! You had so much fun, but unfortunately,")
    print("you are lost on the way to the airport! You did a lot of shopping, so you only have $15 in your wallet.")
    print("Your phone has died, and you have no way of charging it.")
    print("You need to find a way to get back to the airport without losing all of your money!")
    print()


def stranger_gives_money(money: int) -> int:
    """Initiates the function where the stranger gives player money, if they choose to take it."""
    global points
    points = money
    print("Wait! Before you start your journey...")
    print("A stranger walks up to you...she looks very friendly!")
    # changes points based on whether or not player wants to talk to stranger
    choice: str = input("Would you like to talk to them? (Y/N): ")
    if choice == "Y":
        points += 5
        print()
        print("***************************************************")
        print("The stranger just gave you $5 because you looked lost!")
        print(f"You now have ${points} to use on your journey.")
        print("***************************************************")
    print()


def pick_choice() -> None:
    """Is the protocol for the player picking where they want to start in the game."""
    print("Ok. Back to your mission!")
    print("What do you want to do first?")
    print(f"1. Walk into the bakery that is on your left {CROISSANT}")
    print(f"2. Talk to the stranger standing next to you {STRANGER}")
    print(f"3. Use the payphone to call a friend {PHONE}")
    print(f"*****{SEQUENCE}*****")
    print()


def pay_for_snack() -> None:
    """Changes points to account for buying a pastry."""
    global points
    print("You are about to pay $10 to buy a pastry...")
    see_money: str = input("Would you like to see how much money you have left as well? (Y/N): ")
    # prints out how much money player has left if they choose to check
    if see_money == "Y":
        print()
        print(f"You have ${points} left.")
    # updates points due to cost of pastry
    points -= 10
    print()


def pay_for_dictionary() -> None:
    """Changes points to account for buying a dictionary."""
    global points
    print("You are about to pay $5 to buy a dictionary...")
    see_money: str = input("Would you like to see how much money you have left as well? (Y/N): ")
    # prints out how much money player has left if they choose to check
    if see_money == "Y":
        print()
        print(f"You have ${points} left.")
    print()
    # updates points due to cost of dictionary
    points -= 5


def pay_for_phone() -> None:
    """Changes points to account for paying to use a phone."""
    global points
    print("You are about to pay $10 to phone a friend...")
    see_money: str = input("Would you like to see how much money you have left as well? (Y/N): ")
    # prints out money left if player chooses to check
    if see_money == "Y":
        print()
        print(f"You have ${points} left.")
    print()
    # updates points based off of paying for the payphone
    points -= 10
    

def bakery() -> None:
    """Introduces the player to the bakery option, and directs the player from there."""
    global points
    print(f"{player}, you walk into a cute bakery and walk up to the clerk.")
    print("He asks you something in French, and you have no idea what he is saying!")
    print("What do you do next?")
    print()
    print(f"1. Buy a snack to please the man ($10) {CROISSANT}")
    print(f"2. Enlist the help of a stranger {STRANGER}")
    print()
    choice: str = input("Enter your number choice: ")
    print()
    # if player chooses to buy a snack, enters into a game direction
    if choice == "1": 
        print("***************************************************")
        print()
        pay_for_snack()
        print("You just spent $10 on a pain au chocolat...")
        print("But! The man offered to buy you a cab to the airport! Success! You are going home!")
    # if player chooses to enlist the help of a stranger, enters into that game direction
    elif choice == "2": 
        print("***************************************************")
        print()
        print("The stranger luckily speaks English!")
        print(f"They give you a map of Paris and all of the metro routes {METRO}. You get to go home!")
    print()


def talk_to_stranger() -> None:
    """Introduces player to the talk to stranger option, and leads the player from there."""
    global points
    print(f"{player}, you decided to go up to a friendly-looking woman on the street.")
    print("However, she doesn't speak English!")
    print("Do you...")
    print(f"1. Buy a French dictionary ($5) to communicate with her {DICTIONARY}")
    print(f"2. Go into the bakery {CROISSANT}")
    print(f"3. Use the payphone {PHONE}")
    print()
    choice: str = input("Enter your number choice: ")
    print()
    # if player chooses to buy dictionary, enters into that game direction
    if choice == "1":
        # updates money
        print("***************************************************")
        print()
        pay_for_dictionary()
        print(f"It worked! The woman was able to tell you how to use the metro to get to the airport {METRO}. Merci! Au revoir Paris!")
    elif choice == "2":
        print("***************************************************")
        print()
        bakery()
    elif choice == "3":
        print("***************************************************")
        print()
        phone_a_friend()


def phone_a_friend() -> None:
    """Introduces player to the phone a friend option, leading the player from there."""
    global points
    print(f"{player}, you decide to go to the payphone to see if you can call your new best friend in Paris.")
    print("Thankfully you remember their number! But, it costs $10 to phone a friend.")
    print("Do you...")
    print(f"1. Phone a friend {PHONE}")
    print(f"2. Go into bakery {BAGUETTE}")
    print(f"3. Talk to a stranger {STRANGER}")
    choice: str = input("Enter your number choice: ")
    if choice == "1":
        print("***************************************************")
        print()
        does_phone_work()
    elif choice == "2":
        print("***************************************************")
        print()
        bakery()
    elif choice == "3":
        print("***************************************************")
        print()
        talk_to_stranger()
    print()


def does_phone_work() -> None:
    """The protocol for calling the friend and whether or not they pick up."""
    global points
    pay_for_phone()
    print(f"Ring, ring, ring...{PHONE}{PHONE}{PHONE}")
    if_ring: int = randint(1, 3)
    if if_ring == 1:
        print(f"Yay! Your friend picked up, and they called you an Uber to the airport! {UBER}")
        print("Au revoir Paris!")
        print()
    else:
        print("...Oh no...")
        print(f"Your friend didn't answer! {SAD}")
        choice: str = input("What would you like to try again? (Y/N): ")
        if choice == "Y":
            does_phone_work()
        else:
            print("Do you...")
            print(f"1. Go into bakery {BAGUETTE}")
            print(f"2. Talk to a stranger {STRANGER}")
            choice = input("Enter your number choice: ")
            if choice == "1":
                print("***************************************************")
                print()
                bakery()
            elif choice == "2":
                print("***************************************************")
                print()
                talk_to_stranger()
    print()
            

def main() -> None:
    """Main function."""
    greet()
    stranger_gives_money(points)
    pick_choice()
    choice: str = input("Enter your number choice: ")
    if choice == "1":
        print()
        print("***************************************************")
        print()
        bakery()
    elif choice == "2":
        print()
        print("***************************************************")
        print()
        talk_to_stranger()
    elif choice == "3":
        print()
        print("***************************************************")
        print()
        phone_a_friend()
    else:
        print("You did not select a valid choice. Try again.")
        main()
    
    if points < 0:
        print()
        print(f"Oh no... turns out you didn't get to go home after all. You ended up going into debt! You are ${(points / -1)} in debt!")
        print(f"Looks like you better start trying to find an apartment...{SAD}")

    elif points >= 0:
        print()
        print(f"You made it to the airport with ${points} left! {MONEY}")
        print()
        if points > 0:
            keep_playing: str = input("Would you like to keep playing with the money you have left? (Y/N): ")
            print()
            if keep_playing == "Y":
                print("***************************************************")
                print()
                main()


if __name__ == "__main__":
    main()