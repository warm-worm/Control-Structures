###
# Checking if both people are adults
#
person1_name = input("Enter the first person's name: ")
person1_age = int(input("Enter first person's age: "))
person2_name = input("Enter the second person's name: ")
person2_age = int(input("Enter second person's age: "))
if person1_age >= 18 and person2_age >= 18:
    print(f'Both {person1_name} and {person2_name} are adults.')
elif person1_age < 18 and person2_age >= 18:
    print(f'{person2_name} is an adult while {person1_name} is not.')
elif person1_age >= 18 and person2_age < 18:
    print(f'{person1_name} is an adult while {person2_name} is not.')
else:
    print(f'Neither {person1_name} nor {person2_name} are adults.')
