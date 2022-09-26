class Solution(object):
    def twoSum(self, nums, target):
        
        for i in nums:
            for j in nums:
                if i+j==target and nums.index(i)!=nums.index(j):
                    #print(nums.index(i)!=nums.index(j))
                    return nums.index(i),nums.index(j)
nums=[3,3]
target=6
object=Solution()
sum=object.twoSum(nums,target)
print(sum)