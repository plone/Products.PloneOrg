#!/usr/bin/python

import os, sys, commands

source='antiloop.plone.org:/srv/plone.org'
dest='/srv/backup.plone.org/rsync/antiloop/plone.org'

def backup(source, dest):
    print 'Backing up %s' % source
    out = commands.getoutput('rsync -e ssh --partial --progress -av %s/ %s/' % 
        (source, dest))
    print out
    print '\n\n'

def main(argv, source, dest):
    backup(source, dest)

if __name__ == "__main__":
    main(sys.argv[1:], source, dest)
