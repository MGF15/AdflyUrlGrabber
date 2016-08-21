import requests,base64,sys
#multigrabber script to grab multi adfly url :)
#multigrabber.py file.txt []

def crack(code):
	q = code[::2]+code[::-2]
	key = q.decode('base64')[2:]
	return key
	
def url(host):
    r = requests.get(host).text
    ysmm = r.split("ysmm = \'")[1].split("\';")[0]
    cr = crack(ysmm)
    return cr
def file():
    f = sys.argv[1]
    file = open(f,'rb').read()
    new = open('adfly.txt','wb')
    for i in file.split('\n'):
        e = url(i)
        new.write(i+'\t'+e+'\n')
    new.close()

try:
    file()
except:
    print 'use : multigrabber.py file.txt\n'
