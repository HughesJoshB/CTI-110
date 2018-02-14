#Distance Traveled by train
# 9/20/2016
#CTI-110 M4HW1 - Distance Traveled
#Josh Hughes


#Ask user for the speed of train
speed = int(input('At what speed where you traveling in mph?'))

#Ask user for time traveled
time = int(input('How many hours did the train travel?'))


#Calculate distance traveled


print('time \t distance')
print('----------------')

for time in range(1, time + 1):
    distance = speed * time
    print(time, '\t', distance)
