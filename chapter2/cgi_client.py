from urllib import request
from urllib import parse

url = "http://localhost:8888/cgi-bin/script.py"
data = {
    'language': 'python',
    'framework': 'django',
    'email': 'kim@naver.com'
}
# encData = parse.urlencode(data)

charset = request.urlopen(url).read().get_content_charset()
encData = request.urlopen(url).read().decode(charset)

f = request.urlopen(url, encData)  # POST
print(f.read())
