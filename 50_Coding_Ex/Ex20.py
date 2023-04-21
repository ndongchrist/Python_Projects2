# Initialize an array
arr = [1, 2, 3, 4, 5]

# Rotate the array to the left by 1 position
temp = arr[0]  # store the first element in a temporary variable
for i in range(len(arr) - 1):
    arr[i] = arr[i + 1]  # shift each element to the left by 1 position
arr[-1] = temp  # set the last element to the temporary variable

# Print the rotated array
print(arr)