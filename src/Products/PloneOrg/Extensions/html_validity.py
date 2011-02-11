"""
External method to reproduce parsing problems.
usage: html_validity?url=<url>
"""

from lxml import etree
from urllib2 import urlopen, Request, HTTPError
import urlparse

def html_validity(self, url):
    request = self.REQUEST
    request.RESPONSE.setHeader('Content-Type','text/plain')
    path, qs = urlparse.urlsplit(url)[2:4]
    if qs:
        path += '?' + qs
    #plone_path = request['PATH_INFO'].split('VirtualHostRoot')[0]
    plone_path = 'VirtualHostBase/http/plone.org:80/plone.org/'
    plone_url = 'http://%s/%sVirtualHostRoot%s' % (request['HTTP_HOST'], plone_path, path)
    request.environ['debug_plone_url'] = plone_url
    new_req = Request(plone_url)
    cookie = request.environ.get('HTTP_COOKIE', None)
    if cookie is not None:
        new_req.add_header('Cookie', cookie)
    try:
        response = urlopen(new_req)
    except HTTPError, e:
        return 'Error opening url.\n%s' % e
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
            msg.append('%s: %s' % (e.__class__.__name__, e.args[0].encode('utf-8')))
            msg.append(str(p.feed_error_log))
            return '\n'.join(msg)
        else:
            next = pos + CHUNK_SIZE
            chunk = data[pos:next]
            pos = next

    return 'Parsed OK.'
