class Solution(object):
    """
    Constraints:
    1 <= nums.length <= 1000
    -10^6 <= nums[i] <= 10^6
    """
    
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
            
        return prefix
    
#Setup of solution with LeetCode example input
solution = Solution()

input1 = [1,2,3,4]
input2 = [1,1,1,1,1]
input3 = [3,1,2,10,1]

print(f"Input: nums = {input1}")
print(f"Output: " + str(solution.runningSum(input1)))
print()
print(f"Input: nums = {input2}")
print(f"Output: " + str(solution.runningSum(input2)))
print()
print(f"Input: nums = {input3}")
print(f"Output: " + str(solution.runningSum(input3)))