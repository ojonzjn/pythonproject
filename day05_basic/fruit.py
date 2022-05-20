# 과일가게 재고 프로그램
# 1. 과일 입력 2. 과일 판매 3. 과일 재고리스트 4. 과일 삭제 5. 프로그램 종료
# - 과일 입력 : 과일이름과 가격, 수량, 원가를 입력받아서 저장. 기존에 있는 과일이면 수량에 추가
# - 과일 판매 : 과일판매 수익과 누적판매개수 출력 
# - 과일 재고리스트 : 저장된 과일명과 가격을 출력
# - 과일 삭제 : 목록에서 원하는 과일 삭제
# - 프로그램 종료 : 프로그램을 종료하는 메시지를 출력하고 종료

fruitlist=[]
fruitlist = [{'name' : '사과', 'price' : '1000', 'cost' : '500', 'count' : '2'},
             {'name' : '바나나', 'price' : '2000', 'cost' : '800', 'count' : '3'},
             {'name' : '오렌지', 'price' : '1400', 'cost' : '650', 'count' : '4'}]

profit=0
pan=0

while True:
    choice=input('''
다음 중에서 하실 일을 골라주세요 :
1. 입력   2. 판매   3. 재고리스트   4. 삭제   5. 종료
>>> ''').upper()  

    if choice=="1":  
        fruit={'name' : '', 'price' : '', 'cost' : '','count' : ''}
        #for i in range(len(fruitlist)):
        while True:
            fruit['name'] = input('과일이름 입력 >>> ')
            for i in range(len(fruitlist)):
                if fruit['name'] in fruitlist[i]['name']:
                    k = int(input('추가할 수량 입력 >>> '))
                    nam = int(fruitlist[i]['count'])
                    nam = nam + k
                    fruitlist[i]['count'] = nam
                    print(fruitlist)
                    break
                else:
                    price = 'a'
                    while not price.isdecimal():
                        fruit['price']=input('가격을 입력하세요.>>>')
                        break

                    cost = 'b'
                    while not cost.isdecimal():
                        fruit['cost']=input('원가를 입력하세요.>>>')
                        break

                    count = 'c'
                    while not count.isdecimal():
                        fruit['count']=input('수량을 입력하세요.>>>')
                        break
            
                    
                    fruitlist.append(fruit)
                    print(fruitlist)
                    break
            break
        
    
    elif choice=="2": 
        fruit={'name' : '', 'price' : '', 'cost' : '','count' : ''}
        while True:
            fruit['name'] = input('과일이름 입력 >>> ')
            for i in range(len(fruitlist)):
                if fruit['name'] in fruitlist[i]['name']:
                    k = int(input('판매한 과일 수 입력 >>> '))
                    nam = int(fruitlist[i]['count'])
                    nam -= k
                    if nam == 0:
                        print('다 팔렸어요~')
                        fruitlist[i]['count']=nam
                        profit = profit + (int(fruitlist[i]['price'])-int(fruitlist[i]['cost']))*k
                        pan = pan+k
                    elif nam < 0:
                        s=fruitlist[i]['count']
                        print(f'재고보다 많이 팔 수는 없어요~~! 현재재고는 {s}개 입니다.')                     
                    else:
                        fruitlist[i]['count']=nam
                        profit = profit + (int(fruitlist[i]['price'])-int(fruitlist[i]['cost']))*k
                        pan = pan+k
                    break
            print(f'누적 수익은 {profit}원이고 판매량은 {pan}개입니다.')
            break
    

    elif choice == '3':
        print('------  fruit  ------')
        print(*fruitlist,sep='\n')
        print(f'누적 수익은 {profit}원 입니다.')
        
    elif choice == '4':
        print('현재메뉴 : ',fruitlist)
        choice1 = input('삭제하려는 과일명을 입력하세요 >>> ')
        delok = 0
        for i in range(len(fruitlist)):
            if fruitlist[i]['name'] == choice1:
                print('삭제되었습니다.')
                del fruitlist[i]
                delok = 1
                break
        if delok == 0:
            print('등록되지 않은 과일입니다.')
        print(fruitlist)

    elif choice=="5":
        print('프로그램을 종료합니다.')
        break
