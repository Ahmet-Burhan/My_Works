flowers = [["jasmine", ["lavender", "rose"], "tulip"]]
colors = ["red", ("blue", ["yellow", "green"]), "pink"]
text = "My two favorite flowers are {} and {}, two favorite colors are {} and {}.".format(flowers[0][2],flowers[0][1][1],colors[1][0],colors[1][1][1])
print(text)
