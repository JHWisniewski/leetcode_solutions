class Solution(object):
    """
    Constraints:
    n == nums.length
    1 <= k <= n <= 10^5
    -10^4 <= nums[i] <= 10^4
    """
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        curr = ans = 0
        
        #Initial curr
        for i in range(k):
            curr += nums[i]
        
        #Store current average as ans
        ans = float(curr) / k
        
        #Calculate advancing curr with iterative calculations
        #Change window curr by adding new right bound (i) and subtracting old left bound (i - k)
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            ans = max(ans, float(curr) / k)
            
        return ans

def main():
    #Setup of solution with LeetCode example input
    solution = Solution()
    
    with open('./Problem Inputs/3_Input.md') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        input_nums, input_k = line.split(", ")  # Split by the delimiter ", "

        nums = eval(input_nums)
        k = int(input_k)
        output = solution.findMaxAverage(nums, k)
        
        print(f"Input: nums = {nums}, k = {k}")
        print(f"Output: {output:.5f}\n")

if __name__ == "__main__":
    main()