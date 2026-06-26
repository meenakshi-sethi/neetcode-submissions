class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (n*2) #defining length of new array having all elements as zero so that in only 3 iteration it do the assignment.

        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        return ans

