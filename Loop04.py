import random
answer = random.randint(1,101)
while True:
    guess = int(input("ทายตัวเลข (1-100):"))
    if guess > answer:
        print("มากไป")
    elif guess < answer:
        print("น้อยไป")
    else:
        print(f"ถูกต้อง!")
        break