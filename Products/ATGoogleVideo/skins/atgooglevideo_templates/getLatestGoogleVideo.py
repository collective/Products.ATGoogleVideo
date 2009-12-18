""" returns the latest video """

from Products.CMFCore.utils import getToolByName

catalog = getToolByName(context, 'portal_catalog')
results = catalog.searchResults(portal_type='Google Video',
                                review_state='published',
                                sort_on='effective',
                                sort_order='reverse',
                                sort_limit=1)[:1]
if results:
    return results[0]
