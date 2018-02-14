#Body Mass Index Calculator
#9/13/2016
#CTI-110 M3HW2-Body Mass Index
#Joshua Hughes

#Ask individual to enter weight
weight = int(input('Please enter your body weigh in lbs.:'))

#Ask Individual to enter Height
height = int(input('Please enter your height in inches.:'))

#calculate Body Mass Index
# BMI = weight * 703/ (height * height)

bmi = weight * 703 / (height**2)

if bmi < 18.5:
    print('Your BMI of', format(bmi,'.2f'), 'is underweight for your height.')
elif bmi >= 18.5 and bmi <= 25:
    print('Your BMI of', format(bmi,'.2f'), 'is the optimal for your height.')
else:
    print('Your BMI of', format(bmi,'.2f'), 'is overweight for your height.')
    
