import logging
def square(xz):
#	x=int(input('entervalue'))
	logging.basicConfig(filename=r'C:\Users\SURYA\Desktop\2020\Du Python\abcde.txt',level=logging.DEBUG,filemode='a')
	logging.debug('some input was a given')
	logging.error('incorrect input given')
	return xz**2



square('a')
square(2)