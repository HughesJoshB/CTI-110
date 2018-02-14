# Program to show a nested loop
# 9/29/2016
# CTI-110 M4HW3 - Nested Loops
# Joshua Hughes



# define base size
base_size = 7

#row 1 should have 7 columns
#row 7 should have 1 column

for r in range(base_size): # r starts at 0 to begin
    for c in range(7 - r): # first row to print is 7 then each row after is -1
        print('*', end='')
    print()
        
