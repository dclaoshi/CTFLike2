# ruby

## 题目描述
```
一切从 ruby 开始！
```

## 解题思路

https://github.com/mame/quine-relay/tree/50

根据doll.rb代码中最后的注释：Quine Relay，在github上找到同名项目：Quine Relay

根据提示，使用ubuntu虚拟机安装编译环境：

```bash
sudo apt-get install algol68g bash bf boo clisp clojure1.4 \
  coffeescript f2c fp-compiler g++ gauche gawk gcc gforth gfortran ghc \
  gnat gnu-smalltalk gobjc golang groovy icont iconx intercal iverilog \
  jasmin-sable llvm lua5.2 make mono-devel mono-mcs nodejs ocaml octave \  open-cobol openjdk-6-jdk parrot perl php5-cli pike7.8 python r-base \
  regina-rexx ruby2.0 scala swi-prolog tcl ucblogo valac
```

然后执行脚本：

```bash
ruby doll.rb > QR.scala
scalac QR.scala && CLASSPATH=. scala QR > QR.scm
gosh QR.scm > QR.bashbash QR.bash > QR.st
gst QR.st > QR.tcl
tclsh QR.tcl > QR.unl
ruby unlambda.rb QR.unl > QR.vala
valac QR.vala && ./QR > QR.viverilog -o QR QR.v && ./QR -vcd-none > QR.ws
ruby whitespace.rb QR.ws > qr.adb
gnatmake qr.adb && ./qr > QR.a68
a68g QR.a68 > QR.awkawk -f QR.awk > QR.boo
booi QR.boo > QR.bf
bf QR.bf > QR.c
gcc -o QR QR.c && ./QR > QR.cpp
g++ -o QR QR.cpp && ./QR > QR.cs
mcs QR.cs && mono QR.exe > QR.clj
clojure QR.clj > QR.cob
cobc -O2 -x QR.cob && ./QR > QR.coffee
coffee QR.coffee > QR.lisp
clisp QR.lisp > QR.fs
gforth QR.fs > QR.f
f2c QR.f && gcc -o QR QR.c -L/usr/lib -lf2c && ./QR > QR.f90
gfortran -o QR QR.f90 && ./QR > QR.go
go run QR.go > QR.groovy
groovy QR.groovy > QR.hs
ghc QR.hs && ./QR > QR.icn
icont -s QR.icn && ./QR > QR.i
ick -bfO QR.i && ./QR > QR.j
jasmin QR.j && CLASSPATH=. java QR > QR.java
javac QR.java && CLASSPATH=. java QR > QR.ll
llvm-as QR.ll && lli QR.bc > QR.logo
logo QR.logo > QR.lua
lua QR.lua > QR.makefilemake -f QR.makefile > QR.il
ilasm QR.il && mono QR.exe > QR.js
nodejs QR.js > QR.m
gcc -o QR QR.m && ./QR > QR.ml
ocaml QR.ml > QR.octave
octave -qf QR.octave > QR.pasm
parrot QR.pasm > QR.pas
fpc QR.pas && ./QR > QR.pl
perl QR.pl > QR.php
php QR.php > QR.pike
pike QR.pike > QR.prolog
swipl -q -t qr -f QR.prolog > QR.py
python QR.py > QR.R
R --slave < QR.R > QR.rexx
rexx ./QR.rexx > QR2.rb
```

```
[26,20,31,25,5,9,27,79,29,80,19,27,83,12,80,83,12,24,77,83,9,17,14,79,28,83,80,26,83,15,11,79,18,27,3].map{|a| (128-a).chr}.join
```

flag{we1c0me-t0-th3-wor1d-0f-qu1ne}

