import cx_Oracle

conn = cx_Oracle.connect('scott','tiger','192.168.1.11:1521/XE')
cursor = conn.cursor()
cursor.execute("create table FRUIT(FNAME VARCHAR2(20),PRICE NUMBER(10),COST NUMBER(10),COUNT NUMBER(10))")