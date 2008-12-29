import os
from os.path import join
import shutil

SOURCE = '/srv/plone.org/zope/files'
TARGET = '/srv/dist.plone.org/http/root/packages'

for root, dirs, files in os.walk(SOURCE):
    for file in files:
        ext = os.path.splitext(file)[-1]
	path = join(root, file)
	if ext not in ('.egg', '.zip', '.gz', '.tgz'):
	    continue
	target = join(TARGET, file)
    print 'Copying %s to %s' % (path, target)
	shutil.copyfile(path, target)
	

