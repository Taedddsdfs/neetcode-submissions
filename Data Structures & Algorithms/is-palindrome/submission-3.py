class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            # Move left pointer forward if the character is not alphanumeric
            if not s[left].isalnum():
                left += 1
                continue  # Skip to the next iteration to re-check the condition
                
            # Move right pointer backward if the character is not alphanumeric
            if not s[right].isalnum():
                right -= 1
                continue  # Skip to the next iteration to re-check the condition
                
            # Both characters are alphanumeric, so compare them in lowercase
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
                
        return True