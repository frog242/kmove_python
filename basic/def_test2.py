a=1
alist=[1,2,3]

def add_data(a):
    a=2
    alist.append(4)
    print("안쪽 %d" %a)

add_data(a)
print("바깥쪽 %d"%a)
print(alist)
print(type(a))
print(type(alist))