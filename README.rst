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

Instructions.

Clone::

    git clone git@github.com:plone/Products.PloneOrg.git

Create b.out::

    cp buildout.cfg.in buildout.cfg

Edit it::

    [buildout]
    # Rename to buildout.cfg and uncomment one of the profiles below
    extends =
    # Copy data local (with plone.org account)
        conf/database.cfg

Set up your `SSH keys for plone.org <http://opensourcehacker.com/2012/10/24/ssh-key-and-passwordless-login-basics-for-developers/>`_.

Run buildout::

    python bootstrap.py -v 1.6.3
    bin/buildout

This will create p.org configuration and rsync cleaned ``Data.fs``
and related files from plone.org for your local computer. The data
size is around 5 GB (2013/04), so see instructions below
how to avoid the copying in the future buildout runs.

Create an admin user for yourself::

    bin/instance adduser admin2 admin

Start::

    bin/instance fg

(First startup after fresh Data.fs copy takes time.)

Visit `http://localhost:8080/plone.org <http://localhost:8080/plone.org>`_.

Admin password is ``admin2`` / ``admin``.

Rebuilding the copy
------------------------

To run buildout without sync::

    bin/buildout install instance omelette  # And other parts here you might need here too

Deployment
==============

First test changes on the staging, then deploy on plone.org

Example::

    ssh plone.or

    # Test on staging
    cd /srv/staging.plone.org
    sudo -u zope git pull
    sudo -u zope /usr/local/Python-2.6.5/bin/python2.6 bootstrap.py -v1.7.1
    sudo -u zope bin/buildout -c conf/staging.cfg
    sudo -u zope bin/plonectl restart

    # See that http://staging.plone.org comes up

    # Update live
    # TODO
    cd /srv/plone.org
    sudo -u zope git pull
    bin/buildout

Changes
=========

Please update ``docs/HISTORY.txt`` and ``docs/CONTRIBUTORS.txt`` regarding changes in the setup.

Upgrades
=========

Please update ``docs/UPGRADES.txt`` regarding upgrade notes run on *plone.org*.

Maintenance guide
===================

Please update ``developer.plone.org`` maintenance guide regarding system setup and sysadmin tasks
for *plone.org*.



