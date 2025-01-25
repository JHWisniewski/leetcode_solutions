class Solution(object):
    """
    Constraints:
    n == nums.length
    1 <= n <= 10^5
    0 <= nums[i], k <= 10^5
    """

    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        prefix = [nums[0]]
        ans = []
        denom = 2 * k + 1

        #Build prefix
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
        
        #Sliding window implementation with bound tests
        for i in range(len(nums)):
            left = i - k
            right = i + k

            if left < 0 or right >= len(nums):
                ans.append(-1)
            else:
                #Account for current left element in step-by-step sum
                ans.append(prefix[right] - prefix[left] + nums[left] // denom)

        return ans
    
#Setup of solution with LeetCode example input
solution = Solution()

input1 = [7,4,3,9,1,8,5,2,6]
k1 = 3
input2 = [100000]
k2 = 0
input3 = [8]
k3 = 100000

print(f"Input: nums = {input1}, k = {k1}")
print(f"Output: " + str(solution.getAverages(input1, k1)))
print()
print(f"Input: nums = {input2}, k = {k2}")
print(f"Output: " + str(solution.getAverages(input2, k2)))
print()
print(f"Input: nums = {input3}, k = {k3}")
print(f"Output: " + str(solution.getAverages(input3, k3)))