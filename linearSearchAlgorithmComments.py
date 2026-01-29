# main program
nlist = [23, 56, 21, 89, 54, 12, 99]   # list of numbers (x1 mark)
searchTerm = int(input('Enter the search term: '))   # 1 mark
found = False
# start at the beginning of the list (x1 mark)
# search through consecutive values in the list (x1 mark)
for x in range(0, len(nlist)):

    # checks to see if searchterm is the same as value in the list
    if (searchTerm == nlist[x]):
        # if searchTerm matches a value in the list (x1 mark)        
        found = True
        break

if (found == True):
    # output found search term and position (x1 mark)
    print('Found search term at position ', x)
else:
    # output not found search term and output -1 (x1 mark)
    print('Not found search term therefore position -1')


