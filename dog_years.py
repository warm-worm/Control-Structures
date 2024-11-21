#
## Program that calculates a dog's age in dog's years
# For the first two years, a dog's life is equal to 10.5 human years
# After that, each dog year is equal to 4 human years
#
age = int(input("Enter the dog's age: "))
if age < 0:
    print("The dog hasn't been born yet...")
elif age <= 2:
    human_years1 = int(age * 10.5)
    print(f"The dog's age in human years is {human_years1} y'o.")
elif age > 2:
    human_years2 = int(2 * 10.5 + (age - 2) * 4)
    print(f"The dog's age in human years is {human_years2} y'o.")