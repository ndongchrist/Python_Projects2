listOfPrime = [2]
def checkPrime(num):
    for i in range(2, 100):
        if num%i == 0:
            pass
        else:
            listOfPrime.append(num)

for num in range(2, 100):
    list = checkPrime(num)
    
print(list)