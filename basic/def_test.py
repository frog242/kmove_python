def add(a,b):
    return a+b 
#함수에서 리턴되는 값은 없거나 하나만 가능

print(add(5,4))
c= add(4,3)
print(c)

def add_many(choice, *a): #*붙는 것은 뒤에 위치
    result =0
    print(type(a))
    print(a)
    for i in a:
        result = result + i
    return result

d = add_many(1,4,5,2,3,5)
print(d)

def add_and_mul(a,b):
    return a+b, a*b

add,mul = add_and_mul(3,6)
print(type(add))
print(type(mul))
print(add)
print(mul)

def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." %name)
    print("나이는 %d살 입니다." %old)
    if man :
        print("남자입니다.")
    else:
        print("여자입니다.")
say_myself("강창효", 28)
say_myself("김민지", 23, False)