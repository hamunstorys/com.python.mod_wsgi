from urllib import request
from urllib import parse

# GET 방식 요청(Request)1
with request.urlopen('http://www.python.org/') as f:
    print(f.read(300))

# GET 방식 요청(Request)2
f = request.urlopen("http://www.example.com")
print(f.read(500))

# POST 방식 요청(Request)
data = "query=python".encode("utf-8")  # bytes type으로 Encoding해서 매개인수로 입력해야한다.
f = request.urlopen("http://www.example.com", data, )
print(f.read(300))

# Request Class로 요청 헤더 지정
req = request.Request("http://www.example.com", data="query=python".encode('utf-8'), method='POST')  # POST 방식 요청
req.add_header("Content-Type", "text/plain")
f = request.urlopen(req)
print(f.read(300))

