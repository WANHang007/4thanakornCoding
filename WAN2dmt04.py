print("x", end="\t")
for col in range(1, 13):
    print(col, end="\t")
print("ตัวคูณ")
 
for row in range(1, 13):
    print(row, end="\t")
    for col in range(1, 13):
     result = row * col
     print(result, end="\t")
    print("ตัวตั้ง")
