import json

class Solution(object):
    """
    Description:
        Given a 2D integer array nums where nums[i] is a non-empty array of 
        distinct positive integers, return the list of integers that are 
        present in each array of nums sorted in ascending order.

    Constraints:
        1 <= nums.length <= 1000
        1 <= sum(nums[i].length) <= 1000
        1 <= nums[i][j] <= 1000
        All the values of nums[i] are unique.
        
    """
    def intersection(self, nums):
        """
        :type arr: List[int]
        :rtype: int
        """
        return 0

def main():
    #Setup of solution with LeetCode example input
    solution = Solution()
    
    with open('./Problem Inputs/2248_Input.json') as f:
        JSON = json.loads(f.read())

    for object in JSON:
        print(f"Input: nums = {object['nums']}")
        output = solution.intersection(object['nums'])
        print(f"Output: {output}")
        print(f"Expected Output: {object['expected']}")

        if output == object['expected']:
            print("PASS")
        else:
            print("FAIL")
        print()

if __name__ == "__main__":
    main()