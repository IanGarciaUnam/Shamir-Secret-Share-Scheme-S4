from main import Main
from os import remove
from random import randint
from unittest import TestCase
from os import remove
import pytest
import os
import io

class test_Manager(TestCase):
	"""
	Class for test Cifrador Class
	"""

	def test_entry_no_option(self):
		"""
		Verify that user's option exists
		"""
		Args=[]

		with pytest.raises(SystemExit) as pytest_wrapped_e:
			m=Main(Args)
			m.main()
		assert pytest_wrapped_e.type == SystemExit

	def test_entry_invalid_option(self):
		"""
		Verify an empty option that includes just kind of work but no one more argument
		"""
		Args=["c"]
		with pytest.raises(SystemExit) as pytest_wrapped_e:
			m=Main(Args)
			m.main()
		assert pytest_wrapped_e.type == SystemExit
	
	def test_entry_option_unknown(self):
		"""
		Verify when users enters a no valid option/argument
		"""
		Args=["Random word", randint(0,2000), randint(0, 131000)]

		with pytest.raises(SystemExit) as pytest_wrapped_e:
			m=Main(Args)
			m.main()
		assert pytest_wrapped_e.type==SystemExit		
	

	def test_entry_d_option_no_files(self):
		"""
		User enters an option known but no arguments enough
		"""
		Args=["d"]
		with pytest.raises(SystemExit) as pytest_wrapped_e:
			m=Main(Args)
			m.main()
		assert pytest_wrapped_e.type==SystemExit



