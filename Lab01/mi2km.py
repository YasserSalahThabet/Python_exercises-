#!/usr/bin/env python3

#Yasser Thabet
#Palomar College CSIT 175
#Lab 1, excercise 3, miles to kilometers Calculator



# Function to convert miles to kilometers

def miles_to_km(miles):
    
    # Conversion factor (given): 1 km = 0.62 miles
    
    conversion_factor = 1 /0.62
    
    # Calculate kilometers
    
    km = miles * conversion_factor

    return km 
    


miles = float(input("Enter distance in miles: "))

km = miles_to_km(miles)

print(f"{miles} miles is equal to {km:.2f} km.")
