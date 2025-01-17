# This program returns the intersection of two sorted arrays/lists

class Solution:
    def intersection(self, arr1, arr2):
        i = 0
        j = 0
        intersected = []
        
        while i < len(arr1) and j < len(arr2) :
            if arr1[i] < arr2[j] :
                i += 1
            elif arr1[i] > arr2[j] :
                j += 1
            else :
                if len(intersected) == 0 or intersected[-1] != arr1[i] :
                    intersected.append(arr1[i])
                i += 1
                j += 1

        return intersected
    
sol = Solution()
list1 = [1,2,3,4,5]
list2 = [2,4,6,8,9]
print(sol.intersection(list1, list2))