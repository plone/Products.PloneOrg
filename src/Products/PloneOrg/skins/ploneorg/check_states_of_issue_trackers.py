## Script (Python) "check_states_of_issue_trackers"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
# Example code:

# Import a standard function, and get the HTML request and response objects.
from Products.PythonScripts.standard import html_quote
request = container.REQUEST
RESPONSE =  request.RESPONSE

pc = context.portal_catalog
pois = pc(portal_type='PoiPscTracker' )


states={}

for i in pois:
    if i.review_state in states.keys():
        states[i.review_state]= states[i.review_state]+1
    else:
        states[i.review_state]=1

return states
