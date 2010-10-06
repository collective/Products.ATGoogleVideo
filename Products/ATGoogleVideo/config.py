# BBB for CMF 1.4
try:
    from Products.CMFCore.permissions import setDefaultRoles
except ImportError:
    from Products.CMFCore.CMFCorePermissions import setDefaultRoles

try:
    # Plone 4 and higher 
    import plone.app.upgrade 
    PLONE_VERSION = 4 
except ImportError: 
    PLONE_VERSION = 3

PROJECTNAME = 'ATGoogleVideo'
DEFAULT_ADD_CONTENT_PERMISSION = "Add Google Video"

setDefaultRoles(DEFAULT_ADD_CONTENT_PERMISSION, ('Manager', 'Owner',))

# Flash video quality
QUALITY = ('low', 'high', 'autolow', 'autohigh', 'best',)
