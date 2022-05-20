#함수만들고 적용시키는 파일

import function_customer as fc
custlist=[]
page=-1
custlist=[{'name': '홍길동', 'gender': 'M', 'email': 'hong123@gmail.com', 'birthyear': '2000'},
          {'name': '박철수', 'gender': 'M', 'email': 'park01@gmail.com', 'birthyear': '2002'},
          {'name': '김나리', 'gender': 'F', 'email': 'kim123@gmail.com', 'birthyear': '1999'} ]
page = 2 
while True:
    choice=input('''
다음 중에서 하실 일을 골라주세요 :
I - 입력   C - 현재   P - 이전   N - 다음   U - 수정   D - 삭제   Q - 종료
>>>''').upper()  

    if choice=="I":  
        page = fc.customer_input(custlist)

    elif choice=="C": 
        fc.customer_c(page,custlist)

    elif choice == 'P':
        page = fc.customer_p(page,custlist)

    elif choice == 'N':
        page = fc.customer_n(page,custlist)
        
    elif choice=='D':
        page = fc.customer_delete(page,custlist)
        
    elif choice=="U": 
        fc.customer_update(page,custlist)
