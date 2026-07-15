class Solution:

    def encode(self, strs: list[str]) -> str:
        s = ''

        for i in strs:
            s += i + "😀"
        return s

    def decode(self, s: str) -> list[str]:
        result = []
        
        ori_str = s.split("😀")
        ori_str.pop()
        return ori_str