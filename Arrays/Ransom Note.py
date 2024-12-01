class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        Counter = {}
        for c in magazine:
            if c in Counter:
                Counter[c]+=1
            else:
                Counter[c]=1

        
        for c in ransomNote:
            if c not in Counter:
                return False
            elif Counter[c]==1:
                del Counter[c]
            else:
                Counter[c] -= 1


        return True