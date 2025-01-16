#THIS IS CODE FOR FINDING HIGHER LOWER GAME
#THE PLAN IS TO GENERATE TWO RANDOM VALUES FROM A LIST AND GIVE IT AS AN OPTION TO THE USER, WHICHEVER OTION FROM THE TWO HAS HIGHER VALUE WILL BE DECIDED BY THE USER AND THE POINT WILL BE ADDED IF GUESSED RIGHT OR THE GAME IS ENDED.
#here the list is defined with the names,the profession and the followers. The number of followers will be the basis to check who has got higher value.
#So,when asking the user the options only the name and profession need to displayed and then based on the folowers in the list, the logic will be written to check if the user is right or wrong
#A count variale will be inialized to keep track of the user points and everytime he guesses right the option with higher value and another randomly generated value will be compared in a loop format
#start of the code
import random
followers = [1000, 2000, 3000, 4000, 500]
names = ["John", "Peter", "Rahul", "Rohan", "Sabrina"]
professions = ["Engineer", "Doctor", "Teacher", "Lawyer", "Actor"]


flag=True
count=0
while flag:
    #randomly select two values from the list
    option1 = random.choice(followers)
    option2 = random.choice(followers)
    #make sure that the two values are not same
    while option1 == option2:
        option2 = random.choice(followers)
    #display the options to the user
    print("Who do you think has more followers?")
    print("Option 1: ", names[followers.index(option1)], " ", professions[followers.index(option1)])
    print("Option 2: ", names[followers.index(option2)], " ", professions[followers.index(option2)])
        #input the option
    user_option = input("Enter the option you think has higher followers: ")
        #check if the user option is correct or not
    if user_option=='1':
        if option1>option2:
            count=count+1
            print("You got it right, here's your updated score:",count)
            #loop back
            flag=True
        else:
            print("You have lost the game! You can always play again.Here's your final score:",count)
            flag=False
    elif user_option=='2':
        if option2>option1:
            count=count+1
            print("You got it right, here's your updated score:",count)
            #loop back
            flag=True
        else:
            print("You have lost the game! You can always play again.Here's your final score:",count)
            flag=False

