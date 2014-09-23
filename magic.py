'''
Problem A. Magic Trick

Solution: Fetch the row of the first guess and the
row of the second guess. Check their intersection (we can
make them set because each number is used only once). If
the intersection is empty, then the volunteer cheated. If
there is exactly one number, then that is the right value.
Else, the magician messed up.

'''

inputf = open('A-small-practice.in')
outputf = open('solution.txt', 'w')

lines = inputf.readlines()
lines = lines[::-1]		

cases = int(lines.pop())


for c in range(cases):
	guess_1 = int(lines.pop())
	row1 = set(map(int,lines[-1 * guess_1].split()))
	lines = lines[:-4]

	guess_2 = int(lines.pop())
	row2 = set(map(int,lines[-1 * guess_2].split()))
	lines = lines[:-4]

	common = row1.intersection(row2)

	if len(common) == 0:
		outputf.write('Case #' + str(c + 1) + ': Volunteer cheated!\n')
	elif len(common) == 1:
		outputf.write('Case #' + str(c + 1) + ': ' + str(common.pop()) + '\n')
	else:
		outputf.write('Case #' + str(c + 1) + ': Bad magician!\n')










