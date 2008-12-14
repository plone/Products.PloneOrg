Introduction
============

This is the site product for plone.org. It contains custom templates, images,
browser views, etc. responsible for turning a default Plone site into
plone.org.

Development
===========

(This assumes you have an account on antiloop.)

To use plone.org data:
    1. svn co http://svn.plone.org/svn/plone/Products.PloneOrg/trunk/ PloneOrg
    2. cd PloneOrg
    3. python2.4 bootstrap.py
    4. bin/buildout -c database.cfg
    5. go get coffee
    6. cp database/Data.fs var/filestorage
    7. cp database/CatalogData.fs var/filestorage
    8. bin/instance fg
