def quicksort(listie):
	if len(listie) <= 1:
		return listie
	pivot = [listie[len(listie)/2]]
	listie.remove(pivot[0])

	less = []
	greater = []

	for x in listie:
		if x <= pivot[0]:
			less.append(x)
		else:
			greater.append(x)

	return quicksort(less) + pivot + quicksort(greater)


f = open('names.txt', 'r')
bigstring = f.read()
bigstring = bigstring.replace('"',"")
bigarr = bigstring.split(',')


# sortedarr = quicksort(bigarr)
bigarr.sort()

tot = 0

for x in range(0, len(bigarr)):
	name = bigarr[x]
	val = 0
	for y in range(0, len(name)):
		val += ord(name[y])-64

	tot += val * (x+1)

print tot
