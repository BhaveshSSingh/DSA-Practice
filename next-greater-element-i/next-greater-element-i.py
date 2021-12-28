class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # using a dictionary
        m = {}
        # adding -1 to the stack for checking if the stack is empty
        st = [-1]
                 # start from end go in a reverse order
        for e in nums2[::-1]:
            # until stack is empty and the top /
            while st[-1] != -1 and st[-1] <e:
                st.pop()
            m[e] = st[-1]
            st.append(e)
        return [m[x] for x in nums1]