#Author:D4Vinci
#rewrited by MGF15 to decode new adfly encoder ! f&^%k you adfly
#algorithm from StoreClerk 
#python2 only i hate python3 ! :P
import base64 , urllib, re, sys, urllib

def crack(code):

	zeros = ''
	ones = ''
	for n,letter in enumerate(code):
		if n % 2 == 0:
			zeros += code[n]
		else:
			ones = code[n] + ones
	key = zeros + ones
   
	key = list(key)

	i = 0

	while i < len(key):

		if key[i].isdigit():

			for j in range(i+1,len(key)):

				if key[j].isdigit():
                    
					u = int(key[i])^int(key[j])
                    
					if u < 10:
                        
						key[i] = str(u)
                        
					i = j					
					break
		i+=1

	key = ''.join(key).decode('base64')[16:-16]

	return key

if __name__ == '__main__':
	
	if len(sys.argv) < 2 : 
		print ('python AdflyURLGrabber.py <URL>')
		exit()
	else:
		adfly = sys.argv[1]
		adfly = urllib.urlopen(adfly).read()
		ysmm = re.findall(r"var ysmm = '(.*?)';",adfly)[0]
		decrypted_url = crack(ysmm)
		print decrypted_url
