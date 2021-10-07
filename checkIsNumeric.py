# numericValue = '7'
# print(numericValue.isnumeric())

# numericValue = 'Bob'
# print(numericValue.isnumeric())

first_value = input("First number: ")
second_value = input("Second number: ")

if first_value.isnumeric() == False or second_value.isnumeric() == False:
    print("Value is not a number")
    exit()


# if second_value.isnumeric() == False:
#     print("Value is not a number")
#     exit()

first_value = int(first_value)
second_value = int(second_value)

sum = first_value + second_value
print("Sum: " + str(sum))