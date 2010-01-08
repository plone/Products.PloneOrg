What is this?

  This is a Deliverance buildout for applying the new theme for plone.org using
  a slightly modified version of Deliverance called xdv.

How does it work?

  For development purposes, you might want to run the proxy version that doesn't
  require you to compile nginx and other related parts. See the nginx version 
  below if that's what you want to do instead.

  To install the development version:
  cd new.plone.org
  python bootstrap.py
  bin/buildout -c development.cfg

  Then, to run the proxy:
  bin/paster serve server.ini

  This will look for a Plone site at http://localhost:8080/demo and apply the
  new plone.org theme to it. If you want to replace this with a different 
  local/remote instance, edit 'server.ini'.

In the target site:

  (for this particular theme, not Deliverance/xdv in general)

  - Disable all CSS except for the Kupu stuff

  - Disable KSS

  - Turn off document_actions in /@@manage-viewlets

  - Note that the CSS won't carry over properly unless you have a version of
    ResourceRegistries that incorporates this change: 
    http://dev.plone.org/plone/changeset/23996
    (the symptoms will be that you don't get the Kupu CSS)

Using nginx

  You may need to install libxslt/libxml2/pcre (via MacPorts or your preferred
  packaging system) for this to work.  

  To install the production version:
  cd new.plone.org
  python bootstrap.py
  bin/buildout

  Then, to start nginx:
  
  Make sure you have set these environment variables:
    export LD_LIBRARY_PATH=${buildout:directory}/parts/libxml2/lib:${buildout:directory}/parts/libxslt/lib

  To start the process:
    bin/main start
  
  It is currently set up for proxying plone.org.
  
  (note: static/development.html is there as a representative page for testing)
