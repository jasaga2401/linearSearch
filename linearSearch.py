#26/11/25
#Greg Allcock
#Linear Search Program

def inputValidation():
    while True:
        try:
            userInput = int(input("Enter an integer: "))
            return userInput
        except:
            print("Please input an integer.")

def linearSearch(nList, searchTerm):
    count = 0
    
    # loops through every data element in the list
    for x in range(len(nList)):
    
        # checks to see if the search term is in the list
        if (searchTerm == nList[x]):
            count = count + 1
            
    # checks to see what the value of found is?
    if (count > 0):
        return(f'Found data item {count} times')

    else:
        return('Not found data item')

def main():
    nList = [12, 43, 77, 98, 23, 72, 88, 77, 77, 77, 77]

    try:
        print(linearSearch(nList, inputValidation()))
        
    except Exception as e:
        print(f"Error of {e} type")

if __name__ == "__main__":
    main()
