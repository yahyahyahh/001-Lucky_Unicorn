show_instructions = ""
while show_instructions.lower() != "xxx":

    # Ask the user if they have played before
    show_instructions = input ("Have you played this game before? ").lower()

    # If they say yes, output 'program  continues'
    if show_instructions == "yes" or show_instructions == "y":
        print("program continues")

    # If they say no, output 'display instructions'
    elif show_instructions == "no" or show_instructions == "n":
        print("display instructions")

    # If anything other than yes or no, output 'Please answer yes / no'
    else:
        print("Please answer yes / no")

    print("You chose: {}".format(show_instructions))