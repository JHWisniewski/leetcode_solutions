import os

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
        denom = 2 * k + 1
        ans = []

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
                ans.append((prefix[right] - prefix[left] + nums[left]) // denom)

        return ans
    
    def getAverages2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        i = 0
        total = 0
        ans = []
        denom = 2 * k + 1
        
        #Sliding window implementation with bound tests
        #Step-by-step addition without use of a prefix
        while i < len(nums):
            left = i - k
            right = i + k

            if left < 0 or right >= len(nums):
                total += nums[i]
                ans.append(-1)
                i += 1
            elif i == k:
                for j in range(i, right + 1):
                    total += nums[j]
                ans.append(total // denom)
                total -= nums[left]
                i += 1
            else:
                total += nums[right]
                ans.append(total // denom)
                total -= nums[left]
                i += 1

        return ans        

def main():
    #Setup of solution with LeetCode example input
    solution = Solution()
    
    with open('./Problem Inputs/7_Input.md') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        input_nums, input_k = line.split(", ")  # Split by the delimiter ", "

        nums = eval(input_nums)
        k = int(input_k)
        output = solution.getAverages2(nums, k)
        
        print(f"Input: nums = {nums}, k = {k}")
        print(f"Output: {output}\n")     

if __name__ == "__main__":
    main()


""" input1 = [7,4,3,9,1,8,5,2,6]
k1 = 3
input2 = [100000]
k2 = 0
input3 = [8]
k3 = 100000

print(f"Input: nums = {input1}, k = {k1}")
print(f"Output: " + str(solution.getAverages2(input1, k1)))
print()
print(f"Input: nums = {input2}, k = {k2}")
print(f"Output: " + str(solution.getAverages2(input2, k2)))
print()
print(f"Input: nums = {input3}, k = {k3}")
print(f"Output: " + str(solution.getAverages2(input3, k3))) """