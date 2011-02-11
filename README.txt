PloneOrg buildout
=================

This is the plone.org site package and corresponding buildout. It is used to
power http://plone.org.

Install
-------

To install and run Plone (only), follow these steps::

    $ python2.6 bootstrap.py -d
    $ bin/buildout
    $ bin/instance fg

Develop
-------
To install and run Plone for development (including add-ons such as PloneSoftwareCenter), 
follow these steps::

    $ python2.6 bootstrap.py -d
    $ bin/buildout -c conf/develop.cfg
    $ bin/instance fg

For other Plone.org buildout configs, please follow the steps in docs/DEVELOPER.txt 

