class Solution:
    def decodeString(self, s: str) -> str:
        stack_string = []
        stack_count = [] # k  = positive integer
        cur = ""
        k=0
        for c in s:
            if c.isdigit():
                k = k*10 + int(c)
            elif c == '[':
                stack_string.append(cur)
                stack_count.append(k)
                cur = ""
                k = 0
            elif c ==']':
                temp = cur
                cur = stack_string.pop()
                count = stack_count.pop()
                cur+=temp*count
            else:
                cur+=c
        return cur