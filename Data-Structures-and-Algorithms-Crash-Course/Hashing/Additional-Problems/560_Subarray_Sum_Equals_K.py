import json

class Solution(object):
    """
    Description:
        Given an array of integers nums and an integer k, return the total number 
        of subarrays whose sum equals to k.

        A subarray is a contiguous non-empty sequence of elements within an array.

    Constraints:
        1 <= nums.length <= 2 * 10^4
        -1000 <= nums[i] <= 1000
        -10^7 <= k <= 10^7
        
    """
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict

        counts = defaultdict(int)
        curr, ans = 0, 0
        counts[0] = 1

        for num in nums:
            curr += num
            ans += counts[curr - k]
            counts[curr] += 1
            
        return ans     

def main():
    #Setup of solution with LeetCode example input
    solution = Solution()
    
    with open('./Problem-Inputs/560_Input.json') as f:
        JSON = json.loads(f.read())

    for object in JSON:
        print(f"Input: nums = {object['nums']}, k = {object['k']}")
        output = solution.subarraySum(object['nums'], object['k'])
        print(f"Output: {output}")
        print(f"Expected Output: {object['expected']}")

        if output == object['expected']:
            print("PASS")
        else:
            print("FAIL")
        print()

if __name__ == "__main__":
    main()