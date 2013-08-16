Introduction
============

This is the plone.org Plone add-on and buildout used to power http://plone.org. It may also be used to develop Plone.org-centric add-ons such as PloneSoftwareCenter, PloneHelpCenter, PloneServicesCenter, and Poi.

.. Note::

    The currently supported Plone version is: 4.3.2-pending.

.. image:: https://github.com/plone/Products.PloneOrg/raw/master/screenshot.png

The `issue tracker`_ is located at https://dev.plone.org; please use the *Website* category.

.. _issue tracker: https://dev.plone.org/query?status=assigned&status=confirmed&status=new&status=reopened&component=Website&col=id&col=summary&col=status&col=type&col=priority&col=milestone&col=component&order=priority

Installation
============

Copy ``buildout.cfg.in`` to ``buildout.cfg`` and uncomment one of the following profiles.

Development
-----------

Instructions.

Clone::

    git clone git@github.com:plone/Products.PloneOrg.git

Create buildout.cfg::

    cp buildout.cfg.in buildout.cfg

Edit it::

    [buildout]
    # Rename to buildout.cfg and uncomment one of the profiles below
    extends =
    # Copy data local (with plone.org account)
        conf/database.cfg

Set up your `SSH keys for plone.org <http://opensourcehacker.com/2012/10/24/ssh-key-and-passwordless-login-basics-for-developers/>`_.

Run Buildout::

    python bootstrap.py
    bin/buildout

This will create plone.org configuration and rsync cleaned ``Data.fs`` and related files from plone.org for your local computer. The data size is around 5 GB (2013/04), so see instructions below how to avoid the copying in the future buildout runs.

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

First test your changes on the staging server, then deploy on plone.org primary.

Staging
----------

In the case if you don't have ``staging.plone.org`` domain record add to your ``/etc/hosts``::

    74.203.223.202 staging.plone.org

**Note**: Always use http:// URLs to access staging, as https:// URLs are not currently routed correctly and end up to live *plone.org*.

Example how to update ``staging.plone.org``::

    ssh plone.org

    # Test on staging
    sudo -i -u zope
    cd /srv/staging.plone.org
    # See we are running before starting to mess with things
    bin/supervisorctl status

    # Pull in patched Products.PloneOrg, run buildout, restart
    git pull
    /usr/local/Python-2.6.5/bin/python2.6 bootstrap.py -v1.7.1  # Let's fix that zc.buildout upgrade problem
    bin/buildout -c conf/staging.cfg
    exit

    # supervisord restart must be pulled in as a root
    cd /srv/staging.plone.org
    sudo bash -c "bin/supervisorctl stop all && sleep 1 && bin/supervisorctl shutdown && sleep 1 && bin/supervisord && bin/supervisorctl start all"

    # Check it came up
    sudo bin/supervisorctl status

    # Check instance1 is running
    telnet 10.57.0.107 6011

    # Check nginx is running
    telnet 10.57.0.107 6021

    # NOTE: Make sure dist.plone.org is not controlled by staging nginx?
    # See /usr/local/etc/varnish/default.vcl

    # See that http://staging.plone.org comes up
    # Login with your live LDAP credentials to http://staging.plone.org/login
    # Test your patch


Production
----------

.. Note:: Production NGINX and HAProxy configuration files are located here: https://github.com/plone/plone-org-nginx, https://github.com/plone/plone-org-haproxy

.. Warning:: Production Python version is currently: /usr/local/Python-2.6.5/bin/python. If you need to re-bootstrap, please remember to use this Python.

Update live *plone.org*::

    sudo -i -u zope
    cd /srv/plone.org
    git pull
    bin/buildout
    bin/supervisorctl stop plone.org-client-instance{1,2,3,4} && sleep 10 && bin/supervisorctl start plone.org-client-instance{1,2,3,4}

    # Test instance1 responds
    telnet 10.57.0.107 5011

    # Restart the rest of the stuff
    sleep 120 && bin/supervisorctl stop plone.org-client-instance{5,6,7,8} && sleep 10 && bin/supervisorctl start plone.org-client-instance{5,6,7,8}

More info

* https://github.com/plone/ploneorg.admin/blob/master/docs/services.rst

Production logs
===============

To view::

    ssh plone.org
    cd /srv/plone.org ; tail -f var/log/instance{1..8}.log

Changes
=========

Please update ``docs/HISTORY.txt`` and ``docs/CONTRIBUTORS.txt`` regarding changes in the setup.

Upgrades
=========

Please update ``docs/UPGRADES.txt`` regarding upgrade notes run on *plone.org*.

Maintenance guide
===================

Please update `developer.plone.org <https://github.com/plone/ploneorg.admin/blob/master/docs/services.rst>`_ maintenance guide regarding system setup and sysadmin tasks
for *plone.org*.


Top level Zope
--------------

Sometimes… not always… but sometimes: you need access to the top level of Zope. For security reasons, we don't expose these ports to the internet. But you can still get to them via ssh tunnel.

To complicate matters, not only are the ports restricted to listen on a non-routable IP address (typically 127.0.0.1 AKA localhost) they are configured to listen on a privately routable IP address for internal configuration management purposes.

So, if you are a plone.org admin (i.e. with the proper credentials), you can do this::

    $ ssh -L localhost:8080:10.57.0.107:5011 direct.plone.org

Then visit http://localhost:8080/manage to login to plone.org.
