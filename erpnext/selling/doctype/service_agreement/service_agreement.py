import webnotes
from webnotes.model.doc import make_autoname, Document, addchild
from webnotes import msgprint
from webnotes.utils import get_defaults
import json
from accounts.utils import post_jv
sql = webnotes.conn.sql

class DocType:
	def __init__(self, doc, doclist):
		self.doc, self.doclist = doc, doclist

	def autoname(self):
		"""
			Create Lease Id using naming_series pattern
		"""
		self.doc.name = make_autoname(self.doc.naming_series+ '.#####')
