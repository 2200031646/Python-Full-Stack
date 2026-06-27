Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Indexing
a="vijayawada"
a[0]
'v'
a[6]
'w'
a[0]+a[1]+a[2]+a[3]+a[4]
'vijay'
>>> a[1]+[2]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a[1]+[2]
TypeError: can only concatenate str (not "list") to str
>>> b="i am in class"
>>> b[8]+b[9]+b[10]+b[11]+b[12]
'class'
>>> b[2]+b[3]
'am'
>>> b[1]
' '
>>> b[5]+b[6]
'in'
>>> b[1]+b[4]+b[7]
'   '
>>> c="i am learning python course"
>>> c[14]+c[15]+c[16]+c[17]+c[18]+c[19]
'python'
>>> c[5]+c[6]+c[7]+c[8]+c[9]
'learn'
>>> c[21]+c[22]+c[23]+c[24]+c[25]+c[26]
'course'
>>> d="time is very precious"
>>> d[13]+d[14]+d[15]+d[16]+d[17]+d[18]+d[19]+d[20]
'precious'
>>> d[8]+d[9]+d[10]+d[11]
'very'
>>> d[0]+d[1]+d[2]+d[3]
'time'
>>> #NEGATIVE Indexing
>>> e="simple is better than complex"
>>> e[-29]+e[-28]+e[-27]+e[-26]+e[-25]+e[-24]
'simple'
>>> e[-12]+e[-11]+e[-10]+e[-9]
'than'
>>> e[-7]+e[-6]+e[-5]+e[-4]+e[-3]+e[-2]+e[-1]
'complex'
>>> e[-19]+e[-18]+e[-17]+e[-16]+e[-15]+e[-14]
'better'
>>> f="i love python"
>>> f[-11]+f[-10]+f[-9]+f[-8]
'love'
>>> f[-6]+f[-5]+f[-4]+f[-3]+f[-2]+f[-1]
'python'
