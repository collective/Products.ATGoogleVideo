# BBB for CMF 1.4
try:
    from Products.CMFCore.permissions import setDefaultRoles
except ImportError:
    from Products.CMFCore.CMFCorePermissions import setDefaultRoles

PROJECTNAME = 'ATGoogleVideo'
DEFAULT_ADD_CONTENT_PERMISSION = "Add Google Video"

setDefaultRoles(DEFAULT_ADD_CONTENT_PERMISSION, ('Manager', 'Owner',))

# Flash video quality
QUALITY = ('low', 'high', 'autolow', 'autohigh', 'best',)
