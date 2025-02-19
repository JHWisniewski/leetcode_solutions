import json

class Solution(object):
    """
    Description:
        Given an array of positive integers nums and a positive integer target, return the minimal length of a 
        subarray whose sum is greater than or equal to target. 
        
        If there is no such subarray, return 0 instead.

    Constraints:
        1 <= target <= 10^9
        1 <= nums.length <= 10^5
        1 <= nums[i] <= 10^4

    """
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left, right, curr = 0, 0, 0

        #Set to minimum impossible value
        ans = len(nums) + 1
        
        #Run through nums
        while right < len(nums):
            curr += nums[right]

            if curr < target:
                right += 1
            else:
                while curr >= target:
                    ans = min(ans, right - left + 1)
                    curr -= nums[left]
                    left += 1

                right += 1
        
        #All feasible options exhausted
        if ans == len(nums) + 1:
            return 0

        return ans

def main():
    #Setup of solution with LeetCode example input
    solution = Solution()

    with open('./Problem Inputs/209_Input.json') as f:
        JSON = json.loads(f.read())

    for object in JSON:
        print(f"Input: target = {object['target']}, nums = {object['nums']}")
        output = solution.minSubArrayLen(object['target'], object['nums'])
        print(f"Output: {output}")
        print(f"Expected Output: {object['expected']}")

        if output == object['expected']:
            print("PASS")
        else:
            print("FAIL")
        print()

if __name__ == "__main__":
    main()
        