first_value = '  FIRST challenge         '
second_value = '-  second challenge  -'
third_value = 'tH IR D-C HALLE NGE'

fourth_value = 'fourth'
fifth_value = 'fifth'
sixth_value = 'sixth'

# First challenge
# first_value = first_value.strip().title().rjust(22)
first_value = f'{first_value.strip().title():^30}'

# Second challenge
second_value = second_value.replace('-', '').strip().capitalize()

# Third challenge
# third_value = third_value.replace(' ', '').capitalize().replace('-', ' ').rjust(30)
third_value = f'''{third_value.replace(" ", "").capitalize().replace('-', ' '):>30}'''

print(first_value)
print(second_value)
print(third_value)

# Fourth challenge - use only the print() function (no f-strings)
# print("{}#{}#{}!".format(fourth_value, fifth_value, sixth_value))
print(fourth_value, fifth_value, sixth_value, sep='#', end='!')

# Fifth challenge - use only a single print() function.  Create tabs and new lines using f-strings
print(f"\t{fourth_value}\n\t{fifth_value}\n\t{sixth_value}")