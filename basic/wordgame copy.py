import random
import time
import pickle

word = []
rank={}
def sortV(x):
    return x[1]

while True:
    print("1.문제 불러오기 2.타자게임 3.등수목록 4.저장하기 5.불러오기")
    menu = input("메뉴를 선택하세요\n")
    if menu == '1':
        f=open("basic/test.txt",'wb')
        data = ['고양이','강아지','호랑이','곰','공룡']
        pickle.dump(data,f)
        f.close()

        f=open('basic/test.txt','rb')
        pick = pickle.load(f)
        f.close()
        word = word + pick
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
        f1=open('rank.txt','wb')
        pickle.dump(rank,f1)
        f.close()
        
    elif menu == '5':
        f1=open('rank.txt','rb')
        datar=pickle.load(f1)
        f.close()
        print(datar)
    elif menu=='7':
        w=input('문제를 입력하세요')
        word.append(w)
    else:
        pass

