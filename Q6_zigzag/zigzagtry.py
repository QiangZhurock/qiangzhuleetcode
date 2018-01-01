class Solution:
	def fill_eachrow(self, result, start, magic, initialstride, s):
		while (start < len(s)):
			if (initialstride == 0):
				initialstride = magic
			result.append(s[start])
			start += initialstride
			initialstride = magic - initialstride

	def convert(self, s, num_rows):
		if (num_rows == 1):
			return s
		result = []
		magic = 2 * num_rows - 2
		initialstride = magic
		for i in range(num_rows):
			self.fill_eachrow(result, i, magic, initialstride, s)
			initialstride -= 2
		print result
		return ''.join(result)

if __name__ == "__main__":
    print Solution().convert("AB",2)
 