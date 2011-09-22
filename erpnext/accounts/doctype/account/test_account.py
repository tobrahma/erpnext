import unittest
import webnotes
import copy

from webnotes.model.doclist import DocList
from webnotes.model.doc import Document
from webnotes.model.code import get_obj
from webnotes.utils import flt

sql = webnotes.conn.sql


class TestAH(unittest.TestCase):
	def setUp(self):
		webnotes.conn.begin()

	def tearDown(self):
		webnotes.conn.rollback()

	def testInsert(self):
#		td = TestData()
		d = DocList()

		count_before =  flt(sql("select count(*) from tab"+_doctype)[0][0])
		if docok:
			for i in docok:
				d.doc = i
				d.children = None
				d.doc.fields['__islocal']=1
				d.save(1)
		count_after = flt(sql("select count(*) from tab"+_doctype)[0][0])
		self.assertTrue(count_before+len(docok)==count_after)

	def testFailAssert(self):
#		td = TestData()
		if docnotok:
			with self.assertRaises(Exception) as context:
				d = DocList()
				d.doc = docnotok[0]
				d.children = None
				d.doc.fields['__islocal']=1
				d.save(1)

# Test Data

#class TestData():

tabOK =	[
		{'account_name': 'acc1', 'parent_account': 'Indirect Expenses - TC', 'group_or_ledger': 'Ledger', 'is_pl_account': 'Yes', 'debit_or_credit': 'Debit', 'company': 'Test Company'},
		{'account_name': 'acc2', 'parent_account': 'Indirect Expenses - TC', 'group_or_ledger': 'Ledger', 'is_pl_account': 'Yes', 'debit_or_credit': 'Debit', 'company': 'Test Company'},
		{'account_name': 'acc3', 'parent_account': 'Indirect Expenses - TC', 'group_or_ledger': 'Ledger', 'is_pl_account': 'Yes', 'debit_or_credit': 'Debit', 'company': 'Test Company'}
	]

tabNotOK = 	[
		]

_doctype = 'Account'

for i in tabOK: i['doctype']=_doctype
for i in tabNotOK: i['doctype']=_doctype

docok = [Document(fielddata=r) for r in tabOK]
docnotok = [Document(fielddata=r) for r in tabNotOK]


