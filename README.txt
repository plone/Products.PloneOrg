Introduction
============

This is the plone.org site package and corresponding buildout. It is used to
power http://plone.org. It is also a great buildut for working on developing 
Plone.org centric products such as PloneSoftwareCenter, PloneHelpCenter, and
PloneServicesCenter.

- Code repository: http://svn.plone.org/svn/plone/Products.PloneOrg
- Questions and comments to admins@lists.plone.org
- Report bugs to admins@lists.plone.org

The current supported version of Plone is: 4.1.x.


Production
----------

The default buildout setup is for setting up a production environment,
including Plone and nginx running under supervisor. (This won't be
functional without extra work, as other parts of the plone.org stack
such as the load balancer are not currently in the buildout.)
Run buildout as normal::

    $ python2.6 bootstrap.py
    $ bin/buildout
    $ sudo bin/supervisord

Development
-----------

To build plone.org for development, comment out the line in buildout.cfg that
says 'conf/production.cfg' and uncomment 'conf/develop.cfg'. Then proceed as
normal::

    $ python2.6 bootstrap.py
    $ bin/buildout
    $ bin/instance fg

This will get you an unthemed copy of the site. If you want to work on the
theme, you can build Plone + nginx by modifying buildout.cfg to use 
conf/develop_theme.cfg, and then run::

    $ python2.6 bootstrap.py
    $ bin/buildout
    $ bin/instance fg
    $ parts/nginx/sbin/nginx -c ../../etc/nginx.conf

The unthemed site is at http://localhost:8080. Go there and add a Plone site
with the id 'plone.org'.  The themed site is at http://localhost:5021/.

NOTE: Due to circumstances around testing the PloneOrg module, there 
are 2 directories with svn info. The source for Products.PloneOrg is in the 
'src' directory and the rest of the checked out packages are in 'sources'. If 
you can't find a checkout, double check BOTH directories.

Database
~~~~~~~~
To get the latest databases from plone.org, you just need to run the get_data 
shell script. It assumes rsync is in your path::

    $ ./conf/get_data

(This requires shell access to plone.org.)
