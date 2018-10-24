#!/usr/bin/env python
# coding=utf8
from MR_BASE import *

reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_TIPS_QUIT"


class MR_ACT_TIPS_QUIT(mr_base):
	def __init__(self):
		mt_type = [
			{'key': 'DISVER', 'type': 's', 'mt': r'.*DISVER:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'VER', 'type': 's', 'mt': r'VER:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'CHID', 'type': 's', 'mt': r'CHID:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'MAC', 'type': 's', 'mt': r'MAC:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'CFGVER', 'type': 's', 'mt': r'CFGVER:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'tips_name', 'type': 's', 'mt': r'tips_name:' + common_def.MT_VALUE_VALID_POSTFIX},
			{'key': 'ret', 'type': 'i', 'mt': r'ret:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'append_info', 'type': 's', 'mt': r'append_info:' + common_def.MT_VALUE_VALID_POSTFIX},
		]
		mr_base.__init__(self, mt_type, str_act)


mr_obj = MR_ACT_TIPS_QUIT()

if __name__ == '__main__':
	test_str = r'02:11| [INFO]: <SRC:KWSHELLEXT_1.0.6.9051_MUSIC8500PE|S:1012|PROD:KWSHELLEXT|DISVER:1.0.6.9077|OS:6.1.7601.2_Service Pack 1|PLAT:X64|VER:1.0.0.7|GID:4071|CHID:MUSIC8500PE|PN:rundll32.exe|MAC:4CCC6AB1D477|UAC:0|ADMIN:1|MVER:|MCID:|ST:1497888016|CFGVER:37|ACT:ACT_TIPS_QUIT||tips_name:tips_competitor|ret:1|append_info:c_type=1|{}|U:>(115.202.191.152)TM:1497888133'
	mr_obj.LocalTest(test_str)
	pass
