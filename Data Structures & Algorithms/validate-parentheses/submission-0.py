class Solution:
    def isValid(self, s: str) -> bool:
        parstack = []
        for c in s:
            if ord(c) == ord('(') or ord(c) == ord('{') or ord(c) == ord('['):
                parstack.append(c)
            else:
                if len(parstack) > 0:
                    valid = parstack.pop()
                else:
                    return False
                match c:
                    case '}':
                        if valid != '{':
                            return False
                    case ']':
                        if valid != '[':
                            return False
                    case ')':
                        if valid != '(':
                            return False
        if len(parstack) == 0:
            return True
        else:
            return False