class Solution:
    def clumsy(self, N: int) -> int:
        stack = [N]
        N -= 1
        op = 0
        while N > 0:
            if op % 4 == 0:
                stack[-1] *= N
            elif op % 4 == 1:
                stack[-1] = int(stack[-1] / N)
            elif op % 4 == 2:
                stack.append(N)
            else:
                stack.append(-N)
            N -= 1
            op += 1
        return sum(stack)
