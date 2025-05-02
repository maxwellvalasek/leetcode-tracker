class Solution:
    def validPalindrome(self, s: str) -> bool:

        def is_palindrome(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        l = 0
        r = len(s)-1

        while l < r:
            if s[l] != s[r]:
                return is_palindrome(s, l+1, r) or is_palindrome(s, l, r-1)
            l+=1
            r-=1
        return True