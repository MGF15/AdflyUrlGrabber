
import cherrypy,requests,base64

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

class StringMaker(object):

	@cherrypy.expose
	def index(self):
		return "Hello! How are you?"
	@cherrypy.expose
	def hello(self,url=20):
		req = requests.get(url)
		ysmm = req.text.split("ysmm = \'")[1].split("\';")[0]
		u = crack(ysmm)
		return '<script>var w = window.open("%s");</script>' %u
if __name__ == '__main__':
   cherrypy.quickstart(StringMaker ())
