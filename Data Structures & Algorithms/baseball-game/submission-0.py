class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []
        for op in operations:
            if op == 'D':
                double = stack[-1] * 2
                stack.append(double)
            elif op == 'C':
                stack.pop()
            elif op == '+':
                newVal1 = stack[-1]
                newVal2 = stack[-2]
                stack.append(newVal1 + newVal2)
            else: 
                stack.append(int(op))
        
        return sum(stack)