#총 5개의 사칙연산 문제
import random
import time
operator = ['+','-','*','//']
count=0
input("시작하려면 Enter를 누르세요")
ft = time.time()

for i in range(0,5):
    a = random.randint(1,10)
    b = random.choice(operator)
    c = random.randint(1,10)
    print("%d%s%d" %(a,b,c))
    f = int(input("정답을 입력하세요 : "))
    
    e = eval("%d%s%d"%(a,b,c))
    if f == e:
        print("정답")
        count+=1
        lt = time.time()
    else:
        print("오답")
    

h = int(lt - ft)
print('%d개 맞음' %count)
print('계산하는데 걸린 총 시간은 %.0d초 입니다'%h)