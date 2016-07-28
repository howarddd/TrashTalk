from google.appengine.ext import ndb


class User(ndb.Model):
  identity = ndb.StringProperty(indexed=False)
  email = ndb.StringProperty(indexed=False)


class Event(ndb.Model):
  name = ndb.StringProperty(required=True)
  description = ndb.StringProperty()  # TODO: make this required?
  category = ndb.StringProperty(
    required=True,
    choices=['meeting', 'cleanup']
  )
  creator = ndb.StructuredProperty(User)

  created_at = ndb.DateTimeProperty(auto_now_add=True)
  updated_at = ndb.DateTimeProperty(auto_now=True)

  address = ndb.StringProperty()  # human readable location, optional





# [Example Models]
class Author(ndb.Model):
  """Sub model for representing an author."""
  identity = ndb.StringProperty(indexed=False)
  email = ndb.StringProperty(indexed=False)


class Greeting(ndb.Model):
  """A main model for representing an individual Guestbook entry."""
  author = ndb.StructuredProperty(Author)
  content = ndb.StringProperty(indexed=False)
  date = ndb.DateTimeProperty(auto_now_add=True)
