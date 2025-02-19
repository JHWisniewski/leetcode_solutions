import json

class Solution(object):
    """
    Description:
        Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr. 
        
        If there are duplicates in arr, count them separately.

    Constraints:
        1 <= arr.length <= 1000
        0 <= arr[i] <= 1000
        
    """
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        from collections import Counter

        nums = Counter(arr)
        ans = 0

        for num in nums:
            if num + 1 in nums:
                ans += nums[num]

        return ans

def main():
    #Setup of solution with LeetCode example input
    solution = Solution()
    
    with open('./Data-Structures-and-Algorithms/data/hashing/3_Input.json') as f:
        JSON = json.loads(f.read())

    for object in JSON:
        print(f"Input: arr = {object['arr']}")
        output = solution.countElements(object['arr'])
        print(f"Output: {output}")
        print(f"Expected Output: {object['expected']}")

        if output == object['expected']:
            print("PASS")
        else:
            print("FAIL")
        print()

if __name__ == "__main__":
    main()