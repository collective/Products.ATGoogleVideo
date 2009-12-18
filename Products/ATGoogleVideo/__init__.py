from Products.CMFCore import utils, DirectoryView
from Products.Archetypes.atapi import listTypes, process_types

import sys, content

# Module aliases
sys.modules['Products.ATGoogleVideo.ATGoogleVideo'] = content.googlevideo

# Get configuration data, permissions
from config import PROJECTNAME, DEFAULT_ADD_CONTENT_PERMISSION

# Register skin directories so they can be added to portal_skins
DirectoryView.registerDirectory('skins', globals())

def initialize(context):

    # Import the type, which results in registerType() being called
    from content import ATGoogleVideo

    contentTypes, constructors, ftis = process_types(listTypes(PROJECTNAME), PROJECTNAME)
 
    utils.ContentInit(
        PROJECTNAME + ' Content',
        content_types      = contentTypes,
        permission         = DEFAULT_ADD_CONTENT_PERMISSION,
        extra_constructors = constructors,
        fti                = ftis,
        ).initialize(context)
