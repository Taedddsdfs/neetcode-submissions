class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split("/")
        for cur in paths:
            if cur ==  '..':
                if stack:
                    stack.pop() # going back 
            elif cur!= "" and cur!=".":
                stack.append(cur)
        return "/"+"/".join(stack)
        # ['', '..', '', '_home', 'a', 'b', '..', '', '', '']