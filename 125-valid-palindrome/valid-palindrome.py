class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return alpha == alpha[::-1]