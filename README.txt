PloneOrg buildout
=================

This is the plone.org site package and corresponding buildout. It is used to
power http://plone.org. It is also a great buildut for working on developing 
Plone.org centric products such as PloneSoftwareCenter. 

- Code repository: http://svn.plone.org/svn/plone/Products.PloneOrg
- Questions and comments to admins@lists.plone.org
- Report bugs to admins@lists.plone.org


Production
----------
The default buildout setup is for setting up a development environment.
To deploy to a production environment, uncomment the line that says 
'conf/production.cfg' and comment out 'conf/develop.cfg'. Then 
procede as normal::

    $ python2.6 bootstrap.py
    $ bin/buildout
    $ bin/supervisord

Develop
-------
The default config for this buildout is development mode. Run buildout as
normal::

    $ python2.6 bootstrap.py
    $ bin/buildout
    $ bin/instance zeoserver
    $ bin/instance fg

Database
~~~~~~~~
To get the latest databases from plone.org, you just need to run the get_data 
shell script. It assumes rsync is in your path::

    $ ./conf/get_data

