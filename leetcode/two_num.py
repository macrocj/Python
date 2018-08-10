'''
Author: ''
Created on '7/27/2018'
Version: 1.0
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        index = -1
        for x in nums:
            index += 1
            for i in range(index+1,len(nums)):
                if x + nums[i] == target:
                    result.extend([index,i])
        return result
    def twoSum2(self, nums, target):
            dict_temp = dict()
            for index, value in enumerate(nums):
                if target - value in dict_temp:
                    return [dict_temp[target - value], index]
                dict_temp[value] = index



s = Solution()
nums = [2, 7, 11, 15]
print(s.twoSum2(nums, 17))

