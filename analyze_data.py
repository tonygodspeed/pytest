#!/usr/bin/env python
# coding=utf8
import sys
import os
import time
import datetime

reload(sys)

sys.setdefaultencoding("utf-8")
yesterday = (datetime.date.today() - datetime.timedelta(1))
day = yesterday.strftime("%Y%m%d")
mailto_list = ["shuang.li02@kuwo.cn"]  # ,"gansan.yang@kuwo.cn"


def test(key_sql={}):
	key_cnt = {}
	for k in key_sql:
		print k, key_sql[k]
		key_cnt[k] = 1
	return key_cnt
	pass


def analyze_data():
	map_key_sql = {}
	map_key_sql["1005_start"] = "SELECT COUNT(DISTINCT MAC) from " + day + "_act_recom_start"
	map_key_sql["1005_show"] = "SELECT COUNT(DISTINCT MAC) from " + day + "_act_recom_show_mini"
	map_key_sql["1005_run"] = "SELECT COUNT(DISTINCT MAC) from " + day + "_act_recom_exc_kuwo"

	map_key_cnt = test(map_key_sql)
	res_buf = ""
	for k in map_key_cnt:
		print k, str(map_key_cnt[k])
		res_buf += k + "\t" + str(map_key_cnt[k]) + "\n"
	pass
	res_path = "D:\\test" + day + ".res"
	if len(res_buf):
		fw = file(res_path, "w+")
		fw.write(res_buf)
		pass
	return res_path


if __name__ == '__main__':
	res_path = analyze_data()
	send_mail(mailto_list, day + " stat info", "hi,all:\nplease see attachment", res_path)
