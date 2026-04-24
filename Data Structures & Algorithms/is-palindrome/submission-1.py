class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i <= j: 
            if 48<=ord(s[i])<=57 or 65<=ord(s[i])<=90 or 97<=ord(s[i])<=122:
                if 48<=ord(s[j])<=57 or 65<=ord(s[j])<=90 or 97<=ord(s[j])<=122:
                    if ord(s[i]) != ord(s[j]):
                        if 65<=ord(s[i])<=90 and ord(s[i])+32 == ord(s[j]):
                            pass
                        elif 65<=ord(s[j])<=90 and ord(s[i]) == ord(s[j])+32:
                            pass
                        else: return False

                    # print(s[i], s[j], ord(s[i]), ord(s[j]), ord(s[i]) + 32)
                    i+=1
                    j-=1
                else:
                    j -= 1
            else:
                i += 1
        return True

        