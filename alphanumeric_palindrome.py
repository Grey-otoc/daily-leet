def isPalindrome(s: str) -> bool:
    s = "".join(c for c in s if c.isalnum())

    return s.lower() == s[::-1].lower()

if __name__ == "__main__":
    print(isPalindrome("Was it a car or a cat I saw?"))
