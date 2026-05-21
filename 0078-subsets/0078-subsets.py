class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def helper(nums:List[int] , index , curr):
            if index == len(nums):
                ans.append(curr[:])
                return
            curr.append(nums[index])
            helper(nums , index+1 , curr)
            curr.pop()
            helper(nums , index+1 ,curr)
        helper(nums , 0,[])
        return ans 