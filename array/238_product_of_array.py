class Solution(object):
    def productExceptSelf(self, nums:list):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre, post = [], []
        
        for index, val in enumerate(nums):
            pre.append(val if index == 0 else pre[index - 1] * val)
        print(pre)
        for index, val in enumerate(reversed(nums)):
            post.insert(0, val if index == 0 else post[0] * val)
            
        res = []
     
        for index in range(len(nums)):
            if index == 0:
                output = post[index + 1]
            elif index == len(nums) - 1:
                output = pre[index - 1]
            else:
                output = pre[index - 1] * post[index + 1]
            res.append(output)
        return res
    
obj = Solution()
res = obj.productExceptSelf([1,2,3,4])
print(res)
            
        