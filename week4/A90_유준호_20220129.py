class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums)==0: return 0
        
        
        i=0 
        for j in range(1,len(nums)):
            if nums[i]!=nums[j]:
                i+=1  
                nums[i]=nums[j]
        
        return i+1