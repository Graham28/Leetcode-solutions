"""
A string S represents a list of words.

Each letter in the word has 1 or more options.  If there is one option, the letter is represented as is.  If there is more than one option, then curly braces delimit the options.  For example, "{a,b,c}" represents options ["a", "b", "c"].

For example, "{a,b,c}d{e,f}" represents the list ["ade", "adf", "bde", "bdf", "cde", "cdf"].

Return all words that can be formed in this manner, in lexicographical order.
"""

class Solution(object):
    def expand(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        S= S.replace("{","}")
        s_list=S.split("}")
        if len(s_list[0])==0:
            del s_list[0]
        for i in range(len(s_list)):
            if len(s_list[i])>1:
                s_list[i] = s_list[i].split(",")
            else:
                s_list[i] = [s_list[i]]
        list_1 =[]
        list_2 =[]
        for i in s_list[0]:
            list_1.append(i)
            
        for i in range(1,len(s_list)):
            for k in list_1:
                for j in s_list[i]:
                    list_2.append(k+j)

            list_1 =list_2
            list_2 = []
        return sorted(list_1)