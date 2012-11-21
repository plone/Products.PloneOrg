Introduction
============

This is the plone.org Plone add-on and buildout used to power http://plone.org.
It may also be used to develop Plone.org-centric add-ons such as
PloneSoftwareCenter, PloneHelpCenter, PloneServicesCenter, and Poi.

.. Note::

    The currently supported Plone version is: 4.2.x.

.. image:: https://github.com/plone/Products.PloneOrg/raw/master/screenshot.png

The `issue tracker`_ is at dev.plone.org; use the *Website* category.

.. _issue tracker: https://dev.plone.org/query?status=assigned&status=confirmed&status=new&status=reopened&component=Website&col=id&col=summary&col=status&col=type&col=priority&col=milestone&col=component&order=priority

Installation
============

Copy ``buildout.cfg.in`` to ``buildout.cfg`` and uncomment one of the following profiles.

Development
-----------

To build plone.org for development, uncomment out the line in buildout.cfg that
says ``conf/development.cfg`` then proceed as normal::

    $ python2.7 bootstrap.py
    $ bin/buildout
    $ bin/instance fg

.. Note:: 

    Due to circumstances around testing the PloneOrg module, there 
    are 2 directories with svn info. The source for Products.PloneOrg is in the 
    'src' directory and the rest of the checked out packages are in 'sources'. If 
    you can't find a checkout, double check BOTH directories.


Database
~~~~~~~~

To get the latest databases from plone.org, you just need to run the get_data 
shell script. It assumes ``rsync`` is in your path::

    $ ./conf/get_data

Alternatively, you may uncomment ``conf/database.cfg`` which extends ``conf/develop.cfg``
and uses ``collective.recipe.rsync`` to copy the data (which in turn assumes
that ``rsync`` is in your path).

.. Note::

    Both techniques require shell access to plone.org.

Production
----------

# XXX Update post deployment. Include something about how the buildout contains only the Plone software and no load balancers etc, as per cioppino previous rev.
