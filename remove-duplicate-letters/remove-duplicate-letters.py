class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {}
        for i, e in enumerate (s):
            last[e]= i
        done = set()
        st=[]
        for i , e in enumerate(s):
            if e not in done:
                while st and st[-1]>e and last [st[-1]]>i:
                    done.remove(st.pop())
                st.append(e)
                done.add(e)
        return "".join(st)