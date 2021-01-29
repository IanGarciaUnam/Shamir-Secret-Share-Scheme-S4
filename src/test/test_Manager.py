from Vista.Manager import Manager,Verifier_Builder
from os import remove
from random import randint
from unittest import TestCase
from os import remove
import pytest
import os
from shutil import rmtree
import io

class test_Manager(TestCase):
	"""
	Class for test Cifrador Class
	"""

	def test_entry_no_file(self):
		"""
		Verify that user's file exists
		"""
		maximum= randint(70,140)
		minimum=randint(2,69)

		with pytest.raises(SystemExit) as pytest_wrapped_e:
			m=Manager("No_existente", maximum, minimum)
		assert pytest_wrapped_e.type == SystemExit




	def test_entry_no_max_min_in_right_order(self):
		"""
		Verify the values of max and min are right
		"""	
		maximum= randint(70,140)
		minimum=randint(2,69)

		with pytest.raises(SystemExit) as pytest_wrapped_e:
			m=Manager("/test_files/test.cat",minimum, maximum)
		assert pytest_wrapped_e.type == SystemExit
		rmtree("./exit_files/")

	def test_bad_verifier(self):

		with pytest.raises(SystemExit) as pytest_wrapped_e:
			v= Verifier_Builder("No existente", "No existente")
			v.work_to_descipher()
		assert pytest_wrapped_e.type==SystemExit






