class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        
        st = []
        mp ={')':'(', '}':'{', ']':'['}

        for i in s:
            if i in ['(', '{', '[']:
                st.append(i)
            else:
                if len(st)==0:
                    return False
                if st[len(st)-1] == mp[i]:
                    st.pop()
                else:
                    return False
        if len(st)==0:
            return True
        return False
