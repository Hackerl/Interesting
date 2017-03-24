a = raw_input("String:")
c="hex:"
for b in a:
    c+=str(hex(ord(b)))[2:]
print c
c="ascii:"
for b in a:
    c+=("%"+str(hex(ord(b)))[2:])
print c

