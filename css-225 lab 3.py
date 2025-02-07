#Problem 1 – Write a program that prints “Hello World” to the screen. 

#Paola  

#February 1 ,2025  

# it prints a message onto a screen 

 

Print(“ Hello World!”) 

 

#Problem 2 – Write a program that asks the user for their name and greets them with their name. 

#paola 

#february 1. 2025 

#it asks user for name and greets them 

  

#Print(“What is your name?”) 

User_name=input  

Print (“Hello ” + user_name !) 

 

#Problem 3 – Modify the previous program such that only the users you and your instructor are greeted with their names.  

#paola  

#february 1,2025 

#modified version that greets yourself and instructor 

Authorized_users= [“MyName,” + “InstructorName”] 

name= input 

Print(“what is your name?”) 

If name is in Authorized_users: 

Print(“Hello, {name}! How are you.”) 

else: 

Print(“Hello, stranger! Who are you?”) 

 

#Problem 4 - Write a program that will compute the area of a circle. Prompt the user to enter the radius and print a nice message back to the user with the answer. 

#paola 

#february 2,2025 

#this program will compute the area of a circle & radius 

#for this program we need to use import math to able to use the math equations 

 

Import math 

#ask user to enter radius 

Radius = float(input(“enter the radius of the circle: “)) 

#we calculate the area next 

Area = math.pi * radius ** 2 

#display message 

Print (the area of the circle with radius {radius} is {area:.2f}  sqaure units.”) 

 

 

 

#Problem 5 - Write a program that will compute MPG for a car. Prompt the user to enter the number of miles driven and the number of gallons used. Print a nice message with the answer. 

#paola 

#february 2,2025 

# this program will compute MPG for a car 

 

#prompt the user to enter number of miles driven in a car. 

Miles= float(input(“Enter the number of miles in a car:”)) 

 

#prompt the user tp enter the number of gallons used in a car 

Gallons = float(input(“Enter the number of gallons used in a car:”)) 

 

#calculate MPG 

MPG = miles / gallons 

 

#Display friendly message 

Print(f”MPG: {MPG:.2f}”) 

 

 

 

 

#Problem 6 - Write a program that will convert degrees Fahrenheit to degrees Celsius. 

#paola 

#february 2,2025 

#this program converts degrees  farenheit to celcius 

 

Fahrenheit = float(input(“Please enter the temperature in farenheit: “)) 

 

Celsius = (farenheit – 32) * 5/9 

 

Print (f”{fareneheit} °F is equal to {celsius:.2f} °c.”) 

 

 

 

#Problem 7 - It is possible to name the days 0 through 6 where day 0 is Sunday and day 6 is Saturday. If you go on a wonderful holiday leaving on day number 3 (a Wednesday) and you return home after 10 nights you would return home on a Saturday (day 6) Write a general version of the program which asks for the starting day number, and the length of your stay, and it will tell you the number of day of the week you will return on. 

#paola 

#february 2,2025 

#calculates day of return 

 

#Prompt the user for the starting day number (0 = Sunday, 6 = Saturday) 

start_day = int(input("Enter the starting day number (0 for Sunday, 6 for Saturday): ")) 

 

#Prompt the user for the length of stay (number of nights) 

stay_length = int(input("Enter the number of nights you will stay: ")) 

 

#Calculate the return day 

return_day = (start_day + stay_length) % 7 

 

#Display the result 

print(f"You will return on day number {return_day}.") 