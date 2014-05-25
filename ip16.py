#!/usr/bin/env python

class InvalidIPCode(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)

class ip16:
    def __init__(self):
        pass

    def get_cur_ip(self):
        import socket

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',0))
        return s.getsockname()[0]

    def ip16_encode(self, ip):
        ipint = []

        for n in ip.split('.'):
            ipint.append(int(n))
        
        ip16 = "%02X%02X %02X%02X" % tuple(ipint)
        return ip16

    def ip16_decode(self, ip16):
        ipcode = self.trim(ip16)
        
        if len(ipcode) != 8:
            raise InvalidIPCode(ip16)
        else:
            ipint = []
            ipstr = ""
            
            for i in range(0,8,2):
                ipint.append(int(ipcode[i:i+2],16))

            for i in range(0,4):
                ipstr += str(ipint[i])
                if i < 3:
                    ipstr += '.'

            return ipstr

    def trim(self, string):
        c = [' ', ',',';','-','/','\\','.','~','^']

        for i in c:
            string = string.replace(i, '')

        return string



if __name__ == "__main__":
    from getopt import getopt, GetoptError
    import sys

    i = ip16()

    try:
        opts, args = getopt(sys.argv[1:], "e:hgcd:", ["encode=", "help", "get-ip", "get-code", "decode="])
    except GetoptError as err:
        print str(err)
        sys.exit(2)

    if len(opts) is 0 and len(args) is 0:
        opts.append(('-c',''))
    elif len(opts) is 0 and len(args) is 1:
        opts.append(('-d',args[0]))
    elif len(opts) is 0 and len(args) is 2:
        opts.append(('-d',args[0]+args[1]))
    elif len(opts) is 0 and len(args) is 3:
        opts.append(('-d',args[0]+args[1]+args[2]))
    elif len(opts) is 0 and len(args) is 4:
        opts.append(('-d',args[0]+args[1]+args[2]+args[3]))

    
    for o, a in opts:
        if o in ("-e", "--encode="):
            print i.ip16_encode(a)
        elif o in ("-h", "--help"):
            pass
        elif o in ("-g","--get-ip"):
            print i.get_cur_ip()
        elif o in ("-c","--get-code"):
            print i.ip16_encode(i.get_cur_ip())
        elif o in ("-d","--decode"):
            print i.ip16_decode(a)
        else:
            print "Invalid Option:" + o + a

