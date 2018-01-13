
0. changed one is right. the important error, reverse a,b firstly or I don't reverse, just  for i in xrange(a_len-1, -1, -1):

1. str need to converted to int before adding etc.
2. error1: need to deal with same length, like "1" + "1", return 0 firstly,
3. j += 1 shouldn't forget, and after adding carry, set it to zero
4. still need to reverse
5. don't consider bit_sum = 3, so turn to changed.py see right code.

6. review formal and think about needing reverse or not. , and 043 also doesn't need to reverse firstly.
