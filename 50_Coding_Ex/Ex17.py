number = input("Enter a number-> ")
number.split(" ")
list = []
for i in number:
    a = int(i)
    list.append(a)

sum = 0
for i in list:
    sum = i + sum
    
print(sum)