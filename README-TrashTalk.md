# TrashTalk
Repo for artifacts of the Trash Talk app for organizing cleanups and graffiti abatement.

Goal -- Develop code that finds anyone interested in a specified geographical area, with the ability to communicate "scheduled cleanups".

Trashtalk.com will essentially act as a liaison between: Oakland's Department of Public Works and the Oakland Adopt-A Volunteer Program...fueled by community leaders starting cleanups within their community (or defined areas/location of interest)

In order to act as an integrator, TrashTalk will need to manage a datastore of cleanup events and volunteers.  It also needs to message interested individual neighbors using seeclickfix.com via the seeclickfix API v2.  This is where coding help is requested.   We need help:
==> Using the API to collect ID tokens of people 'watching" an area that will host a cleanup
==> Writing the queries to find those individuals
==> Writing and addressing the clean up invitations to those individuals via the API
==> Creating tables for the ID tokens and the real contact info
==> Managing this info to send to the City of Oakland's Adopt-a-site and Volunteer hours apps

Information on the Seeclickfix API is available here:

http://dev.seeclickfix.com/


Other areas that will need to inherently be developed are:
==> A database umbrella based off the seeclickfix api
==> Page listing of "Clean-up Sites Near You" (with a JOIN feature)
==> Geofencing/Geomapping feature for linking an individual with a service area preference

Also … making a Mobile app and Website to help users navigate this information
Registration feature for smart phones  (i.e. QRcode 'neighborhood registration' feature -- Version 2)

Architectural approach

Trash Talk will be both a Mobile App and a web site so as to provide wide demographic coverage for all citizens regardless of age and social and economic status.  Seniors and low income students still use web sites first or exclusively so a fully functional web site for the application is necessary.

Because this is a utility for the community, and it will be supported by less technical personnel, a serverless architecture is probably best to reduce the management requirements for the backend. We plan to use a website proxy for desktop users, that connects to the application logic.  That would be best provided by a cloud service such as Google App Engine or AWS Lambda.  Assistance in setting up Google App Engine would very helpful and could be a Day 0 activity.  

The proxy web site could be set up via Google Sites or services such as Wix or Square, separating the design and UX components from the backend application logic.
