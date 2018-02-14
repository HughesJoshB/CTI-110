#   This program calculates the amount of sugar, butter and flour
#   needed to make cookies
#   September 1st, 2016
#   CTI-110 M2HW2
#   Joshua Hughes

#Declare the constant values needed for the recipe
SUGAR_RECIPE = 1.5
BUTTER_RECIPE = 1.0
FLOUR_RECIPE = 2.75
COOKIE_YIELD = 48


#prompt user for # of cookies wanted
cookies = float(input('How many cookies would you like to make today?'))

#Calculate cups of sugar needed

Sugar = (cookies * SUGAR_RECIPE) / COOKIE_YIELD

#Calculate butter needed

Butter = (cookies * BUTTER_RECIPE) / COOKIE_YIELD

#Calculate flour needed

Flour = (cookies * FLOUR_RECIPE) / COOKIE_YIELD

#Display results of amount of Sugar, Butter and Flour needed
#to make the specified number of cookies

print('To make', cookies, 'cookies, you will need:')
print(format(Sugar, '.2f'), 'cups of sugar.')
print(format(Butter, '.2f'), 'cups of butter.')
print(format(Flour, '.2f'), 'cups of flour.')
      




