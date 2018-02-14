# Bug Collecting Total
# Sept 20, 2016
# CTI-110 M4T1 - Bug Collector
# Josh Hughes



#Initialize the accumulater
total = 0

#Get the bugs collected for each day
for day in range(1, 8):
    print('Enter the bugs collected on day', day)
    bugs = int(input())
    total += bugs

#Display the total bugs.
print('You collected a total of', total,'bugs.')
