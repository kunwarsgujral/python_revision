# Take input eg: 39 
# Example output 
# 3 + 9 = 12 
# 12

user_input = input("Enter a two digit number:")
first_input_as_int = int(user_input[0])
second_input_as_int = int(user_input[1])

sum = first_input_as_int + second_input_as_int
print(f"{first_input_as_int} +"+f" {second_input_as_int} = {sum}")

print(sum)
