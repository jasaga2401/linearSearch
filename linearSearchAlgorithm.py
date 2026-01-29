def linearSearch(searchTerm, nlist):  
    found = False
    count = 0
    pos = []
    y = 0

    for x in range(0, len(nlist)):
        
        if (searchTerm == nlist[x]):                    
            found = True
            pos.append(x)            
            count = count + 1            

    if (found == True):    
        print('Found search term', count, 'times in postions', pos)
    else:        
        print('Not found search term therefore position -1')

# main program
n = [23, 56, 21, 89, 23, 54, 12, 23, 99]   
sT = int(input('Enter the search term: '))
linearSearch(sT, n)




