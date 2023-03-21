import itertools


# Permutations with repetition
def permutations_with(n, list):
    print("\nPermutations with repetition:")
    for p in itertools.product(list, repeat=n):
        print(p)

# Permutations without repetition
def Permutatins_without(n, list):    
    print("\nPermutations without repetition:")
    for p in itertools.permutations(list, n):
        print(p)

if __name__ == '__main__':
    print("Enter the list of elements separated by space: ")
    list = input().split()
    
    print("Enter the length of permutation: ")
    lenght = int(input())  
    
    descision = int(input("1: With repetition \t 2: Without repetition\n"))
    while(descision != 1 and descision != 2):
        print("Invalid input")
        descision = int(input("1: With repetition \t 2: Without repetition\n"))
        
    if(descision == 1):
        permutations_with(lenght, list)
    
    if(descision == 2):
        Permutatins_without(lenght, list)
    