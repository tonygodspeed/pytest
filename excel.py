# coding=utf-8
#######################################################
# filename:ExcelRW.py
# author:defias
# date:2015-4-27
# function:read or write excel file
#######################################################
import xlrd
import xlwt
import xlutils
import os.path


class XlsEngine():
	"""
	The XlsEngine is a class for excel operation
	Usage:
	  xlseng = XlsEngine('filePath')
	"""

	def __init__(self, xlsname):
		"""
		define class variable
		"""
		self.xls_name = xlsname  # file name
		self.xlrd_object = None  # workbook object
		self.isopentrue = False  # file open flag

	def open(self):
		"""
		open a xls file
		Usage:
		  xlseng.open()
		"""
		try:
			self.xlrd_object = xlrd.open_workbook(self.xls_name)
			self.isopentrue = True
			print('[%s,%s].' % (self.isopentrue, self.xlrd_object))
		except:
			self.isopentrue = False
			self.xlrd_object = None
			print('open %s failed.' % self.xls_name)

	def info(self):
		"""
		show xls file information
		Usage:
		  xlseng.info()
		"""
		if self.isopentrue == True:
			for sheetname in self.xlrd_object.sheet_names():
				worksheet = self.xlrd_object.sheet_by_name(sheetname)
				print('%s:(%d row,%d col).' % (sheetname, worksheet.nrows, worksheet.ncols))
		else:
			print('file %s is not open.' % self.xls_name)

	def readcell(self, sheetname='sheet1', rown=0, coln=0):
		"""
		read file's a cell content
		Usage:
		  xlseng.readcell('sheetname',rown,coln)
		"""
		try:
			if self.isopentrue == True:
				worksheets = self.xlrd_object.sheet_names()
				if sheetname not in worksheets:
					print('%s is not exit.' % sheetname)
					return False
				worksheet = self.xlrd_object.sheet_by_name(sheetname)
				cell = worksheet.cell_value(rown, coln)
				print('[file:%s,sheet:%s,row:%s,col:%s]:%s.' % (self.xls_name, sheetname, rown, coln, cell))
			else:
				print('file %s is not open.' % self.xls_name)
		except:
			print('readcell is false! please check sheetn rown and coln is right.')

	def readrow(self, sheetname='sheet1', rown=0):
		"""
		read file's a row content
		Usage:
		  xlseng.readrow('sheetname',rown)
		"""
		try:
			if self.isopentrue == True:
				worksheets = self.xlrd_object.sheet_names()
				if sheetname not in worksheets:
					print('%s is not exit.' % sheetname)
					return False
				worksheet = self.xlrd_object.sheet_by_name(sheetname)
				row = worksheet.row_values(rown)
				print('[file:%s,sheet:%s,row:%s]:%s.' % (self.xls_name, sheetname, rown, row))
			else:
				print('file %s is not open.' % self.xls_name)
		except:
			print('readrow is false! please check sheetn rown is right.')

	def readcol(self, sheetname='sheet1', coln=0):
		"""
		read file's a col content
		Usage:
		  xlseng.readcol('sheetname',coln)
		"""
		try:
			if self.isopentrue == True:
				worksheets = self.xlrd_object.sheet_names()
				if sheetname not in worksheets:
					print('%s is not exit.' % sheetname)
					return False
				worksheet = self.xlrd_object.sheet_by_name(sheetname)
				col = worksheet.col_values(coln)
				print('[file:%s,sheet:%s,col:%s]:%s.' % (self.xls_name, sheetname, coln, col))
			else:
				print('file %s is not open.' % self.xls_name)
		except:
			print('readcol is false! please check sheetn coln is right.')

	def writecell(self, value='', sheetn=0, rown=0, coln=0):
		"""
		write a cell to file,other cell is not change
		Usage:
		   xlseng.writecell('str',sheetn,rown，coln)
		"""
		try:
			if self.isopentrue == True:
				xlrd_objectc = xlutils.copy.copy(self.xlrd_object)
				worksheet = xlrd_objectc.get_sheet(sheetn)
				worksheet.write(rown, coln, value)
				xlrd_objectc.save(self.xls_name)
				print('writecell value:%s to [sheet:%s,row:%s,col:%s] is ture.' % (value, sheetn, rown, coln))
			else:
				print('file %s is not open.' % self.xls_name)
		except:
			print('writecell is false! please check.')

	def writerow(self, values='', sheetn=0, rown=0, coln=0):
		"""
		write a row to file,other row and cell is not change
		Usage:
		  xlseng.writerow('str1,str2,str3...strn',sheetn,rown.coln)
		"""
		try:
			if self.isopentrue == True:
				xlrd_objectc = xlutils.copy.copy(self.xlrd_object)
				worksheet = xlrd_objectc.get_sheet(sheetn)
				values = values.split(',')
				for value in values:
					worksheet.write(rown, coln, value)
					coln += 1
				xlrd_objectc.save(self.xls_name)
				print('writerow values:%s to [sheet:%s,row:%s,col:%s] is ture.' % (values, sheetn, rown, coln))
			else:
				print('file %s is not open.' % self.xls_name)
		except:
			print('writerow is false! please check.')

	def writecol(self, values='', sheetn=0, rown=0, coln=0):
		"""
		write a col to file,other col and cell is not change
		Usage:
		  xlseng.writecol('str1,str2,str3...',sheetn,rown.coln)
		"""
		try:
			if self.isopentrue == True:
				xlrd_objectc = xlutils.copy.copy(self.xlrd_object)
				worksheet = xlrd_objectc.get_sheet(sheetn)
				values = values.split(',')
				for value in values:
					worksheet.write(rown, coln, value)
					rown += 1
				xlrd_objectc.save(self.xls_name)
				print('writecol values:%s to [sheet:%s,row:%s,col:%s] is ture.' % (values, sheetn, rown, coln))
			else:
				print('file %s is not open.' % self.xls_name)
		except:
			print('writecol is false! please check.')

	def filecreate(self, sheetnames='sheet1'):
		"""
		create a empty xlsfile
		Usage:
		  filecreate('sheetname1,sheetname2...')
		"""
		try:
			if os.path.isfile(self.xls_name):
				print('%s is exit.' % self.xls_name)
				return False
			workbook = xlwt.Workbook()
			sheetnames = sheetnames.split(',')
			for sheetname in sheetnames:
				workbook.add_sheet(sheetname, cell_overwrite_ok=True)
			workbook.save(self.xls_name)
			print('%s is created.' % self.xls_name)
		except:
			print('filerator is false! please check.')

	def addsheet(self, sheetnames='sheet1'):
		"""
		add sheets to a exit xlsfile
		Usage:
		  addsheet('sheetname1,sheetname2...')
		"""
		try:
			if self.isopentrue == True:
				worksheets = self.xlrd_object.sheet_names()
				xlrd_objectc = xlutils.copy.copy(self.xlrd_object)
				sheetnames = sheetnames.split(',')
				for sheetname in sheetnames:
					if sheetname in worksheets:
						print('%s is exit.' % sheetname)
						return False
				for sheetname in sheetnames:
					xlrd_objectc.add_sheet(sheetname, cell_overwrite_ok=True)
				xlrd_objectc.save(self.xls_name)
				print('addsheet is ture.')
			else:
				print("file %s is not open \n" % self.xls_name)
		except:
			print('addsheet is false! please check.')


"""
    def chgsheet(self,sheetn,values):
    def clear(self):
"""
if __name__ == '__main__':
	# 初始化对象
	xlseng = XlsEngine('F:\\test2.xls')
	xlseng.filecreate('F:\\test2.xls')
	# 新建文件，可以指定要新建的sheet页面名称，默认值新建sheet1
	# print("\nxlseng.filecreate():")
	# xlseng.filecreate('newesheet1,newesheet2,newesheet3')
	# 打开文件
	print("xlseng.open():")
	xlseng.open()
	# 添加sheet页
	print("\nxlseng.addsheet():")
	xlseng.addsheet('addsheet1,addsheet2,addsheet3')
	# 输出文件信息
	print("\nxlseng.info():")
	xlseng.info()
	# 读取sheet1页第3行第3列单元格数据（默认读取sheet1页第1行第1列单元格数据）
	print("\nxlseng.readcell():")
	xlseng.readcell('sheet1', 2, 2)
	# 读取sheet1页第2行的数据（默认读取sheet1页第1行的数据）
	print("\nxlseng.readrow():")
	xlseng.readrow('sheet1', 1)
	# 读取sheet1页第3列的数据（默认读取sheet1页第1列的数据）
	print("\nxlseng.readcol():")
	xlseng.readcol('sheet1', 2)
	# 向第一个sheet页的第2行第4列写字符串数据‘I am writecell writed'(默认向第一个sheet页的第1行第1列写空字符串)
	print("\nxlseng.writecell():")
	xlseng.writecell('I am writecell writed', 0, 1, 3)
	# 向第一个sheet页写一行数据，各列的值为‘rowstr1,rowstr2,rowstr3'，从第3行第4列开始写入(默认向第一个sheet页写一行数据，值为‘'，从第1行第1列开始写入)
	print("\nxlseng.writerow():")
	xlseng.writerow('rowstr1,rowstr2,rowstr3', 0, 2, 3)
	# 向第一个sheet页写一列数据，各行的值为‘colstr1,colstr2,colstr3，colstr4'，从第4行第4列开始写入(默认向第一个sheet页写一列数据，值为‘'，从第1行第1列开始写入)
	print("\nxlseng.writecol():")
	xlseng.writecol('colstr1,colstr2,colstr3,colstr4', 0, 3, 3)
