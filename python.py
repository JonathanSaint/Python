

#Age verifying system for voters in Uganda
print("Welcome to the pollstation")
name = input("What is your name? ")
age = int(input("What is your age? "))
print(f"You are {age} years old")
if age >= 18:
    print(f"{name}, You are eligible to vote! ")
else:
    print(f"Oh nooo{name}  Try again next year")