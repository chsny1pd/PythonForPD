Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
tao = turtle.Pen()
tao.shape(''Cat)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
tao.shape('Cat')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    tao.shape('Cat')
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python312\Lib\turtle.py", line 2832, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named Cat
tao.shape('turtle')
tao1 = {'color':'green','dis':100}
>>> tap.color(tao1['color'])
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tap.color(tao1['color'])
NameError: name 'tap' is not defined. Did you mean: 'tao'?
>>> tao.color(tao1['color'])
>>> def rect()
SyntaxError: expected ':'
>>> def rect(tao_object,tdict):
...     for i in range(4):
...         tao_object,forward(tdict['dis'])
...         tao_object.left(90)
... 
...         
>>> rect(tao,tao1)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    rect(tao,tao1)
  File "<pyshell#14>", line 3, in rect
    tao_object,forward(tdict['dis'])
NameError: name 'forward' is not defined
>>> def rect(tao_object,tdict):
...     for i in range(4):
...         tao_object.forward(tdict['dis'])
...         tao_object.left(90)
... 
...         
>>> rect(tao.tao1)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    rect(tao.tao1)
AttributeError: 'Turtle' object has no attribute 'tao1'
>>> rect(tao,tao1)
>>> tao2 = turtle.Pen()
>>> tao2dict = {'color':'green','dis':50}
>>> tao2.color(tao2dict['color'])
>>> tao2dict = {'color':'red','dis':50}
>>> tao2.color(tao2dict['color'])
>>> rect(tao2,tao2dict)
