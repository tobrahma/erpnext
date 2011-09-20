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
			d.doc.fields['__islocal']=1
			d.save(1)
		count_after = flt(sql("select count(*) from tabItem")[0][0])
		self.assertTrue(count_before+3==count_after)
	
	def testFailAssert(self):
		with self.assertRaises(Exception) as context:
			d = DocList()
			d.doc = itemsFail[0]
			d.children = None
			d.doc.fields['__islocal']=1
			d.save(1)

# Test Data

tabItem = [
		{'is_purchase_item': None, 'is_pro_applicable': 'No', 'is_manufactured_item': None, 'description': 'Gel Ink', 'default_warehouse': None, 'item_name': 'Gel Ink', 'item_group': 'Ink', 'item_code': 'GELINK', 'is_sub_contracted_item': None, 'is_stock_item': 'Yes', 'stock_uom': 'Nos', 'docstatus': '0'}, 
		{'is_purchase_item': None, 'is_pro_applicable': 'No', 'is_manufactured_item': None, 'description': 'Gel Refill', 'default_warehouse': None, 'item_name': 'Gel Refill', 'item_group': 'Refill', 'item_code': 'GELREF', 'is_sub_contracted_item': None, 'is_stock_item': 'Yes', 'stock_uom': 'Nos', 'docstatus': '0'}, 
		{'is_purchase_item': None, 'is_pro_applicable': 'No', 'is_manufactured_item': None, 'description': 'Gel Pen', 'default_warehouse': None, 'item_name': 'Gel Pen', 'item_group': 'Pen', 'item_code': 'GELPEN', 'is_sub_contracted_item': None, 'is_stock_item': 'Yes', 'stock_uom': 'Nos', 'docstatus': '0'}
	  ]

tabItemFail = [
		{'is_purchase_item': None, 'is_pro_applicable': None, 'is_manufactured_item': None, 'description': 'F Ink', 'default_warehouse': None, 'item_name': 'F Ink', 'item_group': 'F Ink', 'item_code': None, 'is_sub_contracted_item': None, 'is_stock_item': 'No', 'stock_uom': 'Nos', 'docstatus': '0'}
	      ]

for i in tabItem: i['doctype']='Item'
for i in tabItemFail: i['doctype']='Item'

items = [Document(fielddata=r) for r in tabItem]
itemsFail = [Document(fielddata=r) for r in tabItemFail]


