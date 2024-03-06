import random

def map_choice(choice_number):
    """
    Maps the numeric choice to the corresponding game element (stone, scissors, or paper).

    Args:
        choice_number (int): The user's input (1, 2, or 3).

    Returns:
        str: The corresponding choice (stone, scissors, or paper).
    """
    choices = ["stone", "scissors", "paper"]
    return choices[choice_number-1]

def ppt():
    """
    Plays the stone, scissors, paper game between the user and the PC.

    The game continues until either the user or the PC wins 3 rounds.
    Displays the user's and PC's choices, determines the winner, and keeps track of victories.

    Returns:
        None
    """
    count_victories_user = 0
    count_victories_pc = 0
    count_rounds = 0
    while count_victories_user < 3 and count_victories_pc < 3:
        count_rounds += 1
        print("Round:", count_rounds)
        user_election = int(input("Ingrese valor 1 → piedra, 2 → tijeras, 3 → papel:"))
        user_choice = map_choice(user_election)
        print("The user chooses:", user_choice)
        pc_election = random.randint(1,3)
        pc_choice = map_choice(pc_election)
        print("The PC chooses:", pc_choice)
        if user_election == 1 and pc_election == 2:
            count_victories_user += 1
            print("User won")
        elif user_election == 2 and pc_election == 3:
            count_victories_user += 1
            print("User won")
        elif user_election == 3 and pc_election == 1: 
            count_victories_user += 1
            print("User won")
        elif user_election == pc_election:
            print("It's a tie")
        else:
            count_victories_pc += 1
            print("PC won")
    print("Rounds played:", count_rounds)
    print("User's defeats:", count_victories_pc)
    print("User's victories:", count_victories_user)
ppt()