
def sumArr(array):
    sum = 0;
    for i in array:
        sum = i + sum
    return sum

a = [1,2,3,4,5,6]
print(sumArr(a))