'''
Problem A. Minimum Scalar Product

Solution: To minimize the scalar product of two 
permuted vectors, simply have one vector in sorted
order and the other in reverse sorted order and 
compute.

'''

inputf = open('A-large-practice.in')
outputf = open('solution.txt', 'w')

lines = inputf.readlines()
lines = lines[::-1]

cases = int(lines.pop())

for c in range(cases):
	terms = int(lines.pop())

	v1 = lines.pop().split()
	v2 = lines.pop().split()
	
	v1 = [int(i) for i in v1]
	v2 = [int(j) for j in v2]

	v1.sort()
	v2.sort(reverse=True)
	

	total = 0
	for t in range(terms):
		total += v1[t] * v2[t]
	
	outputf.write('Case #' + str(c + 1) + ": " + str(total) + '\n')
	

inputf.close()
outputf.close()





