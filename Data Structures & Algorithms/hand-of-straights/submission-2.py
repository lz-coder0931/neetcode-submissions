class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # if len(hand) % groupSize:
        #     return False

        # count ={}
        # for n in hand:
        #     count[n] = 1+count.get(n,0)

        # hand.sort()

        # for num in hand:
        #     if count[num]:
        #         for i in range(num, num+groupSize):
        #             if not count[i]:
        #                 return False
        #             count[i] -=1
        # return True
        if len(hand) % groupSize:
            return False

        count = Counter(hand)
        hand.sort()
        for num in hand:
            if count[num]:
                for i in range(num, num + groupSize):
                    if not count[i]:
                        return False
                    count[i] -= 1
        return True

            