class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        for c in operations:
            if c == "--X" or c== "X--":
                X -= 1
            elif  c == "++X" or c== "X++":
                X += 1
        return X
