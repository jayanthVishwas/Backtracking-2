#time = o(n*2^len(nums))  space=O(nums)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(pos, sub):
            
            res.append(sub.copy())

            for i in range(pos, len(nums)):
                sub.append(nums[i])
                helper(i+1, sub)
                sub.pop()

        helper(0,[])
        return res
