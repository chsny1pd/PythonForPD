Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print('Hello World')
Hello World
print('Hello PDDD')
Hello PDDD
name = 'pd'
lastname = 'chsnyt'
fullname = name + ' ' + lastname
print(fullname)
pd chsnyt
>>> fullname = name + lastname
>>> print(fullname)
pdchsnyt
>>> name = 'สมชาย'
>>> lastname = 'ดีมาก'
>>> print(fullname)
pdchsnyt
>>> fullname = name + lastname
>>> print(fullname)
สมชายดีมาก
>>> type(name)
<class 'str'>
>>> age = 10
>>> type(age)
<class 'int'>
>>>  <class 'int'>
...  
SyntaxError: unexpected indent
>>> name = 'Pd'
>>> name.upper()
'PD'
>>> name.lower()
'pd'
>>> print(name)
Pd
>>> name = name.upper()
>>> print(name)
PD
>>> number = '1'
>>> number.zfill(5)
'00001'
>>> number = '15'
>>> number.zfill(5)
'00015'
>>> print('ลุงครับผมชื่อ{} นามสกุล{} อายุ {} ขวบ'.format(name,lastname,age))
ลุงครับผมชื่อPD นามสกุลดีมาก อายุ 10 ขวบ
>>> print(f'ลุงครับผมชื่อ{name} นามสกุล{lastname} อายุ {age} ขวบ')
ลุงครับผมชื่อPD นามสกุลดีมาก อายุ 10 ขวบ
