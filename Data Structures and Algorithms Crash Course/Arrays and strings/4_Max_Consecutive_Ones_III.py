class Solution(object):
    """
    Constraints:
    1 <= nums.length <= 10^5
    nums[i] is either 0 or 1.
    0 <= k <= nums.length
    """
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = curr = ans = 0
        
        for right, num in enumerate(nums):
            if num == 0:
                curr += 1
            
            while curr > k:
                if nums[left] == 0:
                    curr -= 1
                left += 1
                
            ans = max(ans, right - left + 1)
            
        return ans

def main():
    #Setup of solution with LeetCode example input
    solution = Solution()
    
    with open('./Problem Inputs/4_Input.md') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        input_nums, input_k = line.split(", ")  # Split by the delimiter ", "

        nums = eval(input_nums)
        k = int(input_k)
        output = solution.longestOnes(nums, k)
        
        print(f"Input: nums = {nums}, k = {k}")
        print(f"Output: {output}\n")

if __name__ == "__main__":
    main()