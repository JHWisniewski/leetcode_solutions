import json

class Solution(object):
    """
    Description:
        Given a binary array nums, return the maximum length of a 
        contiguous subarray with an equal number of 0 and 1.

    Constraints:
        1 <= nums.length <= 10^5
        nums[i] is either 0 or 1.
        
    """
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        
        counts = defaultdict(int)
        curr, ans = 0, 0
        counts[0] = -1

        for i, num in enumerate(nums):
            curr += 1 if num == 1 else -1
            
            if curr in counts:
                ans = max(ans, i - counts[curr])
            else:
                counts[curr] = i

        return ans
    
    def findMaxLengthHard(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        
        diff, ans = 0, 0
        diff_ind = defaultdict(int)

        for i, num in enumerate(nums):
            if num == 0:
                diff += 1
            else:
                diff -= 1

            if diff not in diff_ind:
                diff_ind[diff] = i

            if diff == 0:
                ans = i + 1
            else:
                ans = max(ans, i - diff_ind[diff])

        return ans

def main():
    #Setup of solution with LeetCode example input
    solution = Solution()
    
    with open('./Data-Structures-and-Algorithms/data/hashing/7_Input.json') as f:
        JSON = json.loads(f.read())

    for object in JSON:
        print(f"Input: nums = {object['nums']}")
        output = solution.findMaxLength(object['nums'])
        print(f"Output: {output}")
        print(f"Expected Output: {object['expected']}")

        if output == object['expected']:
            print("PASS")
        else:
            print("FAIL")
        print()

if __name__ == "__main__":
    main()