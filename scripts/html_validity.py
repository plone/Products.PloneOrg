"""
Simple script to reproduce parsing problems.
usage: python html_validity.py <url>
"""

from lxml import etree
from urllib2 import urlopen
import urlparse
import sys

url = sys.argv[1]
path = urlparse.urlsplit(url)[2]
plone_url = 'http://plone.org:5011/VirtualHostBase/http/plone.org:80/plone.org/VirtualHostRoot%s' % path
print "Fetching %s" % plone_url
response = urlopen(plone_url)
data = response.read()
header_len = len('HTTP/1.0 200 OK\r\n') + len(''.join(response.headers.headers)) + len('\r\n')

CHUNK_SIZE = 1024 # ZServer.HTTPResponse.ZServerHTTPResponse.http_chunk_size

print 'Parsing...\n'

pos = CHUNK_SIZE - header_len # offset headers
chunk = data[:pos]
p = etree.HTMLParser()
while chunk:
    try:
        p.feed(chunk)
    except etree.XMLSyntaxError, e:
        line, column = e.position
        print '\n'.join(data.split('\n')[line-10:line])
        print '-'*(column-1)+'^'
        raise
    else:
        next = pos + CHUNK_SIZE
        chunk = data[pos:next]
        pos = next

print 'Parsed OK.'