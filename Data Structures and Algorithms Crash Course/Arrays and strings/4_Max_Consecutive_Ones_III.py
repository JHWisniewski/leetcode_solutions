class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = curr = ans = 0
        
        for right, num in enumerate(nums):
            if num == 0:
                curr += 1
            
            while curr > k:
                if nums[left] == 0:
                    curr -= 1
                left += 1
                
            ans = max(ans, right - left + 1)
            
        return ans

solution = Solution()

input1 = [1,1,1,0,0,0,1,1,1,1,0]
max_flips1 = 2
input2 = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
max_flips2 = 3

print(f"Input: nums = {input1}")
print(f"Output: " + str(solution.longestOnes(input1, max_flips1)))
print()
print(f"Input: nums = {input2}")
print(f"Output: " + str(solution.longestOnes(input2, max_flips2)))