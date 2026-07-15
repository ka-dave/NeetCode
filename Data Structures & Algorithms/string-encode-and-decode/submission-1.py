class Solution:

    def encode(self, strs: list[str]) -> str:
        s = ''

        if len(strs) == 0:
            return ""
        
        for i in strs:
            s += i + "😀"
        
        return s

    def decode(self, s: str) -> list[str]:
        result = []
        
        ori_str = s.rsplit("😀")
        ori_str.pop()
        return ori_str