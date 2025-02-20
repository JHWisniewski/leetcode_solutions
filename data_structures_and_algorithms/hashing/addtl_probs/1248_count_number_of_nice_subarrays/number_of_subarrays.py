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
    def number_of_subarrays(self, nums, k):
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
    path = './data_structures_and_algorithms/hashing/addtl_probs/1248_count_number_of_nice_subarrays/input.json'

    with open(path, encoding = "utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: nums = {item['nums']}, k = {item['k']}")
        output = solution.number_of_subarrays(item['nums'], item['k'])
        print(f"Output: {output}")
        print(f"Expected Output: {item['expected']}")

        if output == item['expected']:
            print("PASS")
        else:
            print("FAIL")
        print()

if __name__ == "__main__":
    main()
