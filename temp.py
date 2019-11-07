
def welcome():
    print("Welcome to the number one gym app! \n") #Welcomes user
    print("Let\'s get started with creating your program: \n")

def ready(): 
    ready = str(input("Are you ready to start your workout? y/n "))
    if ready == "y":
        return True

def repweight(max_weight): #Defines % of max rep weight that should be used for reps according to science
    return max_weight * 0.7

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
    y = str(input("\nWould you like to raise the weight? y/n "))
    if y == "y":
        weight = weight + 5
        print("\nYour new rep weight is", weight)
        return weight
    else:
        print("\nOk, we will keep the weight the same")
        return weight

def lower_weight(weight): #Asks the user if the want to decrease the weight if the function before has returned 1 which means the user felt it did not go well
    y = str(input("\nWould you like to decrease the weight? y/n "))
    if y == "y":
        weight = weight - 5
        print("\nYour new rep weight is", weight)
        return weight
    else:
        print("\nOk, we will keep the weight the same")
        return weight

def setup_and_app(): 
    answer = input("Would you like to create a new workout program? y/n ")
    if answer == "y":
        for y in range(4):
            max = int(input("Please enter your " + my_exercises[y] + " max rep in kg: "))
            my_weights[y] = round(repweight(max))
        training_app()
    else:
        print("I can't help you if you don't want to create a program")

def training_app(): 
    while ready():

        for i in range(4):
            print("\nYour", my_exercises[i], "sets are 4x8 at", round(int(my_weights[i])), "kg \n")
            done = input("Are you done with your " + my_exercises[i] + "? y/n ")
            if done == "y":
                print("\nWell done! \n")
                x = int(input("How did that feel on a scale from 1-5? "))
                y = feel(x)
                if y == 2:
                    my_weights[i] = raise_weight(my_weights[i])
                elif y == 1:
                    my_weights[i] = lower_weight(my_weights[i])
            else:
                print("\nYou\'ve got to work harder!")


my_weights = [0, 0, 0, 0] # List of the users rep weights
my_exercises = ["benchpress", "squat", "deadlift", "military press"]

welcome()

setup_and_app()




            


