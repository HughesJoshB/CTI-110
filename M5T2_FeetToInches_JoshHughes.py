# Converting feet to inches
# Date
# CTI-110 M5T2_FeetToInches 
# Joshua Hughes


# Constant for the number of inches per foot
inchesPerFt = 12

# main function
def main():
    #Get a number of feet from the user
    feet = int(input('Enter a number of feet: '))

    #Convert that to inches.
    print(feet, 'ft equals', feetToInches(feet), 'inches.')

# The feetToInches function converts feet to inches
def feetToInches(feet):
    return feet * inchesPerFt

#call the main function
main()
