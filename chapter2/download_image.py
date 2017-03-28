#!/usr/bin/env python
#
from urllib import request
from urllib import parse
from http import client
from html.parser import HTMLParser
import os


class ImageParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag != 'img':
            return
        if not hasattr(self, 'result'):
            self.result = []
        for name, value in attrs:
            if name == 'src':
                self.result.append(value)


def downloadImage(srcUrl, data):
    if not os.path.exists('DOWNLOAD'):  # 패키지 안의 DOWNLOAD 폴더가 있는 지 확인함
        os.makedirs('DOWNLOAD')  # 없을 경우 DOWNLOAD 디렉토리 생성

    parser = ImageParser()
    parser.feed(data)
    resultSet = set(x for x in parser.result)

    for x in sorted(resultSet):
        src = parse.urljoin(srcUrl, x)
        basename = os.path.basename(src)
        targetFile = os.path.join('DOWNLOAD', basename)

        print("Downloading..."), src
        request.urlretrieve(src, targetFile)


def main():
    host = "www.google.com"

    conn = client.HTTPConnection(host)
    conn.request("GET", '')
    resp = conn.getresponse()

    charset = resp.headers.get_content_charset()
    data = resp.read().decode(charset)
    conn.close()

    print("\n>>>>>>>>> Download Images from", host)
    url = request.urlunparse(('http', host, '', '', '', ''))
    downloadImage(url, data)


if __name__ == '__main__':
    main()
