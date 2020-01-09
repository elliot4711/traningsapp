from formulas import rep_hypertrophy, rep_strenght, rep_toning

import csv

def welcome():
    print("Welcome to the number one gym app! \n") #Welcomes user

def main():
    welcome()
    

def load_system():
    ans = input("Do you want to create a new workout or use your most recent workout (only do this if you have completed setup before)? please answear \"new\" or \"load\"  ")
    if ans == "new":
        setup_and_app()
    elif ans == "load":
        path = "/Users/elliotstjernqvist/Dokument/Skola/Programmering_1/Python/traningsapp/traningsapp_data.csv"
        file = open(path, newline='')
        reader = csv.reader(file)
        temp = next(reader)
        for y in range(len(temp)-1):
            temp[y+1].replace("'", "")
            my_exercises[y] = temp[y+1]
        for row in reader:
            my_sets[0] = str(row[0])
            my_weights[0] = float(row[1])
            my_weights[1] = float(row[2])
            my_weights[2] = float(row[3])
            my_weights[3] = float(row[4])
    else: 
        load_system()

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
            check_excercise(i)
        ans = input("Would you like to save this workout setup for later? y/n ")
        if ans == "y":
            save_system()

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
    my_sets[0] = "4x4"

def weight_setup_hypertrophy():
    for y in range(4):
        max = int(input("Please enter your " + my_exercises[y] + " max rep in kg: "))
        my_weights[y] = round(rep_hypertrophy(max))
    my_sets[0] = "4x8"

def weight_setup_toning():
    for y in range(4):
        max = int(input("Please enter your " + my_exercises[y] + " max rep in kg: "))
        my_weights[y] = round(rep_toning(max))
    my_sets[0] = "4x16"