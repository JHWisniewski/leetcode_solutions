import json

class Solution(object):
    """
    Description:
        Given an array of integers nums, calculate the pivot index of this array.

        The pivot index is the index where the sum of all the numbers strictly to the left of the index is 
        equal to the sum of all the numbers strictly to the index's right.

        If the index is on the left edge of the array, then the left sum is 0 because there are no elements 
        to the left. This also applies to the right edge of the array.

        Return the leftmost pivot index. If no such index exists, return -1.

    Constraints:
        1 <= nums.length <= 10^4
        -1000 <= nums[i] <= 1000

    """
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, l_sum, r_sum = 0, 0, 0
        prefix = [nums[0]]

        #Build prefix
        #No other solution without this as far as I can tell
        for j in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[j])

        #Iterate through and compare left sum to right sum
        while i < len(nums):
            l_sum = prefix[i]
            r_sum = prefix[-1] - prefix[i] + nums[i]
        
            if l_sum == r_sum:
                return i
            
            i += 1

        return -1

def main():
    #Setup of solution with LeetCode example input
    solution = Solution()

    with open('./Data-Structures-and-Algorithms/data/arrays-and-strings/724_Input.json') as f:
        JSON = json.loads(f.read())

    for object in JSON:
        print(f"Input: nums = {object['nums']}")
        output = solution.pivotIndex(object['nums'])
        print(f"Output: {output}")
        print(f"Expected Output: {object['expected']}")

        if output == object['expected']:
            print("PASS")
        else:
            print("FAIL")
        print()

if __name__ == "__main__":
    main()
        