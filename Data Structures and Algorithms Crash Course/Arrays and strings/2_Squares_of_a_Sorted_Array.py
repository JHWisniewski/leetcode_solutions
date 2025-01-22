class Solution(object):
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
        #Avoids needing to reverse array and just insert directly into ans
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