# This Python file uses the following encoding: utf-8

"""
this test suite was based on Martin Aspeli's 'borg' and David Convent's 'DIYPloneStyle' ones

tested on Plone 2.5.5

$Id$
"""

from Products.ATGoogleVideo.config import PROJECTNAME
from Testing import ZopeTestCase

# Let Zope know about the two products we require above-and-beyond a basic
# Plone install (PloneTestCase takes care of these).
ZopeTestCase.installProduct(PROJECTNAME)

# Import PloneTestCase - this registers more products with Zope as a side effect
from Products.PloneTestCase.PloneTestCase import PloneTestCase
from Products.PloneTestCase.PloneTestCase import FunctionalTestCase
from Products.PloneTestCase.PloneTestCase import setupPloneSite

# Set up a Plone site
setupPloneSite(products=[PROJECTNAME])

class ATGoogleVideoTestCase(PloneTestCase):
    """Base class for integration tests for the 'JuliusLite' product. This may
    provide specific set-up and tear-down operations, or provide convenience
    methods.
    """

class ATGoogleVideoFunctionalTestCase(FunctionalTestCase):
    """Base class for functional integration tests for the 'JuliusLite' product. 
    This may provide specific set-up and tear-down operations, or provide 
    convenience methods.
    """
