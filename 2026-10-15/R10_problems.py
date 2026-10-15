#############################################################################
# Problem 1:
# For each of the following expressions, what is the order of growth class that best describes it?

# a) 8n
# Theta(n)

# b) 3n**2 + 7n**3 + 4
# Theta(n**3)

# c) 5log(n) + 5n
# Theta(log(n))

# d) 3**n + n**2
# Theta(3**n)

# e) 20n + nlog(n)
# Theta(nlog(n))

# f) 5 + 60
# Theta(1)

# g) log(n) + 4n
# Theta(n)


#############################################################################
# Problem 2:
# Rank the following functions by runtime complexity. Note some may have the same runtime complexity.

# f(n) = n**2 + 4n + 2
# Theta(n**2)

# g(n) = log(n**2)
# Theta(log(n))

# h(n) = log2(n)  (i.e. read as log base 2 n)
# Theta(log(n))

# j(n) = 3n**3 + 2
# Theta(n**3)

# l(n) = n!
# Theta(n**n)

# k(n) = 2**n
# Theta(2**n)

# Ranked from fastest to slowest:
# g(n) = h(n) > f(n) > j(n) > k(n) > l(n)


#############################################################################
# Problem 3:
# What is the time complexity for the following programs? 

def program1(my_list):
    my_list_even= []
    for i in range(len(my_list)):
        if i % 2 == 0:
            my_list_even.append(i)
    return my_list
# Theta(n)

def program2(my_list):
    my_second_list = [1,2,3,4,5,7]
    
    output_list1 = [i for i in my_list]

    output_list2 = []
    for i in my_list:
        for j in my_second_list:
            output_list2 += [i,j]
    
    return (output_list1, output_list2)
# Theta(n**2)

def program3(n):
    epsilon = 0.01
    low = 0
    high = n
    ans = (high + low) / 2 
    
    while abs(ans**4 - n) >= epsilon:
        if ans**4 > n:
            high = ans 
        else: 
            low = ans
        ans = (high + low) / 2
    return ans
# Theta(log(n))


#############################################################################
# Problem 4:
# Describe two ways to construct an algorithm to find the maximum number is a list. 
# One algorithm should have time complexity O(n), the other O(n**2). (Note the 
# O(n**2) algorithm is highly inefficient and we'd never actually use it 
# in practice).

maximum = list1[0]
for n1 in list1:
    if n1 > maximum:
        maximum = n1
print(maximum)
# Theta(n)

for n1 in list1:
    maximum = n1
    for n2 in list1:
        if maximum < n2:
            break
print(maximum)
# Theta(n**2)
