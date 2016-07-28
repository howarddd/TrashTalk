import webapp2
import json
import datetime

from google.appengine.ext import ndb
from google.appengine.api import users
from trashtalk import models
from trashtalk import geo_handler


def address_to_latlong(street, zip, town, state):
  addr_str = '{street} {town} {state}, {zip}'.format(
    street=street,
    town=town,
    zip=zip,
    state=state
  )
  return geo_handler.get_lat_long(addr_str)


def date_and_location_serializer(obj):
  """JSON serializer for objects not serializable by default json code"""

  if isinstance(obj, datetime.datetime):
    serial = obj.isoformat()
    return serial
  elif isinstance(obj, ndb.GeoPt):
    serial = (obj.lat, obj.lon)
    return serial
  raise TypeError("Type not serializable")


class EventHandler(webapp2.RequestHandler):

  def get(self):
    events = models.Event.query().fetch()
    self.response.write(
      json.dumps(
        [e.to_dict() for e in events],
        default=date_and_location_serializer
      )
    )


  def post(self):
    user_email = self.request.get('user_email')
    scf_username = self.request.get('scf_username')
    scf_password = self.request.get('scf_password')
    name = self.request.get('name')
    description = self.request.get('description')
    category = self.request.get('category')
    scheduled_date = self.request.get('scheduled_date')  # TODO: parse this and make it required
    summary = self.request.get('summary')
    address_street = self.request.get('address_street')
    address_zip = self.request.get('address_zip')
    address_town = self.request.get('address_town')
    address_state = self.request.get('address_state')
    latitude = self.request.get('latitude')
    longitude = self.request.get('longitude')

    # Validate the input
    required = [user_email, scf_username, scf_password, name, category, summary]
    if not all(required):
      raise webapp2.exc.HTTPBadRequest('missing required fields')
    has_full_address = address_state and address_street and address_zip and address_town
    if not has_full_address:
      raise webapp2.exc.HTTPBadRequest('need a full address')
    user = users.get_current_user()
    if not user:
      raise webapp2.exc.HTTPUnauthorized('no user is authenticated')

    # Create the datastore Event and put it
    event_creator = models.EventCreator(
      identity=user.user_id(),
      email=user.email(),
      seeclickfix_username=scf_username,
      seeclickfix_password=scf_password
    )
    address = models.Address(
      street=address_street, zip=address_zip, town=address_town, state=address_town
    )
    if latitude and longitude:
      location = ndb.GeoPt(latitude, longitude)
    else:
      latitude, longitude = address_to_latlong(address_street, address_zip, address_town, address_state)
      location = ndb.GeoPt(latitude, longitude)

    new_event = models.Event(
      name=name, description=description, category=category, creator=event_creator,
      address=address, location=location, summary=summary
    )
    new_event.put()

    self.response.write('OK')  # TODO: This sends out a 200, right?


class EventHandlerSingle(webapp2.RequestHandler):
  def get(self, event_id):
    event_id = int(event_id)
    event = ndb.Key(models.Event, event_id).get()
    self.response.write(json.dumps(event.to_dict(), default=date_and_location_serializer))
