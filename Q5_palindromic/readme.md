在本地跑完后通过
第一次测试 bb测试不通过，数组越界，因为退出时i 小于 j了
第二次测试 abcda 输出abc， 期望输出是a
写了个subsequence的代码，改不出来放弃。经验，看准题目！！
#######################
学习substring代码：
method1: Expand Around Center

In fact, we could solve it in O(n2) time using only constant space.

We observe that a palindrome mirrors around its center. Therefore, a palindrome can be expanded from its center, and there are only 2n−1 such centers.

You might be asking why there are 2n−1but not n centers? The reason is the center of a palindrome can be in between two letters. Such palindromes have even number of letters (such as ”abba”) and its center are between the two ’b’s.


dp still need to learn