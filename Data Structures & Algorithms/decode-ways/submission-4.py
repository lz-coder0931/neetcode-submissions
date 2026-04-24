class Solution:
    def numDecodings(self, s: str) -> int:
        cnt = [0] * (len(s)+2)
        cnt[0] = 1
        cnt[1] = 1
        if int(s[0]) == 0:
            return 0
        # if int(s[0:2]) > 26:
        #     return 0
        # else:
        #     cnt[2] = 1
        for i in range(2, len(s)+2, 1):
            dig1, dig2 = 0, 0
            # cond 1 dig
            if int(s[i-2]) > 0:
                dig1 = cnt[i-1]
            if i > 2 and int(s[i-3:i-1])<=26 and int(s[i-3:i-1])>=10:
                dig2 = cnt[i-2]
            cnt[i] = dig1+dig2
            print(dig1, dig2, s[i-3:i-1])
        return cnt[-1]