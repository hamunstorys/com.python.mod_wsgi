#!/usr/bin/env python
#
from urllib import request
from html.parser import HTMLParser


class ImageParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag != 'img':
            return
        if not hasattr(self, 'result'):
            self.result = []
        for name, value in attrs:
            if name == 'src':
                self.result.append(value)


def parseImage(data):
    parser = ImageParser()
    parser.feed(data)
    dataSet = set(x for x in parser.result)
    print('\n'.join(sorted(dataSet)))


def main():
    url = "http://www.google.co.kr"
    f = request.urlopen(url)
    charset = f.headers.get_content_charset()
    data = f.read().decode(charset)

    print("\n>>>>>>>>> Fetch Images from", url)
    parseImage(data)


if __name__ == '__main__':
    main()
