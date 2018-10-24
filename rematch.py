import sys
import os
import re
import unittest


class Test(unittest.TestCase):
	def test(self):
		print "test"
		pass


if __name__ == '__main__':
	unittest.main()
'''
    #strLogText = r'03:41| [INFO]: <SRC:MUSIC_8.0.3.1_BCS74|ACT:APPTREASURE|S:KwMusic|4c532000050319121575:Connected|CHANNEL_NAME:10001_02|PROD:MUSIC|VER:8.0.3.1_BCS74|PLAT:WIN32|FROM:kuwo2015.exe|UI:|{kuwo2015.exe}|K:94908572|RESEND:0|U:80121297>(180.75.70.56)TM:1450800217'
    strTest = r'03:41| [INFO]: <SRC:MUSIC_8.0.3.1_BCS74|ACT:APPTREASURE|S:KwMusic|' \
        '4c532000050319121575:Connected|CHANNEL_NAME:10001_02|PROD:MUSIC|VER:8.0.3.1_BCS74|' \
        'PLAT:WIN32|FROM:kuwo2015.exe|UI:|{kuwo2015.exe}|K:94908572|RESEND:0|U:80121297>' \
        '(180.75.70.56)TM:1450800217'
    #strTest = r'03:41| [INFO]: <SRC:MUSIC_8.0.3.1_BCS74|ACT:APPTREASURE|S:KwMusic|4c532000050319121575:Connected|CHANNEL_NAME:10001_02|PROD:MUSIC|VER:8.0.3.1_BCS74|PLAT:WIN32|FROM:kuwo2015.exe|UI:|{kuwo2015.exe}'

    try:
        strMatch = r'^.*<SRC:(.*)\|ACT:(.*)\|S:KwMusic\|' \
                    '(.*)' \
                    '\|CHANNEL_NAME:(.*)\|PROD:MUSIC' \
                   '\|VER:(.*)\|PLAT:(.*)\|FROM:(.*)\|UI:(.*)\|\{(.*)\}\|K:([0-9]+)\|(.*)\|U:([0-9]+)>' \
                   '\((.*)\)TM:([0-9]+)$'
        mtRet = re.match(strMatch, strTest)
        print mtRet.group(10)
    except:
        print "mat except"

    #return mtRet
	#re.match(strMatch, strText)
	'''
