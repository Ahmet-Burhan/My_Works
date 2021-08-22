numbers1 = []
for i in range(100, 501):
    if i%7 == 0:
        if i%3 == 0:
            numbers1.append(i)


numbers2 = []
for i in range(100, 501):
    if (i%7 == 0) & (i%3 == 0):
        numbers2.append(i)

numbers3 = []
for i in range(100, 501):
    if (i%21 == 0):
        numbers3.append(i)
