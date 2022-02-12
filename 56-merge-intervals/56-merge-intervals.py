class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals,key=lambda x:x[0])
        res=[]
        curr=intervals[0]
        for nextInterval in intervals:
            # 3 and 2
            if curr[1]>=nextInterval[0]:
                # 3and6
                if curr[1]<nextInterval[1]:
                    curr[1]=nextInterval[1]
            else:
                res.append(curr)
                curr=nextInterval
        res.append(curr)
        return res