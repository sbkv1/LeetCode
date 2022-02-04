class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        
        for i in range(len(nums)):
            required = target - nums[i]
            if required in dic:
                return [dic[required], i]
            dic[nums[i]] = i