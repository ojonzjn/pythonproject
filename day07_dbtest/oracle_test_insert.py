import cx_Oracle

conn = cx_Oracle.connect('scott','tiger','192.168.1.11:1521/XE')
cursor = conn.cursor()
# sql = "insert into dept values(50,'databse','seoul')"
# cursor.execute(sql)
sql = "insert into dept values(:1,:2,:3)"
code = input('부서코드를 입력하세요(2자리 숫자) >>> ')
dname = input('부서명을 입력하세요  >>>')
city = input('위치를 입력하세요 >>> ')
data = (int(code),dname,city)
cursor.execute(sql,data)
cursor.close()
conn.commit()
conn.close()