##a new string made of an input string’s first, middle, and last character.
input = "PRADEEP"
# Ensure the string is not empty
if len(input) >= 3:
    # Create a new string from the first, middle, and last character
    output = input[0] + input[len(input) // 2] + input[-1]
    print(output)  # Output: PDP
else:
    print("string should contain atleat 3 characters")


##a new string made of the middle three characters of an input string.
# Input string
input = "PRADEEP"
# Ensure the string length is at least 3 characters
if len(input) >= 3:
    # Calculate the starting index for the middle three characters
    mid = len(input) // 2
    # Extract the middle three characters
    middle_three = input[(len(input) // 2)-1] + input[len(input) // 2] + input[(len(input) // 2)+1]
    # Print the new string
    print(middle_three)  # Output: ADE
else:
    print("Input should contain atleast 3 characters")


##a new string str3 by appending str2 in the middle of str1.
# Input strings
str1 = "STAR"
str2 = "SUPER"
# Calculate the middle index of str1
middle_index = len(str1) // 2
# Create the new string by inserting str2 in the middle of str1
str3 = str1[:middle_index] + str2 + str1[middle_index:]
# Print the new string
print(str3)  # Output: STSUPERAR


