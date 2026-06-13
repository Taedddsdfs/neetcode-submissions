class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Helper function to check if a substring is a valid palindrome
        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                # Try deleting either the left character or the right character
                return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
            left += 1
            right -= 1
            
        return True