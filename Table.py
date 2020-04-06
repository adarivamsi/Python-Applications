#10*10 Table Program using Python

for i in range(1,11):
	print('{:<3}|'.format(i),end="")

	for j in range(1,11):
		print('{:>4}'.format(i * j),end="")

	if i == 1:
		print('\n{:#^44}'.format(""),end="")

	print("") 