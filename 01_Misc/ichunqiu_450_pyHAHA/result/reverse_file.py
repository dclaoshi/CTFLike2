f = open('D:\\tmp\\Real_PyHaHa.pyc','wb')
with open('D:\\tmp\\PyHaHa.pyc','rb') as g:
	f.write(g.read()[::-1])
f.close()