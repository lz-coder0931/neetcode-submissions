class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(path, open_count, closed_count):
            # Base Case: When the string is complete, add it to the results.
            if open_count == closed_count == n:
                res.append(path)
                return

            # Choice 1: Add an open parenthesis if we haven't used all 'n' of them.
            if open_count < n:
                backtrack(path + "(", open_count + 1, closed_count)

            # Choice 2: Add a closed parenthesis if it's valid to do so.
            # A ')' is valid only if it doesn't outnumber the open parentheses.
            if closed_count < open_count:
                backtrack(path + ")", open_count, closed_count + 1)

        # Start the recursion with an empty string and zero counts.
        backtrack("", 0, 0)
        return res
            