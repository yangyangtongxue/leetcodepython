class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used_char = {} #字符的映射
        start = 0  #重复位置
        res = 0  #结果
        for num, char in enumerate(s):  
            if char in used_char and used_char[char]>=start:  #字符在使用的映射中，且该字符在窗口中
                start = used_char[char]+1 #重置重复位置
            else:
                res = max(res,num-start+1)  #计算结果
            used_char[char] = num  #字符映射更新
        return res