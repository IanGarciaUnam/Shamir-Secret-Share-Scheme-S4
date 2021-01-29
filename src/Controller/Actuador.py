import getpass as gt
from Crypto.Cipher import AES
import hashlib
import sys, os

class Actuador:
	"""
	A class that provides diverses statics methods, helping in repetitive works
	"""
	def make_dir(dir_name):
		"""
		Creates a directory given a name
		
		Args:
			dir_name(str): Directory name
		"""
		try:
			os.mkdir(dir_name)
		except OSError as error:
			print(error)
   
	@staticmethod
	def get_secret(show_to_public:str)->str:
		"""
		Get some string from the user withoud doing echo in the Terminal
		
		Args:
			show_to_public: Mensaje al usuario
		"""
		return gt.getpass(show_to_public)

	@staticmethod
	def change_to_new_term(original_name, new_ext):
		"""
		Change the original extension of the file to the new one

		Args:
			original_name: str
			new_ext:str

		Returns:
			The new str: in fussion
		"""
		original=original_name.split(".")[0]
		original+="."+new_ext
		return original
	def convert_list_in_file(list_out ,file_frg, new_dir):
		"""
		Exclusively designated for frg's files that contains tuples of</n>
		number and digits, process and analyse a file, becoming each tuple to line of a frg

		Args:
			list_out:list tuple list
			file_frg: name of a frg file to be written
		

		"""
		file_name=file_frg.split("/")

		new_file = os.path.join(new_dir, file_name[len(file_name)-1])
		arch=open(new_file, "w")
		for (x,y) in list_out:
			chain=str(x)+","+str(y)+"\n"
			arch.write(chain)

		arch.close()

	@staticmethod
	def convert_file_in_list(file_frg)->list:
		"""
		Exclusively designated for frg's files that contains tuples
		Each line is readed and transform into a tuple added to the list
		
		Args: 
			file_frg(str): File frg

		Returns:
			out_list:list :tuple list
		"""
		out_list=[]
		arch= open(file_frg, "r")
		for line in arch.readlines():
			little_list=line.split(",")
			try:
				x=int(little_list[0])
				y=int(little_list[1])
			except:
				continue
				
			out_list.append((x,y))

		if len(out_list)==0:
			sys,exit(1)
		return out_list

	@staticmethod
	def get_original_ext(encrypted_file:str):
		"""
		Read the name of an encrypted file and return the original extension of the .aes file
		
		Args:
			encrypted_file:str : file.ext.aes to be Readed
		
		Returns:
			str: the original extension
		"""
		chain=encrypted_file.split(".")
		return chain[1]

