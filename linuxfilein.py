import time as t
from os import path


def createFile(dest):
	print dest
	'''
the script creates a text file at the end pf location
'''
	date=t.localtime(t.time())
	name='%d_%d_%d.txt'%(date[1],date[2],(date[0]))
	if not(path.isfile(date+time)):
                        f=open(date+name,'w')
                        f.write('\n'*30)
                        f.close()
if __name__=='__main__':
        desination='/media/mint17/file'
	createFile(destination)
	raw_input("done!!!")
