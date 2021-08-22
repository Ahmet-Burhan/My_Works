def sessiz_yap(cumle):
    sesli = "aeiıöüou"
    for i in cumle:
        if i in sesli:
            cumle = cumle.replace(i, "")
        return cumle
    
print(sessiz_yap("asfdhaaaaaaaaagsdjasdbhj"))
