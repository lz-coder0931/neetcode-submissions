class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b),
        }
        for char in tokens:
            if char not in '+-*/':
                stack.append(int(char))
            else:
                a = stack.pop()
                b = stack.pop()
                op = operations[char]
                c = op(b,a)
                stack.append(c)
            print(stack)
        return stack.pop()

