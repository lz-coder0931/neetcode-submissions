class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heaparr = [-cnt for cnt in count.values()]
        heapq.heapify(heaparr)
        q = deque()
        time = 0
        while heaparr or q:
            time +=1
            if not heaparr:
                time = q[0][1]
            else:
                cnt = 1+heapq.heappop(heaparr)
                if cnt:
                    q.append([cnt, time+n])
            if q and time == q[0][1]:
                heapq.heappush(heaparr, q.popleft()[0])
        return time