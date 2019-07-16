money=True
if money:
    print("택시를 타고 가라")
else:
    print("걸어가라")

jumsu = int(input("성적을 입력하세요\n"))
print('입력한 성적은 %d 입니다' %jumsu )
#print('입력한 성적은 ',jumsu, ' 입니다') type이 달라지면 쓰기 힘들다
if jumsu >= 90:
    total = 'A'
elif jumsu >=80:
    total = 'B'
elif jumsu >=70:
    total = 'C'
elif jumsu >=50:
    total = 'D'
else:
    total = 'F'

print('당신의 학점은 {}입니다' .format(total))