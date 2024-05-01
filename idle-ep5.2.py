Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> my_dict = {'ชื่อ':'พีดี','อายุ':'17','เพศ':'ชาย'}
>>> 
>>> my_dict['เมน']= 'มินจี'
>>> print(my_dict)
{'ชื่อ': 'พีดี', 'อายุ': '17', 'เพศ': 'ชาย', 'เมน': 'มินจี'}
>>> del mydect['เมน']
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    del mydect['เมน']
NameError: name 'mydect' is not defined. Did you mean: 'my_dict'?
>>> del my_dict['เมน']
>>> print(my_dict)
{'ชื่อ': 'พีดี', 'อายุ': '17', 'เพศ': 'ชาย'}
