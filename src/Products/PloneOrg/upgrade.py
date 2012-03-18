import logging
from Products.CMFCore.utils import getToolByName
from zope.globalrequest import getRequest

logger = logging.getLogger('Products.PloneOrg')


def step_1(context):
    wftool = context.portal_workflow
    if 'collector_issue_workflow' in wftool.objectIds():
        wftool.manage_delObjects(['collector_issue_workflow'])


def reindex_effectiveRange(context):
	"""Reindex effectiveRange.

	This is used prior to one of the Plone 4.2 upgrade steps to
	keep the step from breaking.
	"""
	logger.info('Reindexing broken effectiveRange index...')
	catalog = getToolByName(context, 'portal_catalog')
	catalog.clearIndex('effectiveRange')
	catalog.reindexIndex('effectiveRange', getRequest())


def update_portal_css_conditions(context):
	"""Diazo uses a different variable to indicate theming than we did with xdv.

	So we need to update the conditions.
	"""
	logger.info('Updating portal_css conditions for Diazo...')
	portal_css = getToolByName(context, 'portal_css')
	for stylesheet in portal_css.resources:
		if 'request/HTTP_X_XDV' in stylesheet.getExpression():
			expression = stylesheet.getExpression().replace(
				'request/HTTP_X_XDV',
				'request/HTTP_X_THEME_ENABLED | nothing'
				)
			stylesheet.setExpression(expression)
