#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def isNum(value):
	try:
		x = int(value)
	except TypeError:
		return False
	except ValueError:
		return False
	except Exception, e:
		return False
	else:
		return True


def getParameters(content):
	paraDict = {}
	paraDict["TM"] = content[content.rindex("TM:") + 3:]
	content = content[content.index("<") + 1: content.rindex(">")]
	parameters = content.split("|")
	for para in parameters:
		if ":" not in para:
			continue
		key = para[0: para.index(":")]
		val = para[para.index(":") + 1:]

		if key == "":
			continue

		if val == "":
			val = "-"

		if paraDict.has_key(key):
			key += "2"
		paraDict[key] = val
	return paraDict


def statistics(file):
	for eachLine in file:
		try:
			if eachLine == "" or "ACT:PLAY_MUSIC" not in eachLine:
				continue

			if "PLAT:WIN32" in eachLine:
				eachLine = unicode(eachLine, errors='ignore', encoding='gbk')
			paraDict = getParameters(eachLine.strip())

			if paraDict is None:
				continue

			u = paraDict["U"]
			user_id = paraDict["UI"]
			rid = paraDict["RID"]
			plat = paraDict["PLAT"]
			pt = paraDict["PT"]
			ct = paraDict["TM"]
			endType = paraDict["ENDTYPE"]

			sys.stdout.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (u, user_id, plat, rid, pt, endType, ct))
		except Exception, e:
			continue


statistics(sys.stdin)
