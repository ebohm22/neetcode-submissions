class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        forw = 0
        back = 0
        while numbers[forw] + numbers[length-back-1] != target:
            if numbers[forw] + numbers[length-back-1] > target:
                back +=1
            else:
                forw+=1
        return [forw+1,length-back]


        