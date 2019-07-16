a=[]
b=[1,2,3]
c=['life','is']
d=[1,2,'life']
e=[1,2,[1,2,3]]

print(a)
print(b)
print(c)
print(d)

print(e[2][1])
print(type(a))
a=[1,2,3]
a[2]=4
print(a)

del a[1]
print(a)

a=[5,7,6,2,4,1]
a.sort(reverse=True)
print(a)

dic={1:10,2:20}
print(dic.keys())
t=type(dic)
print(t)