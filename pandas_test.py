# coding=utf8
__author__ = 'Administrator'

import logging
import datetime

import json
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecs;
import re;

reload(sys)
sys.setdefaultencoding("utf-8")

import os


def from_this_dir(filename):
	return os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)


FILE = from_this_dir("")
curDay = datetime.datetime.now().strftime("%Y%m%d")
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s:%(filename)s <%(process)d> [line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y%m%d %H:%M:%S',
                    filename=os.path.join(FILE, curDay + '_log.txt'),
                    filemode='a+')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(filename)s <%(process)d> [line:%(lineno)d] %(levelname)s %(message)s')
console.setFormatter(formatter)
logger.addHandler(console)

if __name__ == "__main__":
	logger.info("============================start:" + str(datetime.datetime.now()) + "============================")
	fRead = codecs.open("F://music_reg2.txt");
	s = set();
	for i in fRead:
		# mt = re.match("",i,re.IGNORECASE)
		vec = i.split('\t');
		if (len(vec) > 2):
			# print (vec[1])
			s.add(vec[1]);
	print(len(s));
	# data = pd.read_table("F://music_reg2.txt",sep = '\t',names = ["act","mac","U",'omac',"type","None"],low_memory=False);#"subRet","err","extend"]);
	# print len(data['mac'].unique());
	# print data.describe();
	# data.drop_duplicates(['mac']);
	# print(data.dtypes)
	# print(data)
	# print(data['mac'])
	# print(data['mac'].unique())

	'''
	s = pd.Series([1,3,5,np.nan,6,8])
	#print(s)

	dates = pd.date_range('20130101', periods=6)
	#print(dates)

	df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
	#print(df)

	df2 = pd.DataFrame({ 'A' : 1.,
                         'B' : pd.Timestamp('20130102'),
                         'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                         'D' : np.array([3] * 4,dtype='int32'),
                         'E' : pd.Categorical(["test","train","test","train"]),
                         'F' : 'foo' })
	#print(df2)
	'''
	logger.info("============================end:" + str(datetime.datetime.now()) + "============================")
