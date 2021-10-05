userContinue = input("Do you want to continue? (Y/N) ")
if userContinue == 'no' or userContinue == 'NO' or userContinue == 'n' or userContinue == 'N':
    print("Exiting")
elif userContinue == 'yes' or userContinue == 'YES' or userContinue == 'y' or userContinue == 'Y':
    print("Continuing ...")
    print("Complete")
else:
    print('Please try again and respond yes or no.')