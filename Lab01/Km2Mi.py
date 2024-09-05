#!/usr/bin/env python3

#Yasser Thabet
#Palomar College CSIT 175
#Lab 1, excercise 2, Kilometers to Miles Calculator



# Function to convert kilometers to miles

def km_to_miles(km):
    
    # Conversion factor (given)
    
    conversion_factor = 0.62
    
    # Calculate miles
    
    miles = km * conversion_factor
    return miles


km = float(input("Enter distance in kilometers: "))
miles = km_to_miles(km)

print(f"{km} km is equal to {miles} miles.")
