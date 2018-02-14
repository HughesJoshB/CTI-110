# Calculating Tuition Increase
# 9/27/2016
# CTI-110 M4HW2 - Tuition Increase
# Josh Hughes

totalTuition = 0
#Ask student/parnet how many yrs of college is expected
year = int(input('Input total number of years planning on attending college:'))
 
#Cost of 1st yr per Semster is
print('The cost of the first semster is $8000.00.')
cost = 8000.00

#Display Graph of years and cost w/ increase of 3% per yr for each Semster
print('Year \tCost Per Semster')
print('-----------------------')
        
for year in range(1,year + 1,1):
    tuition = cost * 1.03
    cost *= 1.03 #cost becomes a new varaiable for each of the following yrs
    print(year, '\t', '$',format(tuition, '.2f'))



