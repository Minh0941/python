def grid_of_arrays():
	# create a grid of arrrays of size 3x3
	grid = []

	# initialie the grid as shown in figure
	for i in range(3):
		a = [] # create a temporary list that we can append to grid
		for j in range(3):
			# fill temporary list with values(these values can be anything, from data to objects or lists)
			a.append(3*i + j)
		# append the temp list with the new list
		grid.append(a)

	# return the list
	return grid

# print some test values
print(grid_of_arrays()[0][0])
print(grid_of_arrays()[1][0])
print(grid_of_arrays()[2][2])
print(grid_of_arrays()[1][1])
OUTPUT