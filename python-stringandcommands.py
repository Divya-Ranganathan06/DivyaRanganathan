# Input string
input = "PRADEEP"

# Ensure the string is not empty
if len(input) > 3:
    # Create a new string from the first, middle, and last character
    output = input[0] + input[len(input) // 2] + input[-1]
    print(output)  # Output: PDP
else:
    print("string should contain atleat 3 characters")
