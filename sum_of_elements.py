# This program provides sum of all the elements of a list while ignoring 7 and it's subsequent.
class Sum :

    def realSum(self, mylist):
        j, sum = 0, 0
        while j < len(mylist) :
            if mylist[j] == 7 :
                j += 2 
            else :
                sum += mylist[j]
                j += 1
        return sum

sum = Sum()
arr = [7,3,7,4,7,1,9]
print("Sum is : ", sum.realSum(arr))