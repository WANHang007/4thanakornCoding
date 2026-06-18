print("คะแนน3วิชารวม")
point1 = int(input("คะแนนวิชา 1  "))
point2 = int(input("คะแนนวิชา 2  "))
point3 = int(input("คะแนนวิชา 3  "))
total_point = point1 + point2 + point3
average = total_point/3
if average <60:
    print("คะแนนรวมเฉลี่ยของคุณคือ " ,average)
    print("ควรปรับปรุง")
elif average <80:
    print("คะแนนรวมเฉลี่ยของคุณคือ " ,average)
    print("ผ่าน")
else:
    print("คะแนนรวมเฉลี่ยของคุณคือ " ,average)
    print("ดีเยี่ยม")