                                   #HAMBURGER

minced_meat = True
hamburger_bread = True
#green
lettuce = True
onion = True
grocery_store = True

hamburger = (minced_meat and hamburger_bread and grocery_store) and (lettuce or onion)
if hamburger:
    print("Bon Appetit!")
