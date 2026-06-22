from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.cnt = defaultdict(int)
        self.maxCnt = 0
        self.stacks = defaultdict(list)  # 이것도 같이 바꾸면 깔끔해

    def push(self, val: int) -> None:
        self.cnt[val] += 1
        valCnt = self.cnt[val]
        if valCnt > self.maxCnt:
            self.maxCnt = valCnt
        self.stacks[valCnt].append(val)  # [] 초기화 필요 없어짐

    def pop(self) -> int:
        res = self.stacks[self.maxCnt].pop()
        self.cnt[res] -= 1
        if not self.stacks[self.maxCnt]:
            self.maxCnt -= 1
        return res