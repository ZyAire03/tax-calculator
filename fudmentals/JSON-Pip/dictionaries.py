# dictionaries is like a list that can content anyting (numbers, strings, both and other objects) like object in JS

# ex
animals = {'lion': 2, 'shark': 8, 'bear':9}

# ex. of empty dic

bars = {}
# adding value to an key

animals['lion'] = 'laugh out loud'
print(animals)

# printing the value 
print(animals['bear'])

# deleting values 
del animals['bear']
print(animals)

# to get a value that might now be there 

defi = animals.get('cat')
print(defi)

# dic nesting lists 

menus = { 'Breakfast':['Egg sandwich', 'Bagle', 'Coffee'],
          'Lunch': ['BLT', 'PB&J', 'Turkey Sandwich']}
print('Brekfast Menu: \t', menus['Breakfast'])

# another way of dsiplaying

for name, menu in menus.items():
    print(name, ':', menu)