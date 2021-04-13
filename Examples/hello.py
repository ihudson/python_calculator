# This program says Hello and asks for my Name

print('Hello World!')
print('What is your name?') # Ask for the users name
myName = input()
print('It is good to meet you, ' + myName)
print('The lenght of your name is:')
print(len(myName))
print('What is your age?') # Ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
