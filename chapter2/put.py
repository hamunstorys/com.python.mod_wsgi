# This creates an HTTP message
# with the content of BODY as the enclosed representation
# for the resource http://localhost:8888/file

import http.client

BODY = "***filecontents***"
conn = http.client.HTTPConnection("localhost", 8888)
conn.request("PUT", "/file.html", BODY)
response = conn.getresponse()
print(response.status, response.reason)
