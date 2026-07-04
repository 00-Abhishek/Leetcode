class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the valid palindrome substring
            return s[left + 1:right]
        
        longest = ""
        for i in range(len(s)):
            # Odd length palindromes (center is a character)
            pal1 = expandAroundCenter(i, i)
            # Even length palindromes (center is between two characters)
            pal2 = expandAroundCenter(i, i + 1)
            
            # Update result if a longer palindrome is found
            if len(pal1) > len(longest):
                longest = pal1
            if len(pal2) > len(longest):
                longest = pal2
                
        return longest