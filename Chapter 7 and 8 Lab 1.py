#Jeremy Durdel
#Chapter 7 and 8 Lab 1
#07/01/2025

import csv

#Finds if the user wants to read or write specific file
name = input("What is the name of the file you wish to work with? ")
r_or_w = input("Are you going to (r)ead the file or (w)rite the file? ")

#If r this statement will read what's in the file
if r_or_w == "r":
    with open(name, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            print("The contents of the file are:")
            print()
            print(F"{row[0]} {row[1]}")
            print(F"{row[2]}")
            print(F"{row[3]}, {row[4]} {row[5]}")

#If w this statement will write address information into the file
elif r_or_w == "w":
    first_name = input("Enter the first name? ")
    last_name = input("Enter the last name? ")
    street_address = input("Enter the street address? ")
    city = input("Enter the city? ")
    state = input("Enter the state? ")
    zipcode = input("Enter the zip code? ")

    book = [first_name, last_name, street_address, city, state, zipcode]

    with open(name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(book)