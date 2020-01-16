EXERCISES = ["benchpress", "squat", "deadlift", "military press"]
"""
There is no function that allows change of excercises in this program and they are therefore a global variable
"""

from formulas import rep_hypertrophy, rep_strenght, rep_toning

import csv

def welcome():
    """
    Welcomes the user
    """
    print("Welcome to the number one gym app! \n") 


def setup(EXERCISES): 
    """
    Begins user setup
    """
    ans = input("Would you like to create a new workout program? y/n ")
    if ans == "y":
        my_weights, my_sets = excercise_type(EXERCISES)
        return my_weights, my_sets
    else:
        print("I can't help you if you don't want to create a program")

def load_system():
    """
    Loads previous weights and sets from traningsapp_data.csv file
    """
    my_weights = [0, 0, 0, 0]
    path = "/Users/elliotstjernqvist/Dokument/Skola/Programmering_1/Python/traningsapp/traningsapp_data.csv"
    file = open(path, newline='')
    reader = csv.reader(file)
    _ = next(reader)
    for row in reader:
        my_sets = str(row[0])
        my_weights[0] = float(row[1])
        my_weights[1] = float(row[2])
        my_weights[2] = float(row[3])
        my_weights[3] = float(row[4])
    return my_weights, my_sets

def excercise_type(EXERCISES):
    """
    Calls respective function depending on what the users main training goal is
    """
    ans = input("Would you like to train for strenght, toning or hypertrophy (muscle building)? Please answear with either \"strenght\", \"hypertrophy\" or \"toning\" ").lower()
    if ans == "strenght": 
        my_weights, my_sets = weight_setup_strenght(EXERCISES)
        return my_weights, my_sets
    elif ans == "hypertrophy":
        my_weights, my_sets = weight_setup_hypertrophy(EXERCISES)
        return my_weights, my_sets
    elif ans == "toning":
        my_weights, my_sets = weight_setup_toning(EXERCISES)
        return my_weights, my_sets
    else:
        print("You have to choose either strenght, hypertropy or toning")
        excercise_type(EXERCISES)

def weight_setup_strenght(EXERCISES):
    """
    Setups working weight depending on the users maximum lifts and goal
    """
    my_weights = [0, 0, 0, 0]
    for y in range(4):
        max = int(input("Please enter your " + EXERCISES[y] + " max rep in kg: "))
        my_weights[y] = round(rep_strenght(max))
    my_sets = "4x4"
    return my_weights, my_sets

def weight_setup_hypertrophy(EXERCISES):
    """
    Setups working weight depending on the users maximum lifts and goal
    """
    my_weights = [0, 0, 0, 0]
    for y in range(4):
        max = int(input("Please enter your " + EXERCISES[y] + " max rep in kg: "))
        my_weights[y] = round(rep_hypertrophy(max))
    my_sets = "4x8"
    return my_weights, my_sets

def weight_setup_toning(EXERCISES):
    """
    Setups working weight depending on the users maximum lifts and goal
    """
    my_weights = [0, 0, 0, 0]
    for y in range(4):
        max = int(input("Please enter your " + EXERCISES[y] + " max rep in kg: "))
        my_weights[y] = round(rep_toning(max))
    my_sets = "4x16"
    return my_weights, my_sets

def training_app(my_sets, my_weights): 
    """
    Begins running the training app and takes command of the rest of the program calling functions as they are needed
    """
    while is_ready():
        for i in range(4):
            print("\nYour", EXERCISES[i], "sets are", my_sets, "at", round(int(my_weights[i])), "kg \n")
            check_excercise(my_weights, i)
        ans = input("Would you like to save this workout setup for later? y/n ")
        if ans == "y":
            save_system(my_sets, my_weights)

def is_ready(): 
    """
    Checks if the user is ready to start a workout
    """
    ans = input("Are you ready to start your workout? y/n ")
    return ans == "y"

def check_excercise(my_weights, i): 
    """
    Checks if the user is done with their excercise and checks the users response to the set
    """
    ans = input("Are you done with your " + EXERCISES[i] + "? y/n ")
    if ans == "y":
        print("\nWell done! \n")
        ans = feel_input()
        val = feel(ans)
        if val == 2:
            my_weights[i] = raise_weight(my_weights[i])
        elif val == 1:
            my_weights[i] = lower_weight(my_weights[i])
    elif ans == "n": 
        print("\nYou\'ve got to work harder!")
    else:
        check_excercise(my_weights, i)

def feel_input():
    """
    Takes answer and validates if answer is acceptable for the program and if so returns it as a string
    """
    ans = input("How did that feel on a scale from 1-5? ")
    while not ans.isdigit():
        ans = input("How did that feel on a scale from 1-5? ")
    ans = int(ans)
    return ans

def feel(feeling):
    """
    Asks the user how the excercise felt and returns 2 if the user felt like it went well and 1 if the user feels it did not go well
    Returned value is used in check_excercise function
    """
    if feeling <= 2:
        print("\nMaybe you should lower the weight")
        return 1
    elif feeling == 3:
        print("\nYou should probably keep the weight the same")
    else:
        print("\nMaybe you should raise the weight")
        return 2

def raise_weight(weight):
    """
    Asks the user if they want to increase the weight if the function before has returned 2 which means the user felt it went well
    """
    ans = input("\nWould you like to raise the weight? y/n ")
    if ans == "y":
        weight = weight + 5
        print("\nYour new rep weight is", weight, "kg")
    else:
        print("\nOk, we will keep the weight the same")
    return weight

def lower_weight(weight):
    """
    Asks the user if the want to decrease the weight if the function before has returned 1 which means the user felt it did not go well
    """
    ans = input("\nWould you like to decrease the weight? y/n ")
    if ans == "y":
        weight = weight - 5
        print("\nYour new rep weight is", weight, "kg")
    else:
        print("\nOk, we will keep the weight the same")
    return weight

def save_system(my_sets, my_weights):
    """
    Saves the previous excercise weights and sets
    """
    returns_path = "/Users/elliotstjernqvist/Dokument/Skola/Programmering_1/Python/traningsapp/traningsapp_data.csv"
    file = open(returns_path, "w")
    writer = csv.writer(file)
    writer.writerow(["sets", EXERCISES[0], EXERCISES[1], EXERCISES[2], EXERCISES[3]])
    writer.writerow([my_sets[0], my_weights[0], my_weights[1], my_weights[2], my_weights[3]])

if __name__ == "__main__":
    """
    Begins running the setup and app if the program is the main program and not being imported into another program
    """
    welcome()
    """
    App setup begins
    """
    ans = input("Do you want to create a new workout or use your most recent workout (only do this if you have completed setup before)? please answear \"new\" or \"load\"  ")
    if ans == "new":
       my_weights, my_sets = setup(EXERCISES)
    elif ans == "load":
        my_weights, my_sets = load_system()
    else:
        my_weights, my_sets = load_system()
    training_app(my_sets, my_weights)
    """
    Setup complete app begins running
    """