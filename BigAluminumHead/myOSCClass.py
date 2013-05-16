import OSC
import time, threading

class myOSC(object):

	def __init__(self):
		self.send_address = '127.0.0.1', 9000
		self.receive_address = '127.0.0.1', 8000
		self.c = OSC.OSCClient()
		self.c.connect( self.send_address ) # set the address for all following messages
		self.s = OSC.OSCServer(self.receive_address)
		self.s.addDefaultHandlers()
		#self.s.addMsgHandler("/word", self.receiveWordHandler) # adding our function 
		# just checking which handlers we have added
		print "Registered Callback-functions are :"
		
		# for addr in self.s.getOSCAddressSpace():
		# 	print addr


		# Start OSCServer
		print "\nStarting OSCServer. Use ctrl-C to quit."
		self.st = threading.Thread( target = self.s.serve_forever )
		self.st.start()

	def sendOSC(self, w):
		msg = OSC.OSCMessage()
		msg.setAddress("/word") # set OSC address
		msg.append( w) # string
		self.c.send(msg)

# def printing_handler (addr, tags, stuff, source):
# 		print "---"
# 		print "received new osc msg from %s" % OSC.getUrlStr(source)
# 		print "with addr : %s" % addr
# 		print "typetags %s" % tags
# 		print "data %s" % stuff
# 		global test 
# 		test = stuff
# 		print len(test)
# 		print "---"	
if __name__ == '__main__':
 	test = "a"
	

	
 	mine = myOSC()
 	mine.s.addMsgHandler("/word",printing_handler) # adding our function 
 	
 # 	print "Registered Callback-functions are :"
	# for addr in mine.s.getOSCAddressSpace():
 #    	print addr
 	mine.sendOSC("sending")

 	try :
	    while 1 :
	        time.sleep(5)
	       	print test
	        if(len(test)>1):
	        	print test[1]
	        	test = 'a'


	except KeyboardInterrupt :
		    print "\nClosing OSCServer."
		    mine.s.close()
		    print "Waiting for Server-thread to finish"
		    mine.st.join() ##!!!
		    print "Done"

