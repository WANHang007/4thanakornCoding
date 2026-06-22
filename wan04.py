print("โปรแกรมคำนวณคะแนนรวม\n")
english = int(input("คะแนนสอบอังกฤษ "))
math = int(input("คะแนนสอบคณิตศาสคร์ "))
History = int(input("คะแนนสอบประวัติศาสตร์ "))
total_score = english + math + History
average = total_score/3

if average <60:
    print("ผมรวมคะแนนสอบ")
    print("คะแนนรวมได้",total_score/3)
    print("พยายามให้มากขึ้น")
elif average <80:
    print("ผมรวมคะแนนสอบ")
    print("คะแนนรวมได้",total_score/3)
    print("ตรงตามมาตรฐาน")
else:
    print("ผมรวมคะแนนสอบ")
    print("คะแนนรวมได้",total_score/3)
    print("ดีที่สุด")