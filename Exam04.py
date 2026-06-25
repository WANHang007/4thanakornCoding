print("โปรแกรมตรวจจับความเร็วรถ")
speed = int(input("ความเร็วของคุณคือ(km/h): "))
if speed >=120:
    print("\nผิดกดหมาย(ปรับทันที)")
elif speed >=101:
    print("\nเสี่ยงถูกจับ")
elif speed >=81:
    print("\nเตือน")
else:
    print("\nปลอดภัย")
print("\nจัดทำโดยนายธนกร อาจยิ่งยง เลขที่ 4")