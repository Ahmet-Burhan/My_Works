def obeb(a,b):
    """ilk parametreyi buyuk olani yaziniz"""
    if b == 0:
        return a
    else:
        return obeb(b, a % b)

print(obeb.__doc__)
print(obeb(65,25))


def obeb_2(a,b):
	list_a = []
	list_b = []
	for i in range(1,a+1) :
		if a % i == 0 :
			list_a.append(i)
	for j in range(1,b +1) :
		if b % j == 0 :
			list_b.append(j)
	inter = set(list_a).intersection(set(list_b))
	return max(inter)
	
print(obeb_2(10,15))