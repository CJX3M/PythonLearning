farenheit = input("What is the temperature in faraenheit? ")
if not farenheit.isnumeric():
    print("Input is not a number")
    exit()
celsius = (int(farenheit) - 32) * 5/9
print(f"Temperature in celsius is {round(celsius)}")