liste_1 = ["sarma","dolma","keskek","borek","kebap"]
liste_2 = filter(lambda x:"ek" in x, liste_1)
liste_3 = map(lambda x :len(x), liste_2)
print(list(liste_3))
