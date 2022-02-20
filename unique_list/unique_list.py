user_list = []



print("Enter -1 to quit")

# Get user input to initiate loop
user_input = int(input("Enter the first number: "))
user_list.append(user_input)

# while user input is positive add to list

while(user_input > 0):
    user_input = int(input("Next: "))
    if(user_input == -1):
      break
    user_list.append(user_input)


# sets MUST CONTAIN unique values
if(len(set(user_list)) == len(user_list)):

   print(f"The sequence {user_list} is unique!")
else:
   print(f"The sequence {user_list} is NOT unique!")