# Linear search
nlist = [12, 43, 77, 98, 23, 72, 88, 77, 77, 77, 77]

searchTerm = int(input('Enter an integer: '))
# flag
found = False
count = 0

# loops through every data element in the list
for x in range(len(nlist)):

    # checks to see if the search term is in the list
    if (searchTerm == nlist[x]):
        # if the search term is in the list, found is assigned to True
        found = True
        count = count + 1

# checks to see what the value of found is?
if (found == True):
    print('Found data item', count, 'times')
else:
    print('Not found data item')
    
