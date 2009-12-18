# This Python file uses the following encoding: utf-8

"""
$Id$
"""

__author__ = 'Héctor Velarde <hvelarde@jornada.com.mx>'
__docformat__ = 'restructuredtext'
__copyright__ = 'Copyright (C) 2007  DEMOS, Desarrollo de Medios, S.A. de C.V.'
__license__  = 'The GNU General Public License version 2 or later'

import os, sys
if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

# Import the base test case classes
from base import ATGoogleVideoTestCase

from Products.ATGoogleVideo.config import *

class TestInstallation(ATGoogleVideoTestCase):
    """Ensure product is properly installed"""

    def afterSetUp(self):
        self.catalog    = self.portal.portal_catalog
        self.kupu       = self.portal.kupu_library_tool
        self.skins      = self.portal.portal_skins
        self.types      = self.portal.portal_types
        self.factory    = self.portal.portal_factory
        self.properties = self.portal.portal_properties
        self.metaTypes = ('Google Video',)

    def testSkinLayersInstalled(self):
        self.failUnless('atgooglevideo_images' in self.skins.objectIds())
        self.failUnless('atgooglevideo_templates' in self.skins.objectIds())

    def testTypesInstalled(self):
        for t in self.metaTypes:
            self.failUnless(t in self.types.objectIds())

    def testPortalFactorySetup(self):
        self.failUnless('Google Video' in self.factory.getFactoryTypes())

    def testDefaultPageTypes(self):
        """test that Google Video is an acceptable default-page type"""
        self.failUnless('Google Video' in self.properties.site_properties.getProperty('default_page_types'))

    def testKupuResources(self):
        """test that Google Video is in Kupu's linkable types"""
        linkable = self.kupu.getPortalTypesForResourceType('linkable')
        self.failUnless('Google Video' in linkable)

class TestUninstall(ATGoogleVideoTestCase):
    """ensure product is properly uninstalled"""

    def afterSetUp(self):
        self.kupu = self.portal.kupu_library_tool
        self.properties = self.portal.portal_properties
        self.qitool = self.portal.portal_quickinstaller
        self.qitool.uninstallProducts(products=[PROJECTNAME])

    def testProductUninstalled(self):
        self.failIf(self.qitool.isProductInstalled(PROJECTNAME))

def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestInstallation))
    suite.addTest(makeSuite(TestUninstall))
    return suite

if __name__ == '__main__':
    framework()
