from numpy import place
from pandas import array


name= input("What is your name?")
print("Welcome", name)
print("It is fantastic to have you here!")

place= input("Where do you live?")
if place in ["Delhi", "Mumbai", "Hyderabad", "Banglore"]:
    print("You belong to the four big cities of India.")
    



