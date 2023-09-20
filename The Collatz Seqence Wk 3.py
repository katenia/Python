
print ('I want to show you a fun math trick?')
print ('Please enter a whole number greater than 1.')
orignialNumber = input ()

#a try and except where we validate if it is a whole number and it's above 1. If not we cycle throught until we get a valid entry
while True:
    try:
        orignialNumber = int(orignialNumber)
        if orignialNumber <= 1:
            raise ValueError
        break
    except ValueError:
        print ("Sorry, that is not a valid entry.")
        print ('Please enter a whole number greater than 1.')
        orignialNumber = input ()


#the collatz math function
def collatz (orignialNumber):
    number = orignialNumber
    while number != 1:
        if number % 2 == 0:
            number = number//2
            print (number)
        else:
            number = number * 3 + 1
            print (number)



#calling the collatz math function
collatz (orignialNumber)


# This is just a repeat of the collatz code with explainations printing each time.
def explain (originalNumber):
    number = orignialNumber
    print ('')
    print ('The number you entered was ' + str(number))
    while number != 1:
        if number % 2 == 0:
            print ('On this line because the last number was even I did this problem:')
            print (str(number) + ' /2. The answer (without a remainder) is:')
            number = number//2
            print (number)
        else:
            print ('On this line because the last number was odd I did this problem:')
            print (str(number) + ' * 3 + 1. The answer is:' )
            number = number * 3 + 1
            print (number)
    print ('Eventually we always get to one and the math is over.')




#User is given the option to run the explain funtion that explains the math that happens in the program
print ('Can you guess what 2 math problems I did repreatedly to take your number to 1?')
print ("If you would like to hear the answer please enter 'show'")
showMe = input()
showMe == showMe.lower
if showMe == "show":
    explain (orignialNumber)
else:
    print ("It seems you don't want to see. Come back anytime. Math will be waiting")