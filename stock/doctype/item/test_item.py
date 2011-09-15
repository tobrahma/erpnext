import unittest
import webnotes

from webnotes.model.doc import Document
from webnotes.model.code import get_obj
sql = webnotes.conn.sql

cols = ['status','description','grade','naming_series','item_code','item_name','item_group','is_stock_item','stock_uom','default_warehouse','docstatus']
rows = [['0','Gel Ink',''],
	[],
	[],
	]
