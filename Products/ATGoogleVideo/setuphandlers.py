from Products.CMFCore.utils import getToolByName

def setupATGoogleVideo(context):

    # to avoid GS run this step again if product has been inspected
    # for an import_steps.xml again.
    if context.readDataFile('atgooglevideo_various.txt') is None:
        return

    portal = context.getSite()

    # Add Google Video to Kupu's linkable types, if Kupu is installed
    kupuTool = getToolByName(portal, 'kupu_library_tool', None)
    if kupuTool != None:
        linkable = list(kupuTool.getPortalTypesForResourceType('linkable'))
        if 'Google Video' not in linkable:
            linkable.append('Google Video')
        kupuTool.updateResourceTypes(({'resource_type' : 'linkable',
                                       'old_type'      : 'linkable',
                                       'portal_types'  :  linkable},))
