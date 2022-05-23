import cx_Oracle

conn = cx_Oracle.connect('scott','tiger','192.168.1.11:1521/XE')
cursor = conn.cursor()
k = input("job을 입력하세요 : ")
cursor.execute(f"select * from emp where job = '{k}'")
for item in cursor:
    print(item[1:8])

m = input("사원의 이름 일부를 입력하세요 : ")
cursor.execute(f"select * from emp where ename like '%{m}%'")
for item in cursor:
    print(item[1:8])