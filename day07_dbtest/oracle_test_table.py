# 과일가게 재고 프로그램
# 1. 과일 입력 2. 과일 판매 3. 과일 삭제 4. 과일 재고리스트 5. 프로그램 종료
# 1) 과일이름 : str
# 2) 과일가격,원가,수량 : int
# - 과일 입력 : 과일이름과 가격, 수량, 원가를 입력받아서 저장. 기존에 있는 과일이면 수량에 추가
# - 과일 판매 : 과일판매 수익과 누적판매개수 출력 
# - 과일 재고리스트 : 저장된 과일명과 가격을 출력
# - 과일 삭제 : 목록에서 원하는 과일 삭제
# - 프로그램 종료 : 프로그램을 종료하는 메시지를 출력하고 종료
import cx_Oracle

conn = cx_Oracle.connect('scott','tiger','192.168.1.11:1521/XE')
cursor = conn.cursor()

while True:
    choice=input('''
다음 중에서 하실 일을 골라주세요 :
1 - 입력   2 - 수정   3 - 삭제   4 - 재고확인  5 - 종료
>>>''')

    if choice=="1":  
        sql = "insert into FRUIT values(:1,:2,:3,:4)"
        rs = cursor.execute("select * from fruit")
        col1 =[]
        for record in rs:
            col1.append(record[0])
        print('\n')
        print('%10s'%('[fname]'),'%10s'%('[price]'),'%10s'%('[cost]'),'%10s'%('[count]'))
        cursor.execute("select * from fruit")
        for item in cursor:
            print('%10s'%(item[0]),'%10d'%(item[1]),'%10d'%(item[2]),'%10d'%(item[3]))
        print('\n')
        fname = input('과일이름을 입력    >>>  ')
        if fname in col1:
            print('중복된 과일입니다. 다시 시작하세요')
            continue
        price = input('가격을 입력하세요  >>>  ')
        cost = input('원가를 입력하세요   >>>  ')
        count = input('개수를 입력하세요   >>>  ')
        data = (fname,int(price),int(cost),int(count))
        cursor.execute(sql,data)
        cursor.close
        conn.commit()


    elif choice=="2":
        cursor.execute("select * from fruit")
        print('\n')
        print('%10s'%('[fname]'),'%10s'%('[price]'),'%10s'%('[cost]'),'%10s'%('[count]'))

        for item in cursor:
            print('%10s'%(item[0]),'%10d'%(item[1]),'%10d'%(item[2]),'%10d'%(item[3]))
        print('\n')
        name=input('수정할 과일이름을 입력하세요 >>>  ')
        change = input('수정할 항목을 입력하세요(1.가격, 2.원가, 3.개수)      >>>       ')
        if change == "1":
            pricech = input('변경할 가격을 입력하세요 >>> ')
            cursor.execute(f"update fruit set price = '{pricech}' where fname = '{name}'")
        elif change == "2":
            costch = input('변경할 원가를 입력하세요 >>> ')
            cursor.execute(f"update fruit set cost = '{costch}' where fname = '{name}'")
        elif change == "3":
            countch = input('변경할 개수를 입력하세요 >>> ')
            cursor.execute(f"update fruit set count = '{countch}' where fname = '{name}'")
        cursor.close
        conn.commit()



    elif choice == '3':
        cursor.execute("select * from fruit")
        print('\n')
        print('%10s'%('[fname]'),'%10s'%('[price]'),'%10s'%('[cost]'),'%10s'%('[count]'))

        for item in cursor:
            print('%10s'%(item[0]),'%10d'%(item[1]),'%10d'%(item[2]),'%10d'%(item[3]))
        print('\n')
        name=input('삭제할 과일이름을 입력하세요 >>>  ')
        cursor.execute(f"delete from fruit where fname = '{name}'")
        cursor.close
        conn.commit()

    
    elif choice == '4':
        cursor.execute("select * from fruit")
        print('\n')
        print('%10s'%('[fname]'),'%10s'%('[price]'),'%10s'%('[cost]'),'%10s'%('[count]'))

        for item in cursor:
            print('%10s'%(item[0]),'%10d'%(item[1]),'%10d'%(item[2]),'%10d'%(item[3]))
        print('\n')
        cursor.close
        conn.commit()


    elif choice == '5':
        print('프로그램을 종료합니다.')
        conn.close()
        break