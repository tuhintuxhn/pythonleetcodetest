class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range (len(s)):
            ch = s[i]
            if ch in "[{(":
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                if (
                    (ch == ")" and stack[-1] == "(")
                    or (ch == "}" and stack[-1] == "{")
                    or (ch == "]" and stack[-1] == "[")
                ):
                    stack.pop()
                else:
                    return False
        return len(stack)==0                    