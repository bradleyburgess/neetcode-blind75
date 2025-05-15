from enum import Enum


class Solution:
    class Bracket(Enum):
        ROUND = "ROUND"
        SQUARE = "SQUARE"
        CURLY = "CURLY"

    @staticmethod
    def valid_parentheses_stack(s: str) -> bool:
        Bracket = Solution.Bracket

        stack = []
        result = True

        for c in s:
            match c:
                case "(":
                    stack.append(Bracket.ROUND)
                case "[":
                    stack.append(Bracket.SQUARE)
                case "{":
                    stack.append(Bracket.CURLY)

                case ")":
                    try:
                        if stack.pop() != Bracket.ROUND:
                            result = False
                    except IndexError:
                        result = False
                case "]":
                    try:
                        if stack.pop() != Bracket.SQUARE:
                            result = False
                    except IndexError:
                        result = False
                case "}":
                    try:
                        if stack.pop() != Bracket.CURLY:
                            result = False
                    except IndexError:
                        result = False

        return len(stack) == 0 and result

    @staticmethod
    def valid_parentheses_stack_optimized(s: str) -> bool:
        stack = []
        bracket_map = {")": "(", "]": "[", "}": "{"}
        open_brackets = bracket_map.values()

        for c in s:
            if c in open_brackets:
                stack.append(c)
            elif c in bracket_map:
                if not stack or stack.pop() != bracket_map[c]:
                    return False
        
        return not stack