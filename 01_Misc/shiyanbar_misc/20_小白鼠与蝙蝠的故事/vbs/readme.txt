:code="Nothing here"
:Set objfso=CreateObject("scripting.filesystemobject")  '创建对象
:Set objTextFile = objfSO.OpenTextFile ("c:\Hello.txt",2,True) '创建文件
:msgbox code   '弹出code变量
:objTextFile.Write(code) '向文件写入code变量

