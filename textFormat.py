# print("Text with a new \n line")
# print("Text with a \t tab")
# print("Text with a return \r carrier")
# print("Text scaping the double quotes \" wrote with double quotes")
# print(r"Text that does not process the scaping \r\n")
# print('''A verbatim text, this one
# accepts more than one line and can easily use single quotes (')
# and double quotes (") without the need to scape them''')
# print("""Just like the ` on javascript. Lets see if it lets us concatenate with variables and transform them
# automatically""")

first = "Conrad"
second = "Grant"
third = "Bob"

print(first, second)
print(first, second, third)
print(first, second, third, sep='-')
print(first, second, third, sep='-', end='-')