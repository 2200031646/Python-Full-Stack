Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Striding
>>> a="data science"
>>> a[::]
'data science'
>>> a[::1]
'data science'
>>> a[::2]
'dt cec'
>>> a="cloud computing"
>>> a[::5]
'c u'
>>> a[::4]
'cdmi'
>>> a[:9]
'cloud com'
>>> a[::2]
'codcmuig'
>>> a[3:11]
'ud compu'
>>> b="machine learning"
>>> b[1:9:2]
'ahn '
>>> b[2:12:3]
'cnlr'
>>> b[3:14:2]
'hn eri'
>>> b[5:15:4]
'nei'
>>> c="python course"
>>> c[-1:-10:-2]
'ero o'
>>> c[-3:-13:-4]
'r t'
>>> c[-5:-11:-3]
'on'
>>> #In positive striding highest to lowest is not possible
>>> c[8:6:2]
''
>>> #In negative striding lowest to highest is not possible
>>> c[-7:-4:-2]
''
