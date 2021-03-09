import random


# Functions go here
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()
        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes / no")


def instructions():
    print("**** How to Play ****")
    print()
    print("")
    print()
    return""


def num_check(question, low, high):
    error = "please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))
            # if the amount is too low / too high give
            if low < response <= high:
                return response

            # output an error
            else:
                print(error)
        except ValueError:
            print(error)


def statement_generator(statement, decoration):

            sides = decoration * 3

            statement = "{} {} {}".format(sides, statement, sides)
            top_bottom = decoration * len(statement)

            print(top_bottom)
            print(statement)
            print(top_bottom)

            return ""

# Main Routine goes here...
statement_generator("Welcome to the Lucky Unicorn Game", "*")
print()

played_before = yes_no("Have you played this game before? ")
print("You chose {}".format(played_before))
print()

if __name__ == '__main__':
    if played_before == "no":
        instructions()


# Ask user how much they want to play with..
how_much = num_check("How much would you like to play with? ", 0, 10)
print()

# balance
balance = how_much

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    # print round number
    print()
    print("***  Round #{}  ***".format(rounds_played))
    chosen_num = random.randint(1, 100)

    # adjust balance
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        prize_decoration = "!"
        balance += 4
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        prize_decoration = "-"
        balance -= 1
    else:
        if chosen_num % 2 == 0:
            chosen = "horse"
            prize_decoration = "H"
        else:
            chosen = "zebra"
            prize_decoration = "Z"
        balance -= 0.5

    outcome = ("You got a {}. Your balance is ${:.2f}".format(chosen, balance))

    statement_generator(outcome, prize_decoration)

    if balance < 1:
        play_again = "xxx"
        print("Sorry, you ran out of money")

    else:
        play_again = input("Press enter to play again or 'xxx' to quit. ")

print()
print("Final balance: ${:.2f}".format(balance))
print()

statement_generator("   Thanks for playing !!   ", "*")
