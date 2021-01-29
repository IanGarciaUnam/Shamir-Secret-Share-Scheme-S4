from Vista.Manager import Manager,Verifier_Builder
from Controller.Actuador import Actuador
import sys as System

USO="Usage\n Encriptar: python main.py [c] <file-original> [total-points required >1 ] <total> \"minimum points required\" >1>  \n Decriptar: python main.py [d] <file-frg> <file-aes>"
""" Usage"""
__author__="David Hernández Uriostegui-420003708, Ian Israel García Vázquez-317097364"
""" Authors David Hernández Uriostegui-420003708, Ian Israel García Vázquez-317097364""" 
__version__="1.0.0"
""" version 1.0.0"""
__license__= "GNU"
""" license = GNU"""
DESCRIPTION = "Shamir Secret  Share Scheme"
""" Shamir Secret Share Scheme"""


class Main:
	"""
	Main Class  manage the first parameter, and receive the parameters from the Terminal,
	analyse the set of this verifying the existence of the option required 

	"""

	def __init__(self, args:list):
		"""
		Main Builder

		Args:
			args: argsv from the terminal
		"""
		self.args=args
		""" args from argsv"""

	def main(self):
		"""
		Verify if the option is correct and given in a correct way
		"""
		if len(self.args)<=1:
			print(USO)
			System.exit(1)

		if len(self.args)==1 or self.args==None:
			print(USO)
			System.exit(1)

		if self.args[1]=='c' and len(self.args)<5:
			print(USO)
			System.exit(1)

		if self.args[1]=='c':
			m=Manager(self.args[2], int(self.args[3]), int(self.args[4]))
			secret=Actuador.get_secret("Please type your password [We will keep it secret]")
			m.work_to_cipher(secret)
			System.exit(1)

		if self.args[1]=='d' and len(self.args)<4 or self.args == None:
			print(USO)
			System.exit(1)
		if self.args[1]=='d':
			r=Verifier_Builder(self.args[2],self.args[3])
			r.work_to_descipher()
		elif self.args[1]!='d':
			print(USO)
			System.exit(1)




if __name__ == "__main__":
	ma=Main(System.argv)
	""" (Main) analyze and use argv"""
	ma.main()

		




