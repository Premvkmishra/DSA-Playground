from collections import defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = defaultdict(int)
        Balloon = 'balloon'
        for c in text:
            if c in Balloon:
                counter[c] +=1

        return min(counter['b'],
                   counter['a'],
                   counter['l']//2,
                   counter['o']//2,
                   counter['n']
                   )
