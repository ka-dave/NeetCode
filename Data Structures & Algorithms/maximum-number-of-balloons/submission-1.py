class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        word = 'balloon'
        hashmap_text = {}
        hashmap_word = {}
        res = float('inf')

        for i in text:
            hashmap_text[i] = hashmap_text.get(i,0) + 1

        for i in word:
            hashmap_word[i] = hashmap_word.get(i,0) + 1

        for i in hashmap_word:
            res = min(res, hashmap_text.get(i, 0) // hashmap_word[i])
        return res