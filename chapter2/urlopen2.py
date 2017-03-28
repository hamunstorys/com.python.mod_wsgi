import urllib.request

# HTTPBasicAuthHandler 클래스로 인증요청
auth_handler = urllib.request.HTTPBasicAuthHandler()
auth_handler.add_password(realm='PDQ Application',
                          uri='https://mahler:8092/site-updates.py',
                          user='klem',
                          passwd='kadidd!ehopper')
opener = urllib.request.build_opener(auth_handler)
# 디폴트 오프너로 설정하면 urlopen() 함수로 요청 가능
urllib.request.install_opener(opener)
urllib.request.urlopen('http://www.example.com/login.html')

# HTTPCookieProcessor 클래스로 쿠기 데이터를 포함하여 요청

# 쿠키 핸들러 생성, 쿠키 데이터 처리는 디폴트로 CookieJar 객체를 사용함
cookie_handler = urllib.request.HTTPCookieProcessor()

opener = urllib.request.build_opener(cookie_handler)
urllib.request.install_opener(opener)
# 쿠키 데이터와 함께 서버로 요청
u = urllib.request.urlopen("http://www.exmaple.com/login.html")

# ProxyHandler 및 ProxyBasicAuthHandler 클래스로 프록시 처리

proxy_handler = urllib.request.ProxyHandler({'http://www.example.com:3128/'})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')

opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
# install_opner(), urlopen() 함수 대신에 직접 open() 함수를 사용할 수 도 있다.
u = opener.open('http://www.example.com/login.html')
