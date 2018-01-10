class Solution():
    def fourSum(self, num, target):
        """
        Algorithm: Hash Table
        O(n^2)
        :param num: array
        :param target: int
        :return: a list of lists of length 4, [[val1,val2,val3,val4]]
        """
        length, result, sum2index = len(num), [], {}
        if length < 4:  # can be omitted.
            return []
        # sort the list.
        num.sort()
        # create 2sum hashtable
        for i in xrange(0, length - 1):
            for j in xrange(i + 1, length):
                sum2_cur = num[i] + num[j]
                if (sum2_cur not in sum2index):
                    sum2index[sum2_cur] = [(i, j)]
                else:
                    sum2index[sum2_cur].append((i, j))
        # deal with 4sum
        for p in xrange(0, length - 3):
            for q in xrange(p + 1, length - 2):
                newtarget = target - num[p] - num[q]
                if newtarget in sum2index:
                    for indexpair in sum2index[newtarget]:
                        curresult = [num[p], num[q], num[indexpair[0]], num[indexpair[1]]]
                        if indexpair[0] > q and curresult not in result:
                            result.append(curresult)

        return result