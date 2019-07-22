import re #정규표현식
custlist=[] #고객전체정보 관리 리스트
page=-1 #현재 페이지 값, index가 0부터 시작하기 때문에

while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    ''').upper()  

    if choice=="I": 
        print("고객 정보 입력")
        customer={'name':'','sex':'',"email":'',"birthyear":''}
        customer['name'] = input('이름을 입력하세요')
        customer['sex'] = input('성별을 입력하세요(M,F)').upper()
        while customer['sex'] != 'M' and customer['sex'] !='F':
            customer['sex'] = input('성별을 입력하세요(M,F)').upper()
        
        while True:
            regex = re.compile('^[a-z][a-z0-9]{4,10}@[a-zA-Z]{2,6}[.][a-zA-Z]{2,3}$')#^로 시작하는 []1자리에 해당하는 {}몇번반복할수있는가
            while True:
                customer['email']=input('이메일을 입력하세요 : ')
                golbang = regex.search(customer['email'])
                if golbang:
                    break
                else:
                    print('"@"를 포함한 정확한 이메일을 입력하세요')
            
            check=0
            for i in custlist:
                if i['email']==customer['email']:
                    check=1

            if check ==0:
                break
            print('중복되는 이메일이 있습니다.')
        
        while True:
            customer['birthyear'] = input('출생년도를 입력하세요')
            if len(customer['birthyear']) == 4 and customer['birthyear'].isdigit():
                break
            
        
        print(customer)
        custlist.append(customer)
        print(custlist)
        page += 1
        print(page)
        print('%d번째 페이지입니다.' %page)

    elif choice=="C":
        if page >= 0:
            print("현재 고객 정보 조회")
            print(custlist[page])
        else:
            print('입력된 정보가 없습니다')

    elif choice == 'P':
        print("이전 고객 정보 조회")
       
        if page <= 0:
            print('첫 번째 페이지이므로 이전 페이지 이동이 불가합니다.')
            print(page)
        else:
            page = page-1
            print('%d번째 페이지입니다.' %page)
            print(custlist[page])
    elif choice == 'N':
        print("다음 고객 정보 조회")
        
        if page >= len(custlist)-1:
            print("마지막페이지이므로 다음 페이지 이동이 불가합니다.")
            print(page)
        else:
            page = page+1
            print('%d번째 페이지입니다.' %page)
            print(custlist[page])
    elif choice=='D':
        print("고객 정보 삭제")
        delmail = input('삭제할 고객 이메일 정보를 입력하세요')
        delok=0
        for i in range(0,len(custlist)):
            if delmail == custlist[i]['email']:
                print('{} 고객님의 정보가 삭제되었습니다.'.format(custlist[i]['name']))
                del custlist[i]
                print(custlist)
                delok = 1
                break
        if delok == 0:
            print('등록되지 않은 이메일입니다.')
            print(custlist) 

    elif choice=="U":
        while True: 
            print("고객 정보 수정")
            editmail = input('수정할 고객님의 이메일 정보를 입력하세요')
            idx= -1
            for i in range(0,len(custlist)):
                if editmail == custlist[i]['email']:
                    idx=i
                    break
            if idx == -1:
                print('등록되지 않은 이메일입니다.')
                break

            editmail1=input('''
            다음중 수정하실 정보를 골라주세요
                name, sex, birthyear
            (수정할 정보가 없으면 'exit'입력)
                ''')
            if editmail1 in ('name','sex','birthyear'):
                custlist[idx][editmail1]=input('수정할 {}를 입력하세요 : ' .format(editmail1))
                break
            elif editmail1 == 'exit':
                break
            else:
                print('존재하지 않는 정보입니다.')
                break

    elif choice=="Q":
        print("프로그램 종료")
        break
    else:
        print("잘못입력하셨습니다.")
