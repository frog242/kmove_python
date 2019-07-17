import time
input("시작하려면 Enter키를 누르세요")
a = time.time()
input("20초 후에 Enter키를 다시 누르세요")
b = time.time()
c = int(b-a)
d = 20 - c
f = d*(-1)
print('실제 시간 : %d ' %c)
if d > 0:
    print('차이 : %d' %d)
else:
    print('차이 : %d' %f)