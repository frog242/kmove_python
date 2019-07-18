import random
import time

word = ['민지','석문','창효','수지','해인','윤곤']
rank={}
def sortV(x):
    return x[1]

while True:
    print("1.문제 불러오기 2.타자게임 3.등수목록 4.저장하기 5.불러오기")
    menu = input("메뉴를 선택하세요\n")
    if menu == '1':
        
        f=open('basic/test.txt','r',encoding = 'utf8')
        line = f.readlines()
        for i in range(5):
            line[i] = line[i].replace('\n','')
            word.append(line[i])
        f.close()
        print(word)
    elif menu == '2':
        input('타자게임을 시작하려면 Enter를 누르세요')
        st = time.time()
        for i in range(5):
            a = random.choice(word)
            print('*문제 %d\n'%(i+1),end = "")
            print(a)
            b = input()
            while a != b:
                print('*문제 %d\n'%(i+1),end = "")
                print(a)
                b = input('다시 입력하세요\n')
        lt = time.time()
        t = lt - st
        print('총 걸린 시간은 %.2f 초 입니다' %t)
        name=input('사용자 이름을 입력하세요')
        rank[name]=float(t)

    elif menu == '3':
        ranklist=sorted(rank.items(),key=sortV)
        num=1
        for k,v in ranklist:
            print("%d등 %s %f"%(num,k,v))
            num+=1
    
    elif menu == '4':
        f=open('rank.txt','w',encoding = 'utf8')
        text=''
        items=rank.items()
        for k,v in items:
            text=text+k+':'+str(v)+'\n'
        f.writelines(text)
        f.close()
        
    elif menu == '5':
        f=open('rank.txt','r',encoding = 'utf8')
        line = 1
        while line:
            line = f.readline().replace("\n","")
            if not(line==''):
                k,v=line.split(':')
                rank[k]=float(v)
        f.close()
    else:
        pass

