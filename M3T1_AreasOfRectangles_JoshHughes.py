# Which of 2 rectangles has greatest area
# 9/6/2016
# CTI-110 M3T1 - Areas of Rectangles
# Joshua Hughes

#Get the dimensions of rectangle 1
length1 = float(input('Enter the length of rectangle 1 to nearest tenth:'))
width1 = float(input('Enter the width of rectangle 1 to nearest tenth:'))

#Get the dimensions of rectangle 2
length2 = float(input('Enter the length of rectangle 2 to nearest tenth:'))
width2 = float(input('Enter the width of rectangle 2 to nearest tenth:'))

#Calculate the areas of rectangles
area1 = length1 * width1
area2 = length2 * width2

#Which rectangle area is greatest
if area1 > area2:
    print('The area of rectangle 1 has the greatest area.')
elif area2 > area1 :
    print('The area of rectangle 2 has the greatest area.')
else:
    print('The area of recatangle 1 is equal to the area of rectangle 2.')
              
