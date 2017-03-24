from base64 import *
result=['随机加密str']
for i in range(10):
    last=[]
    for i in result:
        try:
            last.append(b64decode(i))
        except:
            pass     
        try:
            last.append(b32decode(i))
        except:
            pass        
        try:
            last.append(b16decode(i))
        except:
            pass       
    result=last
for j in result:
    if 'nctf' in j:
        print j
        break
