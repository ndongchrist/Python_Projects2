def permutations_with_rep(n, list):
    # Permutations with repetition.
    print("\nPermutations with repetition:")
    for i in range(len(list)**n):
        p = []
        for j in range(n):
            p.append(list[i // (len(list)**j) % len(list)])
        print(tuple(p))

def permutations_without_rep(n, list):
    # Permutations without repetition.
    print("\nPermutations without repetition:")
    used = [False] * len(list)
    def permute(p):
        if len(p) == n:
            print(tuple(p))
        else:
            for i in range(len(list)):
                if not used[i]:
                    used[i] = True
                    permute(p + [list[i]])
                    used[i] = False
    permute([])
    
    
print("Enter the list of elements separated by space: ")
list = input().split()
print("Enter the length of permutation: ")
lenght = int(input())

descision = int(input("1: With repetition \t 2: Without repetition\n"))
while(descision != 1 and descision != 2):
    print("Invalid input")
    descision = int(input("1: With repetition \t 2: Without repetition\n"))
    
if(descision == 1):
    permutations_with_rep(lenght, list)

if(descision == 2):
    permutations_without_rep(lenght, list)