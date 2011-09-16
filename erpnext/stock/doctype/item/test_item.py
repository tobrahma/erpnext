import unittest
import webnotes
import copy

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
		count_before =  flt(sql("select count(*) from tabItem")[0][0])
		for i in items:
			i.save(1)
			count_after = flt(sql("select count(*) from tabItem")[0][0])
		self.assertTrue(count_before+3==count_after)
		
	def testFail(self):
		for i in itemsFail:
			i.save(1)
			self.assertRaises(webnotes.ValidationError)
	
	def testDependency(self):
		fitem = copy.copy(tabItemFail[0])
		fitem['item_code']='F Ink'
		fitem['has_batch_no'] = 'Yes'
		fitem['has_serial_no'] = 'Yes'
		Document(fielddata=fitem).save(1)
		self.assertRaises(webnotes.ValidationError)

"""
	def test_dependency(self):
		itemsFail[0].save(1)
		self.assertRaise()
"""

# Test Data
cols = ['docstatus','description','item_code','item_name','item_group','is_stock_item','stock_uom','default_warehouse']
rows = [['0','Gel Ink','GELINK','Gel Ink','Ink','Yes','Nos',None],
	['0','Gel Refill','GELREF','Gel Refill','Refill','Yes','Nos',None],
	['0','Gel Pen','GELPEN','Gel Pen','Pen','Yes','Nos',None]
	]

fail = [['0','F Ink',None,'F Ink','F Ink','Yes','Nos',None]
	]

tabItem = [dict(zip(cols[0::1],row[0::1])) for row in rows]
tabItemFail = [dict(zip(cols[0::1],row[0::1])) for row in rows]

for i in tabItem: i['doctype']='Item'
for i in tabItemFail: i['doctype']='Item'

items = [Document(fielddata=r) for r in tabItem]
itemsFail = [Document(fielddata=r) for r in tabItemFail]


