# coding:utf-8


import base64
import sys
import urllib
import time
import datetime

"""
下载渠道对应的配置文件
"""
import redis
import os
import codecs
import re
# import importToDB
from multiprocessing import Pool
import threading
import Queue;

import sys

sys.path.append('..')
import DoSQLs
import DBTools
import RBaseCommon

STEP_LEN = 100 * 1000


class R_BASE(threading.Thread):
	def __init__(self, t_name, t_attr, r_key=None, db_index=0, queue=None):
		threading.Thread.__init__(self)
		self.sql = "select " + t_attr + " from " + t_name + " where id between {0} and {1}";
		self.db_cnt_sql = "select count(*) from " + t_name;
		# pool = redis.ConnectionPool(host='172.17.60.31', port=6379,db=db_index)
		# self.r = redis.Redis(connection_pool=pool)
		# print("init");
		# print("R_Base db_index = " + str(db_index));
		self.r = redis.Redis(host='172.17.60.31', port=6379, db=db_index);
		self.pipeline = self.r.pipeline()

		self.conn = DBTools.DB_Connect()
		self.t_name = t_name;
		self.setDaemon(True)
		self.queue = queue;
		self.r_key = r_key;
		if r_key is not None:
			self.r.delete(r_key);

		if queue is not None:
			queue.put(self);
			self.start();

	def db_query_item_done(self, item):
		self.pipeline.sadd(self.r_key, str(item[0]))

	def clear_data(self):
		self.r.flushdb();

	def run_complete(self):
		pass;

	def get_db_total_cnt(self):
		result = DoSQLs.doExcuteSql(self.db_cnt_sql);
		if len(result) == 1:
			for x in result[0]:
				return int(x);

	def run(self):
		total_cnt = self.get_db_total_cnt()
		step_cnt = total_cnt / STEP_LEN
		for index in range(0, step_cnt):
			self.db_do_next_step(index * STEP_LEN, (index + 1) * STEP_LEN)
			print("complete {0}% {1} pid = {2}".format(int((index + 1) * 100 / step_cnt), self.t_name, os.getpid()))
		self.db_do_next_step(step_cnt * STEP_LEN, total_cnt)
		DBTools.DB_Close(self.conn)
		self.run_complete();
		if self.queue is not None:
			self.queue.task_done()
		return self.db_result();

	def db_do_next_step(self, start, end):
		sql = self.sql.format(start, end);

		result = DoSQLs.doExcuteSql(sql);
		for item in result:
			self.db_query_item_done(item);

		self.pipeline.execute()

	def db_query_item_done(self, item):
		if self.r_key is not None:
			self.pipeline.sadd(self.r_key, str(item[0]))
		else:
			print("db_query_item_done but r_key is None");

	def db_result(self):
		if self.r_key is not None:
			print("-------------------------------" + self.r_key + " result : " + str(
				self.r.scard(self.r_key)) + "-----------------------------")
		else:
			print("db_result but r_key is None");


if __name__ == '__main__':
	print("============================start:" + str(datetime.datetime.now()) + "============================")
	timeBegin = datetime.datetime.now()
	# CreateDBTable("test_show_mini")
	# DB_CALC("20161116_act_recom_show_mini")

	'''
	s_mini = SHOW_MINI("20161116_act_recom_show_mini","mac,org,green_shot,is_green")
	s_mini.db_calc();
	s_mini.db_result();
	'''

	# 多线程
	'''
	queue = Queue.Queue()
	tips = START_DISP("20161116_act_recom_show_mini","mac",queue);
	#disp = START_TIPS("20161117_common_start_recom","mac",queue)
	queue.join();
	tips.db_result();
	#disp.db_result();
	'''

	# tips.db_calc();
	# disp.db_calc();

	# 多进程
	'''
	pool = Pool(processes=2)
	pool.apply_async(CalcShow,args=())
	pool.apply_async(CalcExcu,args=())
	pool.close()
	pool.join()
	'''
	# pool.apply_async(disp.db_calc,args=(dips))



	print(
	"============================start:" + str(datetime.datetime.now() - timeBegin) + "============================")
	# r.flushdb()
