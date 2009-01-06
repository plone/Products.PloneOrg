# Run 'python mirror.py' to copy existing-externally-stored-files to
# where they can be web-served (TARGET). New uploads will automatically
# be copied there.

import os
from os.path import join
import shutil

SOURCES = ('/srv/plone.org/zope/files', '/srv/plone.org/p3/var/files')
TARGET = '/srv/dist.plone.org/http/root/packages'

for SOURCE in SOURCES:
    for root, dirs, files in os.walk(SOURCE):
        file, ext = '', ''
        for file in files:
            ext = os.path.splitext(file)[-1]
            path = join(root, file)
            if ext not in ('.egg', '.zip', '.gz', '.tgz'):
                continue
            target = join(TARGET, file)
            if os.path.exists(target):
                continue   
            print 'Copying %s to %s' % (path, target)
            shutil.copy2(path, target)
   
print 'Done. make sure you fix the rights in %s' % TARGET

