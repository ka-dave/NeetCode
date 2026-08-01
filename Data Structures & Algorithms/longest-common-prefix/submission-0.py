class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count = 0 

        for item in zip(*strs):
            if len(set(item)) == 1:
                count +=1 
            else:
                break

        return strs[0][:count]