class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        m=''
        for i in sorted(zip(indices,s)):
           m=m+(i[1])
        return m
