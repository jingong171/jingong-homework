Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> t=w/h**2
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    t=w/h**2
NameError: name 'w' is not defined
>>> w=55
>>> h=1.63
>>> t=w/h**2
>>> printt
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    printt
NameError: name 'printt' is not defined
>>> w=55
>>> h=1.63
>>> t=w/h**2
SyntaxError: multiple statements found while compiling a single statement
>>> w=55
>>> h=1.63
>>> t=w/h**2
>>> t
20.70081674131507
>>> t<18
False
>>> t<=25 t>=18
SyntaxError: invalid syntax
>>> t<=25
True
>>> t>=18
True
>>> t>25
False
>>> t>27
False
>>> 
