import requests,base64,sys
#multigrabber script to grab multi adfly url :)
#multigrabber.py file.txt []

def crack(code):
	zeros = ''
	ones = ''
	for n,letter in enumerate(code):
		if n%2 == 0:
			zeros += code[n]
		else:
			ones =code[n] + ones
	key = zeros + ones
	key = base64.b64decode(key.encode("utf-8"))
	return key[2:]
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
