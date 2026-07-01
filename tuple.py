Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #tuple()
>>> a=(5,6.7,"code",4+8j,True,False)
>>> print(a)
(5, 6.7, 'code', (4+8j), True, False)
>>> type(a)
<class 'tuple'>
>>> a.count(4+8j)
1
>>> a.index(True)
4
>>> len(a)
6
