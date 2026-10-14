my_str = input('Give a string variable:')
output_str = ('')
for index in range(len(my_str)):
    if index % 2 == 0:
        output_str += my_str[index]
print(output_str)