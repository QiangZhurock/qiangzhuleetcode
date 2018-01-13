
1.学习的思维是  c[I+j] = c[I] + c[j]

2. try after learn:
	num3 = [0 for _ in range(len(num1) + len(num2))] #forget this one firstly.

in 043: num1 = list(num1)[::-1] "123"-->['3','2','1']
           """ x.__floordiv__(y) <==> x//y """  18//10 = 1
	   str(int(res)) res ='087' #convert to int then convert to str, need to return str
3. join in 043
	s = ['1','2','3']
	s1 = [1,2,3]
	t = ''.join(s)
	t1 = ''.join(str(ele) for ele in s)