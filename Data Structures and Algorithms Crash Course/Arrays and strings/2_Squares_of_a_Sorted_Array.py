class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Square each element
        for i, num in enumerate(nums):
            nums[i] = num**2

        #Base cases
        if len(nums) == 0 or len(nums) == 1:
            return nums

        #Two pointers for sorting into ans
        i = 0
        j = len(nums) - 1
        
        #Pre-allocate ans array space and set pos index for backwards interation
        #Avoids needing to reverse appended array
        ans = [0] * len(nums)
        pos = len(nums) - 1

        while i <= j:
            if nums[i] >= nums[j]:
                ans[pos] = nums[i]
                i += 1
            else:
                ans[pos] = nums[j]
                j -= 1
            pos -= 1
                
        return ans

#Setup of solution with LeetCode example input
solution = Solution()

input1 = [-4,-1,0,3,10]
input2 = [-7,-3,2,3,11]

print(f"Input: nums = {input1}")
print(f"Output: " + str(solution.sortedSquares(input1)))
print()
print(f"Input: nums = {input2}")
print(f"Output: " + str(solution.sortedSquares(input2)))