def combo(tot):

	if tot == 0:
		return 1
	elif tot < 0:
		return 0
	
	else:
		return ways(tot, 200) + ways(tot, 100) + ways(tot,50)




def coins(amount, denom):
	if amount <= 0:
		return 0

	return 1 + coins(amount - denom, denom)


# print combo(200)
print coins(150,20)



# 200
# 100 100
# 100 50 50
# 50 50 50 50

# 100 50 25 25
# 100 25 25 25 25
# 50 25 25 25 25 25 25
# 25 25 25 25 25 25 25 25
# 50 50 50 25 25
# 50 50 


# 200
# 100 100
# 100 50 50
# 100 50 20 20 20
# 100 