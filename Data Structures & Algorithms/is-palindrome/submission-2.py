class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True



















        # buffer = []
        # for i in range(len(s)):
        #     if s[i].isalnum():
        #         buffer.append(s[i].lower())

        # buffer2 = []

        # for j in range(len(s)-1,-1,-1):
        #     if s[j].isalnum():
        #         buffer2.append(s[j].lower())
        # if buffer == buffer2:
        #     return True
        # else:
        #     return False


        