import json

class Solution(object):
    """
    Description:
        Given an array of integers nums, you start with an initial positive value startValue.

        In each iteration, you calculate the step by step sum of startValue plus elements 
        in nums (from left to right).

        Return the minimum positive value of startValue such that the step by step sum is 
        never less than 1.
        
    Constraints:
        1 <= nums.length <= 100
        -100 <= nums[i] <= 100
    """

    #Brute force, O(n^2)
    def minStartValue1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        startVal = 1
        prefix = [startVal]
        
        while i < len(nums):
            if nums[i] + prefix[-1] > 0:
                prefix.append(nums[i] + prefix[-1])
                i += 1
            else:
                startVal += 1
                i = 0
                prefix = [startVal]
        
        return startVal

    #O(n) solution
    def minStartValue2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        startVal = total = 0
        
        #Keep just step-by-step calculation in mind
        #All we need is the minium step value
        for num in nums:
            total += num
            startVal = min(startVal, total)

        return -startVal + 1

def main():
    #Setup of solution with LeetCode example input
    solution = Solution()
    
    with open('./Problem Inputs/6_Input.json') as f:
        JSON = json.loads(f.read())

    for object in JSON:
        print(f"Input: nums = {object['nums']}")
        output = solution.minStartValue2(object['nums'])
        print(f"Output: {output}")
        print(f"Expected Output: {object['expected']}")

        if output == object['expected']:
            print("PASS")
        else:
            print("FAIL")
        print()

if __name__ == "__main__":
    main()