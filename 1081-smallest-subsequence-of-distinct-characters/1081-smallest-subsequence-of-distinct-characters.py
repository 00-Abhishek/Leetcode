class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Last occurrence of each character
        last = {ch: i for i, ch in enumerate(s)}

        stack = []
        seen = set()

        for i, ch in enumerate(s):
            # Skip if already included
            if ch in seen:
                continue

            # Maintain lexicographically smallest order
            while stack and stack[-1] > ch and last[stack[-1]] > i:
                seen.remove(stack.pop())

            stack.append(ch)
            seen.add(ch)

        return "".join(stack)