import re

# a = 'hello, world!'
# print(re.match('python',a))
# print(re.match('hello',a))

# print(re.search('^hello',a))
# print(re.search('world!$',a))

# print(re.match('hello|world','hello'))

# str1='123 hello HELLO'
# print(re.match('[0-9]',str1))
# print(re.match('[0-9]+',str1))
# print(re.match('[0-9]*',str1))
# print(re.search('[0-9]*',str1))
# print(re.match('a*b','b'))
# print(re.match('a*b','ccccb'))
# print(re.match('a+b','ab'))
# print(re.match('abc?d','abcd')) # * : 0개이상, + : 1개이상, ? : 0개 또는 1개 . : 이 위치에 뭐든 하나만 오면됨
# print(re.match('ab.d','abxd'))

# print(re.match('c{3}','ccccb'))
# print(re.search('^[0-9]{2,3}-[0-9]{4}-[0-9]{4}$','051-1111-1111'))

p=re.compile('^[a-z][a-z0-9]{4,}@[a-z]{3,}[.][a-z]{2.}$')
email = ''
while not p.search(email):
    email=input('email >>> ')
