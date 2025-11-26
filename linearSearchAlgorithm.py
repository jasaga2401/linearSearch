import random
# creating a random non repeated list of integers
items = [i for i in range(100)]
random.shuffle(items)

# search term entered by user
searchTerm = int(input('What is your search term: '))
found = False
position = ''

# loops through every item in the list
for x in range(0, len(items)):
    # checks to see if the item has been found
    if (searchTerm == items[x]):
        found = True
        position = x

if (found == True):
    print(f'Item found at position {position}')
else:
    print('Item not found')
