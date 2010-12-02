Plone.org
=========

This is the plone.org website package and buildout.

Installation
------------

This package allows people to easily develop and deploy the plone.org
community website.

You can install it like so::

    $ svn co https://svn.plone.org/svn/plone/Products.PloneOrg/trunk Products.PloneOrg
    $ cd Products.PloneOrg
    $ python bootstrap.py -d
    $ bin/buildout
    $ bin/plone fg

Now check http://localhost:8080. You should be able to add a Plone site and
install the Products.PloneOrg add-on.

.. Note::

    This initial setup makes a few compromises::

    * The ``develop`` parameter is used to tell Buildout to include this
      package. The rest of the (non-dev) packages come from PyPI or
      dist.plone.org.
    * There is no plone.org data.

Development
-----------

Please see docs/DEVELOPER.txt


Contact
-------

Questions/comments/concerns? Please email: admins@plone.org.

