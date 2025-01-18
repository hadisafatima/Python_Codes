# This program checks if a list has two consecutive 4s in it or not, if yes it returns "True" or "False" otherwise.

class Consecutive4s :
    def has44(self, arr):
        
        for i in range(len(arr) - 1) :
            if arr[i] == 4 and arr[i + 1] == 4 :
                return "True"
            
        return "False"

fours = Consecutive4s()
arr = [1,2,3,4,4,10,1,10]
print(fours.has44(arr))