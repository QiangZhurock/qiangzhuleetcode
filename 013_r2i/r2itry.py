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
        i = 0
        while (i < len(s)):
            if (i < (len(s) - 1) and roman2int[s[i + 1]] > roman2int[s[i]]):
                result += (roman2int[s[i + 1]] - roman2int[s[i]])
                i += 2
            else:
                result += roman2int[s[i]]
                i += 1
        return result

if __name__ == "__main__":
    print Solution().romanToInt("MCMXCVI")