class Solution(object):
    """
    Constraints:
    1 <= nums.length <= 100
    -100 <= nums[i] <= 100
    """

    #Brute force, O(n^2)
    def minStartValue1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        startVal = 1
        prefix = [startVal]
        
        while i < len(nums):
            if nums[i] + prefix[-1] > 0:
                prefix.append(nums[i] + prefix[-1])
                i += 1
            else:
                startVal += 1
                i = 0
                prefix = [startVal]
        
        return startVal

    #O(n) solution
    def minStartValue2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        startVal = total = 0
        
        #Keep just step-by-step calculation in mind
        #All we need is the minium step value
        for num in nums:
            total += num
            startVal = min(startVal, total)

        return -startVal + 1

#Setup of solution with LeetCode example input
solution = Solution()

input1 = [-3,2,-3,4,2]
input2 = [1,2]
input3 = [1,-2,-3]

print(f"Input: nums = {input1}")
print(f"Output: " + str(solution.minStartValue2(input1)))
print()
print(f"Input: nums = {input2}")
print(f"Output: " + str(solution.minStartValue2(input2)))
print()
print(f"Input: nums = {input3}")
print(f"Output: " + str(solution.minStartValue2(input3)))