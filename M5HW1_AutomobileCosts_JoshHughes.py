# Calculating Automobile Costs
# 10/6/2016
# CTI-110 M5HW1 - Automobile Costs
# Joshua Hughes



def main():
    total = monthlyTotal()
    print('The amount you spend per month is $', format(total,'.2f'))
    yearlyTotal = total * 12
    print('What you spend per year is $', format(yearlyTotal,'.2f'))


def monthlyTotal():
    loan = float(input('Enter your monthly loan payment. '))
    insurance = float(input('Enter your monthly insuracne. '))
    gas = float(input('Enter the total amount spent on gas each month. '))
    oil = float(input('How much on oil do you spend per month? '))
    tires = float(input('How much on tires do you go spend a month? ')) 
    maintance = float(input('How much on monthly maintance do you spend? '))
    total = loan + insurance + gas + oil + tires + maintance
    return total



              
main()
