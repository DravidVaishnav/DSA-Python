# string formating using %, format and f string literal
city = 'Mumbai'
state = 'Maharashtra'

# %
print('%s is a famous city of %s'%(city,state))

# format
print('{0} is a famous city of {1}'.format(city,state))

# f string literal
print(f'{city} is a famous city of {state}')
print(f'{city} converted to lower case is {city.lower()}')
