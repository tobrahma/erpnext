import unittest
import webnotes
from webnotes.model.code import get_obj

class TestCompany(unittest.TestCase):
	def setUp(self):
		webnotes.conn.begin()
		# create a mock customer

	def test_account_creation(self):


	def tearDown(self):
		webnotes.conn.rollback()
