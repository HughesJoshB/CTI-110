# Kilometer Converter Problem
# 10/4/2016
# CTI-110 M5T1_KilometerConverter 
# Joshua Hughes

#  Miles = Kilometers X 0.6214
conversionFactor = 0.624

# The main function gets a distance in kilometers and calls the showMiles to
# conver it

def main():
    # Get the distance in kilometers
    kilometers =float(input('Enter the distance in kilometers: '))

    #Display the distance converted to miles
    showMiles(kilometers)

# The showMiles function converts the km from Kilometers to miles and displays
# result
                      
def showMiles(km):
    #Convert Kilometers to miles
    miles = km * conversionFactor
    #display miles
    print(km, 'kilometers equals', miles, 'miles.')

#call main
main()    
