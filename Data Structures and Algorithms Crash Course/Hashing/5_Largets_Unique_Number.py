import json

class Solution(object):
    """
    Description:
        Given an integer array nums, return the largest integer that only occurs once. 
        
        If no integer occurs once, return -1.

    Constraints:
        1 <= nums.length <= 2000
        0 <= nums[i] <= 1000
        
    """
    def largestUniqueNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict

        count = defaultdict(int)
        once = []

        for num in nums:
            count[num] += 1

        for num, freq in count.items():
            if freq == 1:
                once.append(num)

        if once:
            return max(once)

        return -1

def main():
    #Setup of solution with LeetCode example input
    solution = Solution()
    
    with open('./Problem Inputs/5_Input.json') as f:
        JSON = json.loads(f.read())

    for object in JSON:
        print(f"Input: nums = {object['nums']}")
        output = solution.largestUniqueNumber(object['nums'])
        print(f"Output: {output}")
        print(f"Expected Output: {object['expected']}")

        if output == object['expected']:
            print("PASS")
        else:
            print("FAIL")
        print()

if __name__ == "__main__":
    main()