###
# Calculates the sum of even numbers from 1 to a given number N
# Replace the 'for' statement with a 'while' statement
#
N = 10
sum_even = 0
i = 1 

# Calculate the sum of even numbers
while i in range(1, N + 1):
    if i % 2 == 0:
        sum_even += i
    i+=1

print(f"The sum of even numbers from 1 to {N} is: {sum_even}")
