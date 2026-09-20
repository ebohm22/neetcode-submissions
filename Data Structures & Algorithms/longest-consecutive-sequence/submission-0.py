class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nSet = set(nums)
        count = 0

        for num in nSet:
            if (num-1) not in nSet:
                length = 1
                while(num+length) in nSet:
                    length+=1
                count = max(length,count)

        return count
        