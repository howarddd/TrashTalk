from google.appengine.ext import ndb


class EventCreator(ndb.Model):
  identity = ndb.StringProperty()
  email = ndb.StringProperty()
  seeclickfix_username = ndb.StringProperty(required=True)
  seeclickfix_password = ndb.StringProperty(required=True)  # sorry Kyle


class Address(ndb.Model):
  street = ndb.StringProperty()
  zip = ndb.StringProperty()
  town = ndb.StringProperty()
  state = ndb.StringProperty()


class Event(ndb.Model):
  name = ndb.StringProperty(required=True)
  description = ndb.StringProperty()  # TODO: make this required?
  summary = ndb.StringProperty()
  category = ndb.StringProperty(
    required=True,
    choices=['meeting', 'cleanup']
  )
  creator = ndb.StructuredProperty(EventCreator)

  scf_issue_id = ndb.StringProperty()
  scheduled_date = ndb.DateTimeProperty()

  created_at = ndb.DateTimeProperty(auto_now_add=True)
  updated_at = ndb.DateTimeProperty(auto_now=True)

  address = ndb.StructuredProperty(Address)
  location = ndb.GeoPtProperty()  # lat/long




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
