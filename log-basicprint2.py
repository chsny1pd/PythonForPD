Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
tao = turtle.Pen()
type(tao)
<class 'turtle.Turtle'>
tao.shape('turtle')
tap.color('sky')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    tap.color('sky')
NameError: name 'tap' is not defined. Did you mean: 'tao'?
tao.color('sky')

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    tao.color('sky')
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python312\Lib\turtle.py", line 2215, in color
    pcolor = self._colorstr(pcolor)
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python312\Lib\turtle.py", line 2704, in _colorstr
    return self.screen._colorstr(args)
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python312\Lib\turtle.py", line 1150, in _colorstr
    raise TurtleGraphicsError("bad color string: %s" % str(color))
turtle.TurtleGraphicsError: bad color string: sky
tao.color('blue')
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.left(90)
tao.forward(100)
SyntaxError: multiple statements found while compiling a single statement
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.backward(100)
tao.clear()
for i in range(4):
    tao.forward(100)
    tao.left(90)

    
tao.color("pink")
for i in range(8):
    tao.forward(100)
    tao.left(135)

    





tao.color("red")
for i in range(8):
    tao.forward(100)
    tao.left(45)
    
SyntaxError: multiple statements found while compiling a single statement

tao.color("red")
for i in range(8):
    tao.forward(100)
    tao.left(45)
    
SyntaxError: multiple statements found while compiling a single statement




tao.clear()
for i in range(5):
    print(i)
    tao.forward(100)
    tao.left(108)

    
0
1
2
3
4
list(range(4))
[0, 1, 2, 3]
list(range(1,4))
[1, 2, 3]
list(range(1,5))
[1, 2, 3, 4]
list(range(0,10,2))
[0, 2, 4, 6, 8]
list(range(0,11,2))
[0, 2, 4, 6, 8, 10]
taolist = []
tao.reset()
for i in range(8):
    tao.forward(100)
    tao.left(45)

    

tao.up()
>>> tao.goto(50,50)
>>> tao.down()
>>> for i in range(8):
...     tao.forward(10)
...     tao.left(45)
... 
...     
>>> taolist = []
>>> tao1 = turtle.Pen()
>>> tao2 = turtle.Pen()
>>> taolist.append(tao)
>>> taolist.append(tao1)
>>> taolist.append(tao2)
>>> print(taolist)
[<turtle.Turtle object at 0x00000283E386FCE0>, <turtle.Turtle object at 0x00000283E393A390>, <turtle.Turtle object at 0x00000283E393A570>]
>>> taolist[0].forward(200)
>>> taolist[1].backward(200)
>>> taolist[2].color('red')
>>> taolist[2].left('90')
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    taolist[2].left('90')
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python312\Lib\turtle.py", line 1698, in left
    self._rotate(angle)
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python312\Lib\turtle.py", line 3339, in _rotate
    angle *= self._degreesPerAU
TypeError: can't multiply sequence by non-int of type 'float'
>>> taolist[2].left(90)
>>> taolist[2].forward(100)
>>> for t in taolist:
...     for i in range(4):
...         t.forward(50)
...         t.left(90)
... 
...         

