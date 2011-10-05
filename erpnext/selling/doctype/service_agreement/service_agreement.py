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
		#msgprint(self.doc.naming_series)
		self.doc.name = make_autoname(self.doc.naming_series+ '.#####')
		
	def service_visit_post(self, args):
		"""
			Posts the service visit
		"""
		data = json.loads(args)
		
		sv = Document('Service Visit')
		sv.date = data['visit_date']
		sv.serial_number = data['serial_number']
		sv.details = data['visit_details']
		sv.save(1)
