import os
from os.path import join
import shutil

SOURCE = '/srv/plone.org/files'
TARGET = '/srv/plone.org/mirror'

for root, dirs, files in os.walk(SOURCE):
    for file in files:
        ext = os.path.splitext(file)[-1]
	path = join(root, file)
	if ext not in ('.egg', '.zip', '.gz', '.tgz'):
	    continue
	target = join(MIRROR, file)
	shutil.copyfile(path, target)
	

