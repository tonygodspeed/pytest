#!/usr/bin/env python
# coding=utf8
from MR_BASE import *

reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_TIPS_CLOSE"


class MR_ACT_TIPS_CLOSE(mr_base):
	def __init__(self):
		mt_type = [
			{'key': 'DISVER', 'type': 's', 'mt': r'.*DISVER:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'VER', 'type': 's', 'mt': r'VER:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'CHID', 'type': 's', 'mt': r'CHID:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'MAC', 'type': 's', 'mt': r'MAC:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'MCID', 'type': 's', 'mt': r'MCID:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'CFGVER', 'type': 's', 'mt': r'CFGVER:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'tips_name', 'type': 's', 'mt': r'tips_name:' + common_def.MT_VALUE_VALID_POSTFIX},
			{'key': 'ret', 'type': 'i', 'mt': r'ret:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'append_info', 'type': 's', 'mt': r'append_info:' + common_def.MT_VALUE_VALID_POSTFIX},
		]
		mr_base.__init__(self, mt_type, str_act)


mr_obj = MR_ACT_TIPS_CLOSE()

if __name__ == '__main__':
	test_str = r'03:12| [INFO]: <SRC:KWSHELLEXT_1.0.6.9051_MUSICDR8021PE|S:1012|PROD:KWSHELLEXT|DISVER:1.0.6.9077|OS:6.1.7601.2_Service Pack 1|PLAT:X64|VER:1.0.0.7|GID:71|CHID:MUSICDR8021PE|PN:rundll32.exe|MAC:F832E4A3AE08|UAC:0|ADMIN:1|MVER:MUSIC_8.5.2.0_P2T2|MCID:81018516|ST:1497888579|CFGVER:37|ACT:ACT_TIPS_CLOSE|tips_name:tips_competitor|ret:102|append_info:c_type=3|{}|U:>(175.43.235.16)TM:1497888194'
	mr_obj.LocalTest(test_str)
	pass
