import json

class Solution(object):
    """
    Description:
        Given an array of integers nums and an integer k. A continuous subarray 
        is called nice if there are k odd numbers on it.

        Return the number of nice sub-arrays.

    Constraints:
        1 <= nums.length <= 50000
        1 <= nums[i] <= 10^5
        1 <= k <= nums.length
        
    """
    def numberOfSubarrays(self, nums, k):
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
            curr += num % 2
            ans += counts[curr - k]
            counts[curr] += 1

        return ans

def main():
    #Setup of solution with LeetCode example input
    solution = Solution()
    
    with open('./Data-Structures-and-Algorithms/data/hashing/1248_Input.json') as f:
        JSON = json.loads(f.read())

    for object in JSON:
        print(f"Input: nums = {object['nums']}, k = {object['k']}")
        output = solution.numberOfSubarrays(object['nums'], object['k'])
        print(f"Output: {output}")
        print(f"Expected Output: {object['expected']}")

        if output == object['expected']:
            print("PASS")
        else:
            print("FAIL")
        print()

if __name__ == "__main__":
    main()