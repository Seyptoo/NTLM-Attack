#coding:utf

import sys
import hashlib
import binascii
import threading
import Queue
import time

class NTLM(threading.Thread):
	def __init__(self, system_threads=35):
		threading.Thread.__init__(self)
		self.threads = system_threads
		# Calling Thread variable.
		try:
			# We will test the arguments.
			# To handle incorrect errors.

			self.LIST = sys.argv[1]
			self.NTLM = sys.argv[2]
	
			# I create an exception for the error.
			# For the use of the program.
		except IndexError as e:
			sys.exit(e)

	def NTLModel(self, q, transfert_file):
		while True:
			if(self.NTLM.islower() == False):
				self.NTLM = self.NTLM.lower()

			hash = hashlib.new('md4', q.get().encode('utf-16le')).digest()
			if(binascii.hexlify(hash) == self.NTLM):
				pass

	def run(self):
		"""
		This function will handle
		the thread system to speed up the
		program and the list.
		"""
		if(self.LIST):
			q = Queue.Queue()
			with open(self.LIST, "r") as files:
				transfert_file = files.readlines()
				for online in files:
					q.put(online.strip("\n\r"))
				self.NTLModel(q, transfert_file)		

			for i in range(int(self.threads)):
				wrapper = threading.Thread(target=self.NTLModel, args=(i, q))
				wrapper.setDaemon(True)
				wrapper.start()
				wrapper.join(600)

			q.join()

if __name__ == "__main__":
	NTLM().start()
