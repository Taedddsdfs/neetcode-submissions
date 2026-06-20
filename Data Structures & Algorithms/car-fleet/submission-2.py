class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = [(p,s) for p,s in zip(position,speed)]
        stack = []
        fleet.sort(reverse = True) #target 에 가까운 차부터 딴차가 따라잡는지
        for p,s in fleet:        
            stack.append((target-p)/s) # time
            while len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()

        return len(stack)
