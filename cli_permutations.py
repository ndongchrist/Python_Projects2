def permutations():
    print("Enter the list of elements separated by space: ")
    lst = input().split()
    print("Enter the length of permutation: ")
    n = int(input())
    
    # Permutations with repetition.
    print("\nPermutations with repetition:")
    for i in range(len(lst)**n):
        p = []
        for j in range(n):
            p.append(lst[i // (len(lst)**j) % len(lst)])
        print(tuple(p))
    
    # Permutations without repetition.
    print("\nPermutations without repetition:")
    used = [False] * len(lst)
    def permute(p):
        if len(p) == n:
            print(tuple(p))
        else:
            for i in range(len(lst)):
                if not used[i]:
                    used[i] = True
                    permute(p + [lst[i]])
                    used[i] = False
    permute([])
    
    # Combinations with repetition.
    # print("\nCombinations with repetition:")
    # def combine(p, start):
    #     if len(p) == n:
    #         print(tuple(p))
    #     else:
    #         for i in range(start, len(lst)):
    #             combine(p + [lst[i]], i)
                
    # combine([], 0)
    
    # # Combinations without repetition.
    # print("\nCombinations without repetition:")
    # def choose(p, start):
    #     if len(p) == n:
    #         print(tuple(p))
    #     else:
    #         for i in range(start, len(lst)):
    #             choose(p + [lst[i]], i+1)
                
    # choose([], 0)

print("Hr")
permutations()