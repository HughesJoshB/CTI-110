# Letting student know their letter grade
# 9/7/2016
# CTI-110 M3T2 - Debugging
# Joshua Hughes

#Grade scale

A_score = 90
B_score = 80 
C_score = 70 
D_score = 60 

#Ask student what their grade is
score = float(input('What did you make on your last test?:'))

 

#Input grade into grade scale
              
if score >= A_score:
    print('Your grade is A.')
elif score >= B_score:
    print('Your grade is B.')
elif score >= C_score:
    print('Your grade is C.')
elif score >= D_score:
    print('Your grade is D.')
else:
    print('Your grade is F.')
