# A recursive function to
# find nth catalan number


def catalan(n):
	# Base Case
	if n <= 1:
		return 1

	# Catalan(n) is the sum
	# of catalan(i)*catalan(n-i-1)
	res = 0
	for i in range(n):
		res += catalan(i) * catalan(n-i-1)

	return res


# Driver Code
for i in range(10):
	print(catalan(i), end=" ")

