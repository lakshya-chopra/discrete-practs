from itertools import permutations,product

def permute(lst:list,repetition=False,r=0):

    """
    r: no of permutations
    """

    if r == 0:
        r = len(lst)


    if not repetition: #if repetititon : FALSE.
        return list(permutations(lst,r))
    
    else:
        return product(lst,repeat=r)
    
if __name__ == "__main__":

    lst = input("Enter all the elements separated by a space: ").split()

    print("Permutations with repetition: ")
    lst1 = permute(lst,repetition=True)
    for i in lst1:
        print(i)

    print("\nWithout repetitions: ")
    lst2 = permute(lst,repetition=False)
    for i in lst2:
        print(i)

"""
1. First import permutations & product generator function from "itertools"
2. In the permute function, take in a list & a boolean value 'repetition', either True or False.
3. If repetition = False, we use the permutations function which returns a generator object, we typecast this to a list and return it.
4. Else we use the product function, and set repeat = length of the list created.
5. Finally, we call this function in the main block and print everything nicely.
"""


