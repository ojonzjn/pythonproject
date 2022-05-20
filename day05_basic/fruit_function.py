def fruit_sell(fruitlist):
    profit=0
    pan=0
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
                    return profit,pan
                elif nam < 0:
                    s=fruitlist[i]['count']
                    print(f'재고보다 많이 팔 수는 없어요~~! 현재재고는 {s}개 입니다.')                     
                else:
                    fruitlist[i]['count']=nam
                    profit = profit + (int(fruitlist[i]['price'])-int(fruitlist[i]['cost']))*k
                    pan = pan+k
                    return profit,pan
                break
        print(f'누적 수익은 {profit}원이고 판매량은 {pan}개입니다.')       
        break
    cnt = fruitlist[i]['count']
    return cnt