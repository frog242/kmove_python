listdata = []
print(listdata)
print(len(listdata)
while True:
    print('''
    =============== 리스트 데이터 관리================
    1. 리스트에 추가   
    2. 리스트 데이터 수정   
    3. 리스트 데이터 삭제   
    4. 종료
    =================================================
    ''')
    menu = int(input("메뉴를 선택하세요.\n"))
    if menu == 4:
        break
    elif menu == 1:
        data = input("추가할 데이터를 입력하세요.\n")
        listdata.append(data)
        print(listdata)
    elif menu == 2:
        print(listdata)
        dataindex = int(input("수정할 데이터의 인덱스를 입력하세요.\n"))
        data1 = input("수정할 데이터를 입력하세요.\n")
        listdata[dataindex] = data1
        print(listdata)
    elif menu == 3:
        print(listdata)
        dataindex = int(input('삭제할 데이터의 인덱스를 입력하세요.\n'))
        del listdata[dataindex]
        print(listdata)
