class Solution(object):
    def fourSumCount_TLE(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        # create hashmap use A and B
        length = len(A)
        sumindexAB = {}
        count = 0
        for i in xrange(0, length):
            for j in xrange(0, length):
                sumAB = A[i] + B[j]
                if sumAB not in sumindexAB:
                    sumindexAB[sumAB] = [(i, j)]
                else:
                    sumindexAB[sumAB].append((i, j))  # error1, sumindexAB.append((i,j))
        # deal with C and D
        for p in xrange(0, length):
            for q in xrange(0, length):
                sumCD = C[p] + D[q]
                if -sumCD in sumindexAB:
                    for indexpair in sumindexAB[-sumCD]:
                        count += 1
        return count

    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        # create hashmap use A and B
        length = len(A)
        sumindexAB = {}
        count = 0
        for i in xrange(0, length):
            for j in xrange(0, length):
                sumAB = A[i] + B[j]
                if sumAB not in sumindexAB:
                    sumindexAB[sumAB] = 1
                else:
                    sumindexAB[sumAB] += 1  # error1, sumindexAB.append((i,j))
        # deal with C and D
        for p in xrange(0, length):
            for q in xrange(0, length):
                sumCD = C[p] + D[q]
                if -sumCD in sumindexAB:
                    count += sumindexAB[-sumCD]
        return count

    def fourSumCount_learn(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        hashtable = {}
        for a in A:
            for b in B :
                if a + b in hashtable :
                    hashtable[a+b] += 1
                else :
                    hashtable[a+b] = 1
        count = 0
        for c in C :
            for d in D :
                if -c - d in hashtable :
                    count += hashtable[-c-d]
        return count