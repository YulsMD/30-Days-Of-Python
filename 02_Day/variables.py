# Day 2: 30 Days of python programming

# Exercises level 1
first_name = 'Yulissa'
last_name = 'Martínez'
full_name = 'Yulissa Martinez'
country = 'Mexico'
city = 'Puebla'
age = 25
year = 2022
is_married = False
is_true = True
is_light_on = True
num_one, num_two = 5 , 4

# Exercises: level 2
print(type(first_name), type(last_name), type(full_name))
print(type(country), type(city), type(age), type(year))
print(type(is_married), type(is_true), type(is_light_on))

print('first_name', len(first_name))
print('last_name', len(last_name))

total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

import math
radius = 30
area_of_circle = math.pi * (radius ** 2)
circum_of_circle = 2 * math.pi * radius

print('Insert an area')
radius_input = float((input()))
area_of_circle_input = math.pi * (radius_input ** 2)
print(f"The area is, {area_of_circle_input}")

first_name_input = str(input())
last_name_input = str(input())
full_name_input = str(input())
country_input = str(input())
