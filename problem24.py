count = 0

def permute(digs, soFar):


	# print str(digs) + " " + str(soFar) + " " + str(count)

	if digs == []:
		global count
		count = count + 1
		if count == 1000000:
			print soFar


	for num in digs:
		digs2 = list(digs)
		soFar2 = list(soFar)
		digs2.remove(num)
		soFar2.append(num)

		permute(digs2, soFar2)


thing = [0,1,2,3,4,5,6,7,8,9]
permute(thing,[])

# [1,2,3] []      0
# [2,3]   [1]     1
# [3]     [1,2]   2
# []      [1,2,3] 3

# [2]     [1,3]   2
# []      [1,3,2] 3

# [1,3]   [2]     0
# [3]     [2,1]   0
# []      [2,1,3] 1

# [1]     [2,3]   0
# []      [2,3,1] 1










# 9

# 9

# 8 9

# 9 8

# 7 8 9

# 8 7 9
# 8 9 7
# 9 7 8
# 9 8 7 


# 6 7 8 9

# 7 6 8 9
# 7 6 9 8
# 7 8 6 9
# 7 8 9 6
# 7 9 6 8
# 7 9 8 6
# 8 6 7 9
# 8 6 9 7
# 8 7 6 9
# 8 7 9 6
# 8 9 6 7
# 8 9 7 6
# 9 6 7 8
# 9 6 8 7 
# 9 7 6 8
# 9 7 8 6
# 9 8 6 7
# 9 8 7 6

