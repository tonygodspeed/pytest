#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')
resourceDictSum = {}
date_time = os.environ.get('calTime')


def readResource(resource):
	resourceDictSum = {}
	for index, eachLine in enumerate(resource):
		try:
			if index == 0:
				continue
			resource = {}
			eachLine = eachLine.replace("\n", "")
			parameters = eachLine.split("\t")
			resource['language'] = parameters[4]  # 语种
			resourceDictSum[parameters[0]] = resource
		except Exception:
			continue
	return resourceDictSum


def statistics(file):
	for index, eachLine in enumerate(file):
		try:
			if eachLine == "":
				continue
			eachLine = eachLine.replace("\n", "")
			parameters = eachLine.split("\t")
			uid = parameters[0]
			if index == 0:
				front_u = uid
				languageDict = {}  # 语种
			if uid != front_u:
				languageDict = sorted(languageDict.iteritems(), key=lambda languageDict: languageDict[1], reverse=True)
				languageDict = languageDict[0:3]
				data = "%s\t%s\n" % (front_u, languageDict)
				data = data.replace("\n", "")
				parameters_list = data.split("\t")
				language_list = list(eval(parameters_list[1]))
				for em in iter(language_list):
					sys.stdout.write("%s\t%s\t%s\t%s\n" % (parameters_list[0], em[0], em[1], date_time))
				languageDict = {}  # 语种
			if resourceDictSum.has_key(parameters[1]):
				languageKey = resourceDictSum[parameters[1]]["language"]
				if languageKey != "":
					lan = languageKey.split("-")
					for la in iter(lan):
						languageDict[la] = float(languageDict.get(la, 0)) + float(parameters[2])
			front_u = uid
			if languageDict is None:
				continue
		except Exception, e:
			continue
	languageDict = sorted(languageDict.iteritems(), key=lambda languageDict: languageDict[1], reverse=True)
	languageDict = languageDict[0:3]
	data = "%s\t%s\n" % (front_u, languageDict)
	data = data.replace("\n", "")
	parameters_list = data.split("\t")
	language_list = list(eval(parameters_list[1]))
	for em in iter(language_list):
		sys.stdout.write("%s\t%s\t%s\t%s\n" % (parameters_list[0], em[0], em[1], date_time))


fileA = "resource-music.txt"
# fileA = "E:/codeSVN/EcomBigData/logs/resource-music.txt"
resource = open(fileA, 'r')
resourceDictSum = readResource(resource)

statistics(sys.stdin)
# file = "E:\codeSVN\EcomBigData\logs\preference_new_export-20160124.txt"
# log = open(file, 'r')
# statistics(log)
# log.close()
