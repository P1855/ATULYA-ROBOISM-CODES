class Solution:
   def solve(self, nums):
      max=0
      length=len(nums)
      for i in range(0,length-1):
         count=1
         for j in range(i+1,length):
            if(nums[i]==nums[j]):
               count+=1
               if(max<count):
                  max=count
      return max
sol = Solution()
input_elements = input ("Enter the elements of array with spaces between them :")
highestfrequency = input_elements.split()
print(sol.solve(highestfrequency))
