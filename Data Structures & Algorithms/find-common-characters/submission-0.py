class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        cnt = Counter(words[0])

        for w in words:
            curr_cnt = Counter(w)
            for c in cnt:
                cnt[c] = min(cnt[c], curr_cnt[c])

        res = []
        for k, v in cnt.items():
            for i in range(v):
                res.append(k)

        return res