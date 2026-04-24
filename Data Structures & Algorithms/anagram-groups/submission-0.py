class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        srtedlist = []
        for i, s in enumerate(strs):
            srtedlist.append(sorted(s))
        print(srtedlist)
        lsindex = []
        for i, m in enumerate(srtedlist):
            sub = []
            if i not in lsindex:
                lsindex.append(i)
                sub.append(strs[i])
                for j in range(i+1, len(strs)):
                    if m == srtedlist[j]:
                        # if j not in lsindex:
                        sub.append(strs[j])
                        lsindex.append(j)
                ans.append(sub)
            # print('ans', ans)
            # print(srtedlist)

        return ans




            