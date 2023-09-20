# bringing in a random number and assigning it to answer (Print (answer) for testing purposes - make sure to # out)
from random import randint
number = randint(1, 50)
#print (number)


# This funtion is vailidating if the input was a number
#If they enter any number it will count as a try but invaild entries will not count toward count total
def vaild_response():
    while True:
        try:
            print ("Enter a number 1-50: ")
            guess = input()
            guess = int(guess) 
            return guess
        except ValueError:
            print("ERROR: Invalid input. Please enter a valid integer.")


#This funtion is the code for the actual guessing game
def guessing_game ():
    guess = int(0)
    count = int(0)
    while guess != number:
            guess = vaild_response()
            count += 1 #This keeps a running total of how many attempts it took for the person to guess the number
            if guess < 1 or guess > 50: 
                print ("INVALID ENTRY: Number must be between 1 - 50") #This still counts as a guess but reminds the player the number was not within range
            elif guess < number:
                print ("Guess Higher")
            elif guess > number:
                print ("Guess Lower")
    print ('Great guess you answered correctly.') 
    #This is just a fun addition to encourage repeat use. The player might want to try again to lower their attempt count
    #This first evaluates for 1 attempt then starts at the highest possible return and goes down.
    if count == 1:
        print ('WOW! You got the answer on your first try. You are incredible.')
    elif count > 15:
        print ('WOW! That took it a while!')
        print ('It took ' + str(count) + ' tries to guess the number.')
    elif count > 10:
        print ('I guess that could have taken longer.')
        print ('It took ' + str(count) + ' tries to guess the number.')
    else:
        print ("That wasn't a bad go")
        print ('It took ' + str(count) + ' tries to guess the number.')
    

# Asking user to play game
print ('Welcome to the guessing game of the century!!')
print ('Would you like to play?')
answer = 0 #priming the pump to enter the while loop
while answer != "yes" or answer != "no":
    print ('      Please enter yes or no')
    answer = input ()
    answer = answer.lower () #changing the answer to lower case to be able to evaluate
    if answer == "yes":
        print ('Nice!! You are going to love this!')
        guessing_game () #calling the guessing game funtion
        break
    elif answer == "no":
        print ('What? Seriously? Okay have a good day. Come back anytime.')
        break
    else:
            print ('Sorry but that is not a valid response.')
