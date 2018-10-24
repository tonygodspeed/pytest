# coding=utf8
__author__ = 'Administrator'

import json
import sys
import os
import string
from urllib import quote
import base64
import urllib

reload(sys)
sys.setdefaultencoding("utf-8")

play_all = "&playall=true";


def jump_recom_list():
	s = "8";
	s_id = "2073656918";
	name = "Westlife : 翻唱的作品";
	psrc = "首页->猜你喜欢->";
	csrc = "曲库->首页->个性化推荐->Westlife : 翻唱的作品";

	# 一下是固定部分
	extend = "1";
	param = {};
	param["source"] = s;
	param["sourceid"] = s_id;
	param["name"] = name;
	param["extend"] = extend;
	param["other"] = "|psrc=" + psrc + "|csrc=" + csrc;

	src = "content_gedan.html?source=" + s + "&sourceid=" + s_id + "&name=" + name + "&id=" + s_id + play_all + "&extend=1&other=|psrc=" + psrc + "|csrc=" + csrc;
	b = json.dumps(param)
	p1 = quote(b);
	p2 = quote("ch:10002;name:classify;");
	p3 = quote("url:${netsong}" + src);
	result = "PageJump?param=" + p1 + ";" + p2 + ";" + p3 + "&calljump=true";

	result = base64.b64encode(result)
	result = "/PageJump=" + result;
	print("jump_recom_list = " + result)


def jump_hot_page():
	s = "51";
	s_id = "5045";
	name = "你的爱豆，我的同学！";

	# 一下是固定部分
	extend = "|MUSIC_COUNT=0|ORIGINAL_TYPE=1|";
	param = {};
	param["source"] = s;
	param["sourceid"] = s_id;
	param["name"] = name;
	param["extend"] = extend;
	param["qkback"] = "true";

	src = "content_hotcolumn.html?sourceid=" + s_id + play_all;
	j = json.dumps(param)
	p1 = quote(j);
	p2 = quote("ch:2;name:songlib;");
	p3 = quote("url:${netsong}" + src);

	result = "PageJump?param=" + p1 + ";" + p2 + ";" + p3 + "&calljump=true";

	result = base64.b64encode(result)
	result = "/PageJump=" + result;
	print("jump_hot_page = " + result)


if __name__ == "__main__":
	jump_recom_list()
	jump_hot_page();
	print(
	"play_music = play/?play=MQ==&num=MQ==&musicrid0=TVVTSUNfMjQ5OTg4&name0=aSBtaXNzIHlvdQ==&artist0=QmxpbmstMTgy&album0=QmxpbmstMTgy&artistid0=MTk1OQ==&albumid0=MzgxNQ==&mkvrid0=MTQ4Nzg4&hasecho0=MQ==&mkvnsig10=MjU2NTYwMDQ3MQ==&mkvnsig20=MTc5NTk0MTQ1NA== ")
