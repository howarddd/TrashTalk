import os
import urllib
from trashtalk import handlers

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

##
# App
##

class Home(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            auth_url = users.create_logout_url(self.request.uri)
            auth_text = 'Sign Out'
        else:
            auth_url = users.create_login_url(self.request.uri)
            auth_text = 'Sign In'

        template_values = {
            'auth_url': auth_url,
            'auth_text': auth_text,
        }

        template = JINJA_ENVIRONMENT.get_template('./templates/index.html')
        self.response.write(template.render(template_values))


class Schedule(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            auth_url = users.create_logout_url(self.request.uri)
            auth_text = 'Sign Out'
        else:
            auth_url = users.create_login_url(self.request.uri)
            auth_text = 'Sign In'

        template_values = {
            'auth_url': auth_url,
            'auth_text': auth_text,
        }

        template = JINJA_ENVIRONMENT.get_template('./templates/schedule.html')
        self.response.write(template.render(template_values))


app = webapp2.WSGIApplication([
    ('/', Home),
    ('/event', handlers.EventHandler),
    ('/schedule', Schedule),
], debug=True)
