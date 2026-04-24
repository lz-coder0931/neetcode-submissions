class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        srted = sorted(nums)
        i = 0
        j = len(nums) - 1
        ans = []
        negnum = len([n for n in srted if n <= 0])
        posnum = len([m for m in srted if m > 0])

        if nums[0] == nums[len(nums) - 1] == 0:
            return [[0,0,0]]
        else:


            for i in range(negnum):
                for j in range(len(nums) -1, negnum - 1, -1):
                    # print(i, j)
                    remain = 0 - srted[i] - srted[j]
                    if remain in srted[i + 1:j]:
                        sub = sorted([srted[i], remain, srted[j]])
                        if sub not in ans:
                            ans.append(sub)
        return ans


        