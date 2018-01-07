class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = []
        if (strs == []):
            return ""
        for i in xrange(0, len(strs[0])): #select the ith element in the first string
            ele = strs[0][i]
            count = 0
            if(len(strs) == 1):
                result.append(strs[0])
            for j in xrange(1, len(strs)): #other strings in strs, jth string
                if(i >= len(strs[j])):
                    return ''.join(result)
                else:
                    if ele == strs[j][i]:
                        count += 1
            if(count == len(strs) -1 ):
                if(i == 0):
                    result.append(ele)
                else:
                    if len(result) > 0 :
                        result.append(ele)
        print len(strs[0])
        return ''.join(result) #first string is the shortest one

if __name__ == "__main__":
    strs = ["c","c"]
    print Solution().longestCommonPrefix(strs)