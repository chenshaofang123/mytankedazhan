import os,sys
try:
	dirlib = os.path.join(os.path.dirname(os.path.abspath(__file__)),'lib')
	dirlib2 = os.path.join(os.path.dirname(os.path.abspath(__file__)),r'lib\component')
	sys.path.insert(0,dirlib)
	sys.path.insert(0,dirlib2)
except:
	print('报错')
	pass
import main
main.run()