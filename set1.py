# import math
from itertools import product, chain, combinations
from pprint import pprint

class Set:

    def __init__(self,set1:set):
        self.set1 = set1 # variable type: set
        self.size = len(set1)

    def isMemberOf(self,x):
        return True if x in self.set1 else False
    
    def setUnion(self,set2):

        print(x for x in self.set1.union(set2))

    def subset(self,subset_set:set):
        if subset_set.issubset(self.set1):
            return True
        else:
            return False
        
    def powerSet(self):
        # cardinality = (int)(math.pow(2,self.size))
        # pow_set = set()

        # lst = list(self.set1)

        # for i in range(cardinality): #each subset
        #     subset = set() 
        #     # i -> 00.. -> 11.... (eg: 000, 001, 010, 100, 101,....)

        #     for j in range(self.size): #imside each subset

        #         if (i & (1 << j) > 0): # eg : 001 & 100 -> F, 001 & 010 -> F, 001 & 001 -> T, only the lastmost bit (element at that bit) is included.
        #             # loop: 1 << j -> creates all possible combinations of the binary nums, only the combination, whose & with the counter is > 0 (not 0), is added.
        #             subset.add(lst[j])

        #     pow_set.update(subset)
        # return pow_set

        lst = list(self.set1)
        return chain.from_iterable(combinations(lst, r) for r in range(len(lst)+1)) # r -> 0 to len

    def intersection(self,set2:set):
        return self.set1.intersection(set2)
    
    def sDifference(self,set2:set):
        return self.set1.symmetric_difference(set2)
    
    def difference(self,set2:set):
        return self.set1.difference(set2)

    def cartesianProduct(self, set2):
        
        return set(product(self.set1,set2,repeat=1)) #cartesian product.


    def complement(self,universal_set:set):
        return universal_set.difference(self.set1) 
    
    def add_elements(self,set1:set):

        """
        add the elements, if no element is there, then update
        """

        self.set1.update(set1)
        self.size = len(self.set1)
    
    def display(self):
        pprint(self.set1)



def main():

    print("Menu".center(30,"="))
    print("1. Create the global set, over which all the operations will be performed (call it again to update it)")
    print("2. Check if X is an element of this set")
    print("3. Union")
    print("4. Cartesian Product")
    print("5. Subset")
    print("6. Complement")
    print("7. Difference")
    print("8. Symmetric Difference")
    print("9. Intersection ")
    print("10. Powerset")
    print("11. Display the global set")
    print ("12. Exit")

    # ops = {1:"create",2:'check',3:'union',4:'cartesian',5:'subset',6:"complement",7:'diff',8:'sdiff',9:'intersec'}


    #first create a global empty SET object:
    set_obj = Set(set())

    while True:
        ch = int(input("Enter your choice (1,2...11): "))

        if ch == 12:
            break

        elif ch == 11:
            print("The global set is: ")
            set_obj.display()

        elif 2<ch<10 or ch == 1: #for cases where a set has to be made:

            print("\nCreate a set for the specified operation")
            n = int(input("Length: "))

            set_ = set()
            for i in range(n):

                e = int(input("Element (integers only): "))
                set_.add(e)

            match ch:
                
                case 1:
                    set_obj.add_elements(set1=set_)
                case 3:
                    print("Union of these two sets is: ",set_obj.setUnion(set_))
                case 4:
                    print("The Cartesian Product is: ",set_obj.cartesianProduct(set_))
                case 5:
                    val = set_obj.subset(subset_set=set_)
                    if val: print("the given set is a subset")
                    else: print("Not a subset")

                case 6:

                    print("The complement is: ",set_obj.complement(set_))
                
                case 7: 
                    diff = set_obj.difference(set_)

                    print("The difference is: ",diff)

                case 8:

                    sdiff = set_obj.sDifference(set_)

                    print("The symm. difference is: ",sdiff)
                
                case 9:
                    
                    print("The intersection is: ",set_obj.intersection(set_))
                
        elif ch == 10:

            pow_set = set_obj.powerSet()
            print("Power set: ")
            for x in pow_set:
                print(x)

        else:

            e = float(input("Enter the number: "))
            if set_obj.isMemberOf(e):
                print("yes! its a member")
            else:
                print("Nah")

if __name__ == "__main__":
    main()
                


#Code Explanation:
"""
1. Create a class Set, write an init method to set the set values & a parameter which takes in the size.
2. Create instance methods like "isMemberOf", "powerset()" to perform certain set operations.
3. We can use inbuilt methods for these operations, or create our own algorithms for them.
4. Finally in the if __name__ = "__main__" block: create an instance of the Set class & write a menu driven, showing all the possible options, and run the functions as per the user's choices.



"""