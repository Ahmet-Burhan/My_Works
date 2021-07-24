school_records={
	'personal_info':
		{'kid':{'tom':{'class':'intermediate', 'age':10},
			'sue':{'class':'elemantary', 'age':8}
			},
		'teen':{'joseph':{'class':'college', 'age':19},
			'marry':{'class':'high school', 'age':16}
			},
		},
	'grades_info':
		{'kid':{'tom':{'math':88, 'speech':69},
			'sue':{'math':90, 'speech':81}
			},
		'teen':{'joseph':{'coding':80, 'math':89},
			'marry':{'coding':70, 'math':96}
			},
		}
}

print(school_records['personal_info'])
print(school_records['personal_info'].keys())
print("Marry nin yasi\n:")
print(school_records['personal_info']['teen']['marry']['age'])



# del['key']
# del family["name1"]  -> del family['baba'], family['anne']

                #** .update

#a={'a' : 'b'}
#a.update({'c':'d'}) #, ile daha fazla da koyabilirisin(.append ile ayni mantik)






            #FROMKEYS KULLANIMI
                 
#meyveler = {}.fromkeys(["elma","armut"],0) # hepsini 0 a esitliyor
#meyveler["elma"] +=1   # meyveler["elma"] = meyveler["elma"] +1
#ayrica eklemek icin ***meyveler["kiwi"]= 5***




#sayilar = {"tek" :[]
#           ,"cift" :[]}
#sayilar["tek"].append(1)
#sayilar["tek"].insert(0,3)
#sayilar["cift"].append(6)
#tek2 = [1,2,3,4,5]
#sayilar["tek"].extend(tek2)


#a = dict(baba = "Osman" , anne= "Serpil" , cocuk= "Burhan")

#print(list(a.values()))


#third_dict = {"erkeler" : {"ahmet": 35, "mehmet": 44},\
#              "bayanlar" : {"damla" :22 , "ecem" : 35}}
#print(third_dict["erkeler"])


#second_dict = {[1,2,3] : "liste", "asd"} #list key olarak alinmaz.


#first_dict = {1 : "one", "two" : 2, False : [1,2,3]}
