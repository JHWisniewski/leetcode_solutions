class Solution(object):
    """
    Constraints:
    n == nums.length
    1 <= k <= n <= 10^5
    -10^4 <= nums[i] <= 10^4
    """
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        curr = ans = 0
        
        #Initial curr
        for i in range(k):
            curr += nums[i]
        
        #Store current average as ans
        ans = float(curr) / k
        
        #Calculate advancing curr with iterative calculations
        #Change window curr by adding new right bound (i) and subtracting old left bound (i - k)
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            ans = max(ans, float(curr) / k)
            
        return ans

#Setup of solution with LeetCode example input
solution = Solution()

input1 = [1,12,-5,-6,50,3]
window_len1 = 4
input2 = [5]
window_len2 = 1
ans1 = solution.findMaxAverage(input1, window_len1)
ans2 = solution.findMaxAverage(input2, window_len2)

print(f"Input: nums = {input1}, k = {window_len1}")
print(f"Output = {ans1:.5f}")
print()
print(f"Input: nums = {input2}, k = {window_len2}")
print(f"Output = {ans2:.5f}")