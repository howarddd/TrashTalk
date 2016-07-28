import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

##
# Main App
##

class Home(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            sign_out_url = users.create_logout_url(self.request.uri)
            template_values = {
                'sign_out_url': sign_out_url,
            }
            
        else:
            sign_in_url = users.create_login_url(self.request.uri)
            template_values = {
                'sign_in_url': sign_in_url,
            }

        template = JINJA_ENVIRONMENT.get_template('./templates/index.html')
        self.response.write(template.render(template_values))


class SignIn(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            sign_out_url = users.create_logout_url(self.request.uri)
            template_values = {
                'sign_out_url': sign_out_url,
            }
            template = JINJA_ENVIRONMENT.get_template('./templates/signin.html')
            self.response.write(template.render(template_values))

        else:
            sign_in_url = users.create_login_url(self.request.uri)
            self.redirect(sign_in_url)



app = webapp2.WSGIApplication([
    ('/', Home),
    ('/signin', SignIn),
], debug=True)