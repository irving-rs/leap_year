#leap_year.py
#Date: 09/October/2020
#by irving-rs

#DESCRIPTION:
#Leap Year: Tells you if a certain year is leap year or not.

#DETAILS:
#The year must be greater than 1582, when the transition between the Julian Calendar and the Greagorian calendar started.
#A leap year must follow the next statements:
#The year must be divisible by 4. (year%4 == 0)
#The year must not be divisible by 100, unless the year is also divisible by 400. (year%100 != 0 or year%400 == 0)


#FUNCTIONS:
def verify_input(year): #Verifies if the input is on a valid range.
    if year >= 1582:
        return True
    else:
        print("\nPlease choose a year greater or equal than 1582.\n")
        return False

def leap_year(year): #Determines if is leap year (True) or not (False).
    if (year%4==0) and (year%100 != 0 or year%400 == 0):
        return True
    else:
        return False


#PRESENTATION:
print("\nLEAP YEAR:")
print("\nTells you if a certain year is leap year or not.\n")


#BODY:
year=int(input("Please, enter the year: "))

if verify_input(year) == True:
    if leap_year(year) == True:
        print("\nThe year", year, "is leap year.\n")
    else:
        print("\nThe year", year, "is not leap year.\n")
