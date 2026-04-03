class Solution:
    def isPalindrome(self, s: str) -> bool:
        l_ptr, r_ptr = 0, len(s) - 1

        while l_ptr < r_ptr:
            while l_ptr < r_ptr and not self.isAlphaNumeric(s[l_ptr]):
                l_ptr += 1
            while r_ptr > l_ptr and not self.isAlphaNumeric(s[r_ptr]):
                r_ptr -= 1
            
            if s[l_ptr].lower() != s[r_ptr].lower():
                return False
            
            l_ptr += 1
            r_ptr -=1
        
        return True

    def isAlphaNumeric(self, c: str):
        return (
            ord("A") <= ord(c) <= ord("Z") or
            ord("a") <= ord(c) <= ord("z") or
            ord("0") <= ord(c) <= ord("9")
        )

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome("Was it a car or a cat I saw?"))
