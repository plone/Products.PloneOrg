PloneOrg buildout
=================

This is the plone.org policy product and corresponding buildout. It is used to
power http://plone.org.

- Code repository: http://svn.plone.org/svn/plone/Products.PloneOrg
- Questions and comments to admins@lists.plone.org
- Report bugs to admins@lists.plone.org

As of July 2010, trunk supports Plone 4.

Base
----

A base buildout good enough to run the plone.org Data.fs and CatalogData.fs 
can be built with::

    $ python2.6 bootstrap.py
    $ bin/buildout
    $ bin/instance fg

Develop
-------

A development buildout with trunk checkouts of all of plone.org's dependencies 
can be built with::

    $ python2.6 bootstrap.py
    $ bin/buildout -c profiles/develop.cfg
    $ bin/instance fg

Database
--------

If you need the data, and you have a plone.org account, you can do this::

    $ python2.6 bootstrap.py
    $ bin/buildout -c profiles/database.cfg
    $ bin/instance fg

Production
----------

A production build, suitable for running on plone.org can be built with::

    $ python2.6 bootstrap.py
    $ bin/buildout -c profiles/production.cfg
    $ bin/instance fg

Questions/comments/concerns? Email admins@plone.org.

