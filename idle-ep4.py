Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
cars = ['toyota','honda','benz']
cars.append('byd')
print(cars)
['toyota', 'honda', 'benz', 'byd']
cars.remove('honda')
print(cars)
['toyota', 'benz', 'byd']
cars.insert(0,'tesla')
print(cars)
['tesla', 'toyota', 'benz', 'byd']
print(cars[1])
toyota
for c in cars:
    print(c)

    
tesla
toyota
benz
byd
print(/cars)
SyntaxError: invalid syntax
print(*cars)
tesla toyota benz byd
for i,c in enumerate(cars):
    print(i,c)

    
0 tesla
1 toyota
2 benz
3 byd
for i,c in enumerate(cars,start=0):
    print('ลำดับที่ {} {}'.format(i,c))

    
ลำดับที่ 0 tesla
ลำดับที่ 1 toyota
ลำดับที่ 2 benz
ลำดับที่ 3 byd
for i,c in enumerate(cars,start=1):
    print('ลำดับที่ {} {}'.format(i,c))

    
ลำดับที่ 1 tesla
ลำดับที่ 2 toyota
ลำดับที่ 3 benz
ลำดับที่ 4 byd
print(cars)
['tesla', 'toyota', 'benz', 'byd']
for c in cars:
    print(c)

    
tesla
toyota
benz
byd
i = 0
for c in cars:
    print(i+1,c)
    i = i+1

    
1 tesla
2 toyota
3 benz
4 byd
for i,c in enumerate (cars,start=1):
    print(i,c)

    
1 tesla
2 toyota
3 benz
4 byd
print(cars)
['tesla', 'toyota', 'benz', 'byd']
cars[1]= 'vespa'
print(cars)
['tesla', 'vespa', 'benz', 'byd']
del cars[2]

print(cars)
['tesla', 'vespa', 'byd']
len(cars)
3
ord('ก')
3585
ord('ข')
3586
ord('ฃ')
3587
chr(3587)
'ฃ'
for i in range(10):
    print(chr(3585i))
    
SyntaxError: invalid decimal literal
for i in range(10):
    print(chr(3585+i))

    
ก
ข
ฃ
ค
ฅ
ฆ
ง
จ
ฉ
ช
for i in range(3585,3595):
    print(chr(i))

    
ก
ข
ฃ
ค
ฅ
ฆ
ง
จ
ฉ
ช
number = {'1001':'สมชาย','1002':'สมศรี','1003':'สมศักดิ์'}
print(number['1001'])
สมชาย
for n in number:
    print(n)

    
1001
1002
1003
for n in number.items:
    print(n)'
    
SyntaxError: unterminated string literal (detected at line 2)
for n in number.items:
    print(n)

    
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    for n in number.items:
TypeError: 'builtin_function_or_method' object is not iterable
for n in number.items():
    print(n)

    
('1001', 'สมชาย')
('1002', 'สมศรี')
('1003', 'สมศักดิ์')
for n in number.keys:
    print(n)

    
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    for n in number.keys:
TypeError: 'builtin_function_or_method' object is not iterable
for n in number.keys():
    print(n)

    
1001
1002
1003
for n in number.values():
    print(n)

    
สมชาย
สมศรี
สมศักดิ์
>>> def hello():
...     print('hello word')
...     print('hello word')
...     print('hello word')
...     print('hello word')
...     print('hello word')
... 
...     
>>> 
>>> hello()
hello word
hello word
hello word
hello word
hello word
>>> def hello(q):
...     for i in range(q):
...         print('hello word')
... 
...         
>>> hello(17)
hello word
hello word
hello word
hello word
hello word
hello word
hello word
hello word
hello word
hello word
hello word
hello word
hello word
hello word
hello word
hello word
hello word
