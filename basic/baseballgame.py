import random
number = random.sample(range(1,9),3)
print(number)
number1 = input("숫자를 입력하세요")
strike =0
out = 0


while strike != 3:

    for a in number:
        for b in number1:
            strike = 0
            ball = 0
            if a == b:
                strike += 1
            
    else:
        out+=1
print("%d s %d b %d o"%(strike,ball,out))
