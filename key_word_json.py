# coding=utf8
__author__ = 'Administrator'

import json
import sys
import os
from collections import Counter

reload(sys)
sys.setdefaultencoding("utf-8")


def check_key_words(org_path, tar_path):
	with open(org_path, "r") as f:
		# print(f)
		data = f.read();
		f.close();
		# data = data.decode('unicode-escape');
		data = data.decode('utf-8')
		# print(data);
		pydata = json.loads(data)
		print len(pydata["keywords"]);
		c = Counter(pydata["keywords"])
		pydata["keywords"] = c.keys();

		# strdata = json.dumps(pydata,ensure_ascii=False);
		with open(tar_path, "w") as fw:
			json.dump(pydata, fw, ensure_ascii=False)
			fw.close()
		d = str(c.most_common(50))
		print len(c.keys())
		print(d.decode('unicode-escape'))


def json_del_intent(org_path, tar_path):
	with open(org_path, 'r') as f:
		data = f.read();
		f.close();
		data = data.decode('gbk').encode('utf-8')
		pydata = json.loads(data)
		with open(tar_path, "w") as fw:
			json.dump(pydata, fw, ensure_ascii=False)
			fw.close()


if __name__ == "__main__":
	check_key_words(r"F:/keywords_search_rules_v2", r"F:/keywords_search_rules_v1")
