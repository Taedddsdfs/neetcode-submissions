class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        if '0000' in deadends:
            return -1
        
        q = deque([("0000",0)])
        visited = {"0000"}
        while q: 
            state,moves = q.popleft()
            if state == target:
                return moves
            for i in range(4):
                digit = int(state[i])
                
                for change in(-1,1):
                    new_digit = (digit+change)%10
                    nxt = state[:i]+str(new_digit) + state[i+1:]

                    if nxt not in deadends and nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, moves + 1))
        return -1
                        