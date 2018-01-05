class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman2int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        result = 0

        #for i in xrange(0, len(s)): #error
        for ind, val in enumerate(s):
            if ind > 0 and roman2int[val] > roman2int[s[ind-1]]:  # e.g. XIV
                result -= roman2int[s[ind-1]]  # reverse last action
                result += roman2int[val]-roman2int[s[ind-1]]
            else:
                result += roman2int[val]
        return result

if __name__ == "__main__":
    print Solution().romanToInt("MCMXCVI")