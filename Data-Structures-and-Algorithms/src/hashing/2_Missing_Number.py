import json

class Solution(object):
    """
    Description:
        Given an array nums containing n distinct numbers in the range [0, n], return the only
        number in the range that is missing from the array.

    Constraints:
        n == nums.length
        1 <= n <= 10^4
        0 <= nums[i] <= n
        All the numbers of nums are unique.
        
    """
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)

        for i in range(len(nums) + 1):
            if i not in nums:
                return i

def main():
    #Setup of solution with LeetCode example input
    solution = Solution()
    
    with open('./Data-Structures-and-Algorithms/data/hashing/2_Input.json') as f:
        JSON = json.loads(f.read())

    for object in JSON:
        print(f"Input: nums = {object['nums']}")
        output = solution.missingNumber(object['nums'])
        print(f"Output: {output}")
        print(f"Expected Output: {object['expected']}")

        if output == object['expected']:
            print("PASS")
        else:
            print("FAIL")
        print()

if __name__ == "__main__":
    main()