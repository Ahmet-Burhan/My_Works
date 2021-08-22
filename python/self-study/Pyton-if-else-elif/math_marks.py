math_mark = int(input('Please enter the mark: '))
if math_mark >= 70:
    if math_mark < 85:
        print("B (Good)")
    else:
        print("A (Excellent)")
elif math_mark >= 45 :
    if math_mark >= 60:
        print("C (Medium)")
    else:
        print("D (Not Bad)")
else:
    print("F (Failed)")
