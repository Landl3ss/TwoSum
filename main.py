class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            print(complement)
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]