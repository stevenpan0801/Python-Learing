# Problem 1 - Bisection Search Practise
# Write a program using bisection search to find the forth root of a number inputted by the
# user. Print the forth root calculated with max error of 0.01.

x = float(input("Using bisection search calculate the forth root of: " ))
epsilon = 0.01
low = 0
high = max(x, 1)
ans = (low + high) / 2

while abs(ans**4 - x) > epsilon:
    if ans**4 > x:
        high = ans
        ans = (low + high) / 2
    else:
        low = ans
        ans = (low + high) / 2

print("Forth root of " + str(x) + " is approximately " + str(ans))


# Problem 2 - Functions
# Write a Python function to check whether a number falls in a given range.
def check(x, a, b):
    x = int(input('Enter a number:'))
    a = int(input('Enter the smaller number of the range:'))
    b = int(input('Enter the larger number of the range:'))
    if a <= x <= b:
        return True
    else:
        return False

print(check(x, low, high))


# Problem 3 - Functions
# Write a Python function to check whether a number is perfect or not.
# (In number theory, a perfect number is a positive integer that is equal
# to the sum of its proper positive divisors, excluding the number itself).
def check(x):
    sum = 0
    for i in range(1, x+1):
        if x % i == 0:
            sum += i
    if sum == x:
        return 'perfect'
    else:
        return 'not perfect'

x = int(input('Enter a number:'))
print(check(x))


# Problem 4 - Approximation Algorithm (see Lecture 5 slides for similar problem)
# Write an approximation algorithm to calculate the forth root of some 
# number inputted by the user. 
# Print the result and the number of iterations required to reach that result. 
# The program should not accept negative numbers. Initial parameters epsilon 
# (i.e. accuracy), initial guess, increment and num_guesses are defined below.

# example initial parameters
epsilon = 0.01
ans = 0.0
increment = 0.001
num_guesses = 0
x = float((input('Enter a number:')))

if x < 0:
    print('Invalid input')

else:
    while abs(x - ans**4) >= epsilon and ans**4 < x:
        ans += epsilon
        num_guesses += 1

    if abs(x - ans**4) < epsilon:
        print("ans:", ans)
        print("number guesses:", num_guesses)

    else:
        print("number guesses:", num_guesses)
        print("Failed to calculate approximate square root within " + str(epsilon))

