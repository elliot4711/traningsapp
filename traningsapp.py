"""
Global variables for program setup
"""
my_weights = [0, 0, 0, 0] # List of the users rep weights
my_exercises = ["benchpress", "squat", "deadlift", "military press"]
my_sets = [0]

"""
functions
"""
from formulas import rep_hypertrophy, rep_strenght, rep_toning

import csv


"""
returns_path = "/Users/elliotstjernqvist/Dokument/Skola/Programmering_1/Python/traningsapp/traningsapp_data.csv"
file = open(returns_path, "w")
writer = csv.writer(file)
"""
"""
writer.writerow(["sets", "benchpress reps", "squat reps", "deadlift reps", "military press reps"])
writer.writerow(["4x8", 70, 100, 155, 40])
"""
def welcome():
    print("Welcome to the number one gym app! \n") #Welcomes user
    print("Let\'s get started with creating your program: \n")

def is_ready(): 
    ans = input("Are you ready to start your workout? y/n ")
    return ans == "y"

def save_system():
    ans = input("Do you want to create a new workout or use your most recent workout (only do this if you have completed the setup before)? please answear \"new\" or \"load\"  ")
    if ans == "new":
        setup_and_app()
    elif ans == "load":
        path = "/Users/elliotstjernqvist/Dokument/Skola/Programmering_1/Python/traningsapp/traningsapp_data.csv"
        file = open(path, newline='')
        reader = csv.reader(file)
        my_exercises = next(reader)
        for row in reader:
            my_sets = row[0]
            my_weights[0] = float(row[1])
            my_weights[1] = float(row[2])
            my_weights[2] = float(row[3])
            my_weights[3] = float(row[4])
        training_app()

def excercise_type():
    ans = input("Would you like to train for strenght, toning or hypertrophy (muscle building)? Please answear with either \"strenght\", \"hypertrophy\" or \"toning\" ").lower()
    if ans == "strenght": 
        weight_setup_strenght()
    elif ans == "hypertrophy":
        weight_setup_hypertrophy()
    elif ans == "toning":
        weight_setup_toning()
    else:
        print("You have to choose either strenght, hypertropy or toning")
        excercise_type()


def weight_setup_strenght():
    for y in range(4):
        max = int(input("Please enter your " + my_exercises[y] + " max rep in kg: "))
        my_weights[y] = round(rep_strenght(max))
    my_sets.append("4x4")

def weight_setup_hypertrophy():
    for y in range(4):
        max = int(input("Please enter your " + my_exercises[y] + " max rep in kg: "))
        my_weights[y] = round(rep_hypertrophy(max))
    my_sets.append("4x8")

def weight_setup_toning():
    for y in range(4):
        max = int(input("Please enter your " + my_exercises[y] + " max rep in kg: "))
        my_weights[y] = round(rep_toning(max))
    my_sets.append("4x16")



def feel(feeling): #Asks the user how the excercise felt and returns 1 if the user felt like it went well
    if feeling <= 2:
        print("\nMaybe you should lower the weight")
        return 1
    elif feeling == 3:
        print("\nYou should probably keep the weight the same")
    else:
        print("\nMaybe you should raise the weight")
        return 2

def raise_weight(weight): # Asks the user if they want to increase the weight if the function before has returned 2 which means the user felt it went well
    ans = input("\nWould you like to raise the weight? y/n ")
    if ans == "y":
        weight = weight + 5
        print("\nYour new rep weight is", weight, "kg")
    else:
        print("\nOk, we will keep the weight the same")
    return weight

def lower_weight(weight): #Asks the user if the want to decrease the weight if the function before has returned 1 which means the user felt it did not go well
    ans = input("\nWould you like to decrease the weight? y/n ")
    if ans == "y":
        weight = weight - 5
        print("\nYour new rep weight is", weight, "kg")
    else:
        print("\nOk, we will keep the weight the same")
    return weight

def setup_and_app(): 
    ans = input("Would you like to create a new workout program? y/n ")
    if ans == "y":
        excercise_type()
        training_app()
    else:
        print("I can't help you if you don't want to create a program")

def training_app(): 
    while is_ready():
        for i in range(4):
            print("\nYour", my_exercises[i], "sets are", my_sets[0], "at", round(int(my_weights[i])), "kg \n")
            ans = input("Are you done with your " + my_exercises[i] + "? y/n ")
            if ans == "y":
                print("\nWell done! \n")
                x = int(input("How did that feel on a scale from 1-5? "))
                y = feel(x)
                if y == 2:
                    my_weights[i] = raise_weight(my_weights[i])
                elif y == 1:
                    my_weights[i] = lower_weight(my_weights[i])
            else:
                print("\nYou\'ve got to work harder!")


"""
Program running
"""

welcome()

save_system()



            
