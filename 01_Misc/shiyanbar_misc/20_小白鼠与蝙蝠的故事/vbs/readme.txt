:code="Nothing here"
:Set objfso=CreateObject("scripting.filesystemobject")  '��������
:Set objTextFile = objfSO.OpenTextFile ("c:\Hello.txt",2,True) '�����ļ�
:msgbox code   '����code����
:objTextFile.Write(code) '���ļ�д��code����

