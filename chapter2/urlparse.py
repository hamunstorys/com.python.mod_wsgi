from urllib import parse

result = parse.urlparse("http://www.python.org:80/guido/python/guido/python.html;philosophy?overall=3#n10")
print(result)
