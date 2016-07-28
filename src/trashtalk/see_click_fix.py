"""Information we will need to create an issue in SCF:
lat = latitude of event
lng = longitute of event
address = street address of event
summary = Subject of event
description = body of event (should contain link to TrashTalk event)
username = user's email address registered in SCF
password = user's SFC password

create_issue(37.805559, -122.268921, "1561 Franklin Ave, Oakland, CA", "Testing create_issue 3", "description goes here", "evanpweiss@gmail.com", "password123")
"""

import urllib2
import base64
import json

def create_issue(lat, lng, address, summary, description, username, password):
    data={
        "lat":lat,
        "lng":lng,
        "address":address,
        "request_type_id":"other",
        "answers": {
            "summary": summary,
            "description": description
        }
    }
    api_request = urllib2.Request("https://seeclickfix.com/api/v2/issues")
    api_request.add_header("Content-type", "application/json")
    api_request.add_header("Authorization", "Basic "+base64.b64encode(username+":"+password))
    api_response = urllib2.urlopen(api_request, json.dumps(data))
    response_data = json.loads(api_response.read())
    return response_data