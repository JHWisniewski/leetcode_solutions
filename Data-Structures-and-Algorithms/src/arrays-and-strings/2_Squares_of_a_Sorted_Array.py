import json

class Solution(object):
    """
    Description:
        Given an integer array nums sorted in non-decreasing order, return an array
        of the squares of each number sorted in non-decreasing order.

    Constraints:
        1 <= nums.length <= 10^4
        -10^4 <= nums[i] <= 10^4
        nums is sorted in non-decreasing order.
        
    """
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Square each element
        for i, num in enumerate(nums):
            nums[i] = num**2

        #Base cases
        if len(nums) == 0 or len(nums) == 1:
            return nums

        #Two pointers for sorting into ans
        i = 0
        j = len(nums) - 1
        
        #Pre-allocate ans array space and set pos index for backwards interation
        #Avoids needing to reverse appended array
        ans = [0] * len(nums)
        pos = len(nums) - 1

        while i <= j:
            if nums[i] >= nums[j]:
                ans[pos] = nums[i]
                i += 1
            else:
                ans[pos] = nums[j]
                j -= 1
            pos -= 1
                
        return ans

def main():
    #Setup of solution with LeetCode example input
    solution = Solution()
    
    with open('./Data-Structures-and-Algorithms/data/arrays-and-strings/2_Input.json') as f:
        JSON = json.loads(f.read())

    for object in JSON:
        print(f"Input: nums = {object['nums']}")
        output = solution.sortedSquares(object['nums'])
        print(f"Output: {output}")
        print(f"Expected Output: {object['expected']}")

        if output == object['expected']:
            print("PASS")
        else:
            print("FAIL")
        print()

if __name__ == "__main__":
    main()