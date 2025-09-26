import random

a = random.randint(1,100)

guess = int(input())

while guess != a:
    if guess > a:
        print("numarul este mai mic")
        
    if guess < a:
        print("numarul este mai mare")
   
    guess = int(input())
        

print("felicitari")
