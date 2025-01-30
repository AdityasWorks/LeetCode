class Solution:
    def reverse(self, x: int) -> int:
        a = str(abs(x))
        a = a[::-1]
        if int(a)>2**31-1:
            return 0
        return -int(a) if x<0 else int(a)