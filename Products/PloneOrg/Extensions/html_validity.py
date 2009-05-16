"""
External method to reproduce parsing problems.
usage: html_validity?url=<url>
"""

from lxml import etree
from urllib2 import urlopen
import urlparse

def html_validity(self, url):
    request = self.REQUEST
    request.RESPONSE.setHeader('Content-Type','text/plain')
    path = urlparse.urlsplit(url)[2]
    plone_path = request['PATH_INFO'].split('VirtualHostRoot')[0]
    plone_url = 'http://%s/%sVirtualHostRoot%s' % (request['HTTP_HOST'], plone_path, path)
    response = urlopen(plone_url)
    data = response.read()
    header_len = len('HTTP/1.0 200 OK\r\n') + len(''.join(response.headers.headers)) + len('\r\n')

    CHUNK_SIZE = 1024 # ZServer.HTTPResponse.ZServerHTTPResponse.http_chunk_size


    pos = CHUNK_SIZE - header_len # offset headers
    chunk = data[:pos]
    p = etree.HTMLParser()
    while chunk:
        try:
            p.feed(chunk)
        except etree.XMLSyntaxError, e:
            line, column = e.position
            msg = data.split('\n')[line-10:line]
            msg.append('-'*(column-1)+'^')
            msg.append('%s, line %s, column %s' % (e.error_log, line, column))
            return '\n'.join(msg)
        else:
            next = pos + CHUNK_SIZE
            chunk = data[pos:next]
            pos = next

    return 'Parsed OK.'
