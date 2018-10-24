#!/usr/bin/env python
# coding=utf8
from MR_BASE import *

reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_TIPS_SHOW"


class MR_ACT_TIPS_SHOW(mr_base):
	def __init__(self):
		mt_type = [
			{'key': 'DISVER', 'type': 's', 'mt': r'.*DISVER:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'VER', 'type': 's', 'mt': r'VER:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'CHID', 'type': 's', 'mt': r'CHID:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'MAC', 'type': 's', 'mt': r'MAC:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'CFGVER', 'type': 's', 'mt': r'CFGVER:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'tips_name', 'type': 's', 'mt': r'tips_name:' + common_def.MT_VALUE_VALID_POSTFIX},
			{'key': 'append_info', 'type': 's', 'mt': r'append_info:' + common_def.MT_VALUE_VALID_POSTFIX},
			# {'key':'ret','type':'i', 'mt':r'ret:'+ common_def.MT_VALUE_INVALID_POSTFIX},
		]
		mr_base.__init__(self, mt_type, str_act)


mr_obj = MR_ACT_TIPS_SHOW()

if __name__ == '__main__':
	test_str = r'00:36| [INFO]: <SRC:KWSHELLEXT_1.0.6.9051_MUSIC8702PE|S:1012|PROD:KWSHELLEXT|DISVER:1.0.6.9077|OS:6.1.7601.2_Service Pack 1|PLAT:WIN32|VER:1.0.0.7|GID:4591|CHID:MUSIC8702PE|PN:rundll32.exe|MAC:D02788EBB516|UAC:0|ADMIN:1|MVER:MUSIC_8.7.0.2_PE|MCID:143747496|ST:1497888261|CFGVER:37|ACT:ACT_TIPS_SHOW|tips_name:tips_cdguide|append_info:|{}|U:>(111.73.95.72)TM:1497888038'
	mr_obj.LocalTest(test_str)
	pass
