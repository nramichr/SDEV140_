"""

Write a program that uses nested loops to draw this pattern:

##
# #
#  #
#   #
#    #
#     #

"""

for row in range(6):
	for column in range(row + 2):
		if row == 0 or column == 0 or column == row + 1:
			print('#', end='')
		else:
			print(' ', end='')
	print()
