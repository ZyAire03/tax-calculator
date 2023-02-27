# list that contains anywthing you want (array in JS)

# empty list
empty = []

# list of strings 
acronyms = ['LOL', 'IDK', 'TBH']

# list of numbers 

numbers = [ 5,10,15,20]

# list of mix items 
anything = [5,'SDK', 10.5]

# list of list
nesting= [[1,2,3], ['idk', 'WTM', 'HI']]

# getting item from nested list 
menus = [['Egg sandwich', 'Bagle', 'Coffee'],
         ['BLT', 'PB&J', 'Turkey Sandwich']]
print(menus[0],[1]) 
# prints bagle

# add items with method append 
anything.append('BYE')

# remove item with methid remove or del
numbers.remove(20)
# with the string 
del numbers[0]
# with the index num 

# check if value is in the list 
if 1 in [1,2,3,4,5]:
    print('True')

# loops 

# for 
for anythings in anything:
    print (anythings)
    # prints items in the list sepratly 
# range -generate a sequence (give a start, stop, step)
range(7)

# range/for

for i in range(7):
    print(i)
