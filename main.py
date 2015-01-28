import webapp2
import os
import jinja2 #for templates
from google.appengine.ext import db #for database

template_dir = os.path.join(os.path.dirname(__file__), 'templates') #this tells where templates are present
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True) # autoescape is for escaping html specialchars

class Handler(webapp2.RequestHandler): #custom created class by me 
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)  
    def render(self, template, **kw): #for redering template
        self.write(self.render_str(template, **kw))

class MainPage(Handler):  # class to load main page
    def render_header(self,title): 
    	self.render("header.html",pagetitle=title)
    def render_content(self): 
    	self.render("home.html")
    def render_footer(self): 
    	self.render("footer.html")		
    def get(self):
        self.render_header("HomePage")
        self.render_content()
        self.render_footer()

app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
