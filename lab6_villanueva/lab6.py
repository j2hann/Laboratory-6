age = int(input("Enter your age: "))
mem = input("Are you a member? (Type 'Y' for Yes or anything for No): ")

if 0 < age < 18:
    if mem == "Y" or "y":
        print("Your membership fee is: PHP 450.00")
    else:
        print("Your membership fee is: PHP 650.00")
elif 18 <= age <= 65:
    if mem == "Y" or "y":
        print("Your membership fee is: PHP 550.00")
    else:
        print("Your membership fee is: PHP 750.00")
elif 65 <= age <= 120:
    if mem == "Y" or "y":
        print("Your membership fee is: PHP 400.00")
    else:
        print("Your membership fee is: PHP 600.00")
else:
    print("Invalid input. Try again")