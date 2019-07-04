##两数之和
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for num,i in enumerate(nums):
            if (target-i)  in dic:
                return [i,dic[target-i]]
            else:
                dic[i] = num
        return []
        
