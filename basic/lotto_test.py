import random



for i in range(0,5):
    base =[]
    lotto=[]
    for j in range(0,6):
        number = random.randint(1,45)
        base.append(number)
        for k in range(0,j):
            while base[k] == number:
                number = random.randint(1,45)
                if base[k] != number:
                    break

        lotto.append(number)
        

    lotto.sort()   
    print(lotto)