#!/usr/bin/env python
#coding:utf-8
f=open('康师傅免流-OpenVpn教程.html','r')
result=[]
for i in f.readlines():
    if '%E5%BA%B7%E5%B8%88%E5%82%85%E5%85%8D%E6%B5%81' in i:
        a=i.split('%E5%BA%B7%E5%B8%88%E5%82%85%E5%85%8D%E6%B5%81-OpenVpn%E6%95%99%E7%A8%8B_files')
        b=a[1]
        c=b.split('\"',1)
        result.append(a[0]+'{{static_url("show'+c[0]+'")}}"'+c[1])
    else:
        result.append(i)
a=open('1.html','w+')
a.writelines(result)
