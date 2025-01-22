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
        ans = []

        while i <= j:
            if nums[i] >= nums[j]:
                ans.append(nums[i])
                i += 1
            else:
                ans.append(nums[j])
                j -= 1
                
        #Two pointers for reversing ans array
        i = 0
        j = len(ans) - 1
        
        while i < j:
            temp = ans[i]
            ans[i] = ans[j]
            ans[j] = temp
            i += 1
            j -= 1
                
        return ans