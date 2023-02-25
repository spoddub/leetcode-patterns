class Solution(object):
    def containsDuplicate(self, nums):
        lst = set()
        for i in nums:
            lst.add(i)
        if len(nums) == len(lst):
            return False
        else:
            return True
