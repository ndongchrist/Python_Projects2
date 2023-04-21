# Initialize an array
arr = [1, 2, 3, 4, 5]

# Shift the array to the right by 2 positions in place
for i in range(2):
    temp = arr[-1]
    for j in range(len(arr) - 1, 0, -1):
        arr[j] = arr[j - 1]
    arr[0] = temp

# Print the shifted array
print(arr)