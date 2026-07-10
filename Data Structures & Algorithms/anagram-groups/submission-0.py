class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        h = {}

        for item in strs:
            key = ("".join(sorted(item)))

            if key in h:
                h[key].append(item)
            else:
                h[key] = [item]
        
        return list(h.values())
