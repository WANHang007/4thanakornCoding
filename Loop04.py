import random
answer = random.randint(1,101)
count = 0
while True:
    guess = int(input("ทายตัวเลข (1-100):"))
    count +=1
    if guess > answer:
        print("มากไป")
    elif guess < answer:
        print("น้อยไป")
    else:
        print(f"ถูกต้อง! คุณทายทั้งหมด {count}ครั้ง")
        break