import sys
import hashlib
import binascii
import threading
import Queue

class NTLM(threading.Thread):
   def __init__(self, system_threads=35):
      threading.Thread.__init__(self)
      # Calling Thread variable.
      try:
         # We will test the arguments.
         # To handle incorrect errors.

         self.LIST = sys.argv[1]
         self.NTLM = sys.argv[2]
   
         # I create an exception for the error.
         # For the use of the program.
      except IndexError as e:
         print e

   def run(self):
      q = Queue.Queue()
      with open(self.LIST, "r") as file:
         for online in file:
            q.put(online.rstrip("\n\r"))
         self.BertModel(q)       

      for i in range(int(self.threads)):
         wrapper = threading.Thread(target=self.BertModel, args=(i,q))
         wrapper.setDaemon(True)
         wrapper.start()
         wrapper.join(600)

      q.join()
      

if __name__ == "__main__":
   NTLM().start()
