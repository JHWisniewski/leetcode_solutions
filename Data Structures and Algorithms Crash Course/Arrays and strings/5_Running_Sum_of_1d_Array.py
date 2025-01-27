import json

class Solution(object):
    """
    Constraints:
        1 <= nums.length <= 1000
        -10^6 <= nums[i] <= 10^6
    """
    
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
            
        return prefix

def main():
    #Setup of solution with LeetCode example input
    solution = Solution()
    
    with open('./Problem Inputs/5_Input.json') as f:
        JSON = json.loads(f.read())

    for object in JSON:
        print(f"Input: s = {object['nums']}")
        output = solution.runningSum(object['nums'])
        print(f"Output: {output}\n") 

if __name__ == "__main__":
    main()