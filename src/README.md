#TrashTalk-Oakland
TrashTalk-Oakland - Trashtalk.com will essentially act as a liaison between: Oakland's Department of Public Works and the Oakland Adopt-A Volunteer Program...fueled by community leaders starting cleanups within their community (or defined areas/location of interest)

#App Technology Overview
- Built with Python and hosted on [Google App Engine](https://cloud.google.com/appengine/).
- Uses [Google Cloud APIs](https://cloud.google.com) for authentication, storage and location services.
- Uses [Optimizely OUI](http://design.optimizely.com/oui/index.html)for design.

#Pages
- Landing page with list of events
- Schedule an event

#Endpoints
- /event - a GET post to this returns the data for all the saved events, a POST request made will save an event. A POST request needs the following fields:
user_email
scf_username
scf_password
name
description (optional)
category
address_street
address_zip
address_town
address_state
latitude
longitude
the POST request either needs lat/long, or all of the address fields, or both
- /event_single/{id} - a GET request to this returns the data for a single event. Requires the event id

#Things to Note
- On /schedules you'll get an error if you give an incorrect location (e.g. incorrect zipcode) 
- On /schedules you'll get an error if you give an incorrect SeeClickFix user/pass