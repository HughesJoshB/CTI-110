# Age Classifier
# 9/8/2016
# CTI-110 M3HW1 - Age Classifier
# Joshua Hughes



#Ask the age of individual
age = int(input('How old are you?'))

#Determine age class of individual
if age <= 1:
	print('You are an infant.')
elif age < 13:
	print('You are a child.')
elif age < 20:
	print('You are a teenager.')
else:
	print('You are an adult.')
