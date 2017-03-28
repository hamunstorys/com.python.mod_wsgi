# GET 방식 요청
from http import client

conn = client.HTTPConnection("www.example.com")
conn.request("GET", "/index.html")

r1 = conn.getresponse()
print(r1.status, r1.reason)

data1 = r1.read()
conn.request("GET", "/parrot.spam")
r2 = conn.getresponse()
print(r2.status, r2.reason)
data2 = r2.read()
conn.close()

# HEAD 방식 요청
from http import client

conn = client.HTTPConnection("www.example.com")
conn.request("HEAD", "/index.html")
res = conn.getresponse()
print(res.status, res.reason)
data = res.read()
print(len(data))

# POST 방식 요청
from http import client
from urllib import request
from urllib import parse

params = parse.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
headers = {"Content-type": "application/x-www-form-urlencoded",
           "Accept": "text/plain"}
conn = client.HTTPConnection("bugs.python.org")
conn.request("POST", "", params, headers)
response = conn.getresponse()
print(response.status, response.reason)  # 302F Found 리다이렉트 요청

