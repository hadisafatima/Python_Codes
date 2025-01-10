# This program returns the minimum and maximum elements of a list

class Solution:
    def get_min_max(self, arr):
        min = max = arr[0]
        for num in arr :
            if num < min :
                min = num
            if num > max :
                max = num
        
        return min, max
    
sol = Solution()
print(sol.get_min_max([-6,1,2,5,7,900]))