import unittest
import webnotes
import copy

from webnotes.model.doclist import DocList
from webnotes.model.doc import Document
from webnotes.model.code import get_obj
from webnotes.utils import flt

sql = webnotes.conn.sql


class TestItem(unittest.TestCase):
	def setUp(self):
		webnotes.conn.begin()

	def tearDown(self):
		webnotes.conn.rollback()
		
	def testInsert(self):
		d = DocList()

		count_before =  flt(sql("select count(*) from tabItem")[0][0])
		for i in items:
			d.doc = i
			d.children = None
			d.save(1)
		count_after = flt(sql("select count(*) from tabItem")[0][0])
		self.assertTrue(count_before+3==count_after)
	
	def testFailAssert(self):
		with self.assertRaises(Exception) as context:
			d = DocList()
			d.doc = itemsFail[0]
			d.children = None
			count_before =  flt(sql("select count(*) from tabItem")[0][0])
			d.save(1)
			count_after = flt(sql("select count(*) from tabItem")[0][0])
			print [count_before,count_after]

# Test Data
cols = ['docstatus','description','item_code','item_name','item_group','is_stock_item','stock_uom','default_warehouse','is_manufactured_item','is_purchase_item','is_sub_contracted_item','is_pro_applicable']
rows = [['0','Gel Ink','GELINK','Gel Ink','Ink','Yes','Nos',None,None,None,None,'No'],
	['0','Gel Refill','GELREF','Gel Refill','Refill','Yes','Nos',None,None,None,None,'No'],
	['0','Gel Pen','GELPEN','Gel Pen','Pen','Yes','Nos',None,None,None,None,'No']
	]

fail = [['0','F Ink',None,'F Ink','F Ink','No','Nos',None,None,None,None,None]
	]

tabItem = [dict(zip(cols[0::1],row[0::1])) for row in rows]
tabItemFail = [dict(zip(cols[0::1],row[0::1])) for row in rows]

for i in tabItem: i['doctype']='Item'
for i in tabItemFail: i['doctype']='Item'

items = [Document(fielddata=r) for r in tabItem]
itemsFail = [Document(fielddata=r) for r in tabItemFail]


