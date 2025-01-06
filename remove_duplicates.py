class Solution:
	def removeDuplicates(self, s):
         seen = set() 
         results = []

         for char in s:
              if char not in seen :
                   seen.add(char)
                   results.append(char)
        
         return " ".join(results)
     
# making object
sol = Solution()
# printing the returned value
print(sol.removeDuplicates("GeEksforgeEkS"))