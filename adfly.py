
import cherrypy,requests

def crack(code):
	q = code[::2]+code[::-2]
	key = q.decode('base64')[2:]
	return key
	
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
