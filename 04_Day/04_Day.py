a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')

language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

#Slicing Python Strings
#In python we can slice strings into substrings.

first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
last_three = language[3:6]

# Reversing a String
# We can easily reverse strings in python.

greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH

challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

print(challenge.rfind('y'))  # 16
print(challenge.rfind('th')) # 17