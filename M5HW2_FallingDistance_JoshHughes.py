# A brief description of the project
# 10/10/2016
# CTI-110 M5HW2 - Falling Distance
# Joshua Hughes
#


# Formula is d= 1/2 gt²


def main():
    print('Time \tMeters')
    print('-------------')
    falling_distance = time()
    
    
    


def time():
    # g is a constant of 9.8
    g = 9.8

        # t is the amount of time from 1-10 seconds
    for t in range(1,11):
        
        # d stands for distance covered in seconds
        d = format(.5 * g * t**2,'.2f')
        print(t,'\t',d)


main()    
