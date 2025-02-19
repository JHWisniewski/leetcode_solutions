import json

class Solution(object):
    """
    Description:
        You are given a 0-indexed array nums consisting of positive integers. 
        You can choose two indices i and j, such that i != j, and the sum of 
        digits of the number nums[i] is equal to that of nums[j].

        Return the maximum value of nums[i] + nums[j] that you can obtain 
        over all possible indices i and j that satisfy the conditions. If no 
        such pair of indices exists, return -1.

    Constraints:
        1 <= nums.length <= 10^5
        0 <= nums[i] <= 10^9
        
    """
    def sumDigits(self, n):
        x = 0
        
        while n > 0:
            x += n % 10
            n //= 10

        return x
    
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        curr = 0
        ans = -1

        for num in nums:
            curr = self.sumDigits(num)

            if curr in counts:
                ans = max(ans, counts[curr] + num)
                counts[curr] = max(counts[curr], num)
            else:
                counts[curr] = num
            
            curr = 0

        return ans
            
def main():
    #Setup of solution with LeetCode example input
    solution = Solution()
    
    with open('./Problem-Inputs/2342_Input.json') as f:
        JSON = json.loads(f.read())

    for object in JSON:
        print(f"Input: nums = {object['nums']}")
        output = solution.maximumSum(object['nums'])
        print(f"Output: {output}")
        print(f"Expected Output: {object['expected']}")

        if output == object['expected']:
            print("PASS")
        else:
            print("FAIL")
        print()

if __name__ == "__main__":
    main()