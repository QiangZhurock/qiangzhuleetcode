class Solution():
    def fourSum_withoutduplicate(self, num, target): #afteradding and judgement, we can avoid duplicate.
        """
        Algorithm: Hash Table
        O(n^2)
        :param num: array
        :param target: int
        :return: a list of lists of length 4, [[val1,val2,val3,val4]]
        """
        length, result_set, sum2index = len(num), [], {}
        if length < 4:
            return []
        num.sort()

        for p in xrange(length):
            for q in xrange(p + 1, length):
                # record the pair sum
                if num[p] + num[q] not in sum2index:
                    sum2index[num[p] + num[q]] = [(p, q)]
                else:
                    sum2index[num[p] + num[q]].append((p, q))

        for i in xrange(length):
            for j in xrange(i + 1, length - 2):
                sum_remain = target - num[i] - num[j]
                if sum_remain in sum2index:
                    # construct the result
                    for pair in sum2index[sum_remain]:
                        if pair[0] > j and [num[i], num[j], num[pair[0]], num[pair[1]]] not in result_set :  # avoid duplicate, here we know, pair[0]<pair[1] from last for loop
                            result_set.append([num[i], num[j], num[pair[0]], num[pair[1]]])

        #return [list(i) for i in result_set]  # convert tuple to list
        return result_set

    def fourSum(self, num, target):
        """
        Algorithm: Hash Table
        O(n^2)
        :param num: array
        :param target: int
        :return: a list of lists of length 4, [[val1,val2,val3,val4]]
        """
        length, result_set, sum2index = len(num), set(), {}
        if length < 4:
            return []
        num.sort()

        for p in xrange(length):
            for q in xrange(p + 1, length):
                # record the pair sum
                if num[p] + num[q] not in sum2index:
                    sum2index[num[p] + num[q]] = [(p, q)]
                else:
                    sum2index[num[p] + num[q]].append((p, q))

        for i in xrange(length):
            for j in xrange(i + 1, length - 2):
                sum_remain = target - num[i] - num[j]
                if sum_remain in sum2index:
                    # construct the result
                    for pair in sum2index[sum_remain]:
                        if pair[0] > j:  # avoid duplicate, here we know, pair[0]<pair[1] from last for loop
                            result_set.add((num[i], num[j], num[pair[0]], num[pair[1]]))

        return [list(i) for i in result_set]  # convert tuple to list
        #return result_set

if __name__=="__main__":
    print Solution().fourSum_withduplicate([-3,-2,-1,0,0,1,2,3], 0)