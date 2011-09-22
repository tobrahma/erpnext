import unittest
import webnotes
import copy

from webnotes.model.doclist import DocList
from webnotes.model.doc import Document
from webnotes.model.code import get_obj
from webnotes.utils import flt
from accounts.

sql = webnotes.conn.sql


class TestItem(unittest.TestCase):
	def setUp(self):
		webnotes.conn.begin()

	def tearDown(self):
		webnotes.conn.rollback()
	
	
# Test Data

tabOK = [
		{'posting_date':'2011-09-01','transaction_date':'2011-09-01','account':'acc1',}
	]

tabNotOK = [
		{'is_purchase_item': None, 'is_pro_applicable': None, 'is_manufactured_item': None, 'description': 'F Ink', 'default_warehouse': None, 'item_name': 'F Ink', 'item_group': 'F Ink', 'item_code': None, 'is_sub_contracted_item': None, 'is_stock_item': 'No', 'stock_uom': 'Nos', 'docstatus': '0'}
	      ]

for i in tabItem: i['doctype']='Item'
for i in tabItemFail: i['doctype']='Item'

items = [Document(fielddata=r) for r in tabItem]
itemsFail = [Document(fielddata=r) for r in tabItemFail]


