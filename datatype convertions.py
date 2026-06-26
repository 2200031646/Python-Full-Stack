Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatype convertions
#int
int(2)
2
int(3.4)
3
int("yasaswini")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("yasaswini")
ValueError: invalid literal for int() with base 10: 'yasaswini'
int(3+4j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(3+4j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
#float
float(3)
3.0
float(6.7)
6.7
float("python")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float("python")
ValueError: could not convert string to float: 'python'
>>> float(5+7j)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float(5+7j)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> float(True)
1.0
>>> float(False)
0.0
>>> #string
>>> str(4)
'4'
>>> str(8.9)
'8.9'
>>> str("codegnan")
'codegnan'
>>> str(2+7j)
'(2+7j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> #complex
>>> complex(6)
(6+0j)
>>> complex(7.3)
(7.3+0j)
>>> complex("course")
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    complex("course")
ValueError: complex() arg is a malformed string
>>> complex(4j+3)
(3+4j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #boolean
>>> bool(5)
True
>>> bool(5.9)
True
>>> bool("Vijayawada")
True
>>> bool(7j+8)
True
bool(True)
True
bool(False)
False
