# -*- coding: utf-8 -*-

import unittest2 as unittest

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles

from Products.ATGoogleVideo.config import PLONE_VERSION
from Products.ATGoogleVideo.config import PROJECTNAME
from Products.ATGoogleVideo.testing import INTEGRATION_TESTING

from Products.CMFCore.utils import getToolByName


class TestInstallation(unittest.TestCase):
    """Ensure product is properly installed"""

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.catalog = self.portal.portal_catalog
        self.skins = self.portal.portal_skins
        self.types = self.portal.portal_types
        self.factory = self.portal.portal_factory
        self.properties = self.portal.portal_properties
        self.metaTypes = ('Google Video',)

    def testSkinLayersInstalled(self):
        self.assertTrue('atgooglevideo_images' in self.skins.objectIds())
        self.assertTrue('atgooglevideo_templates' in self.skins.objectIds())

    def testTypesInstalled(self):
        for t in self.metaTypes:
            self.assertTrue(t in self.types.objectIds())

    def testPortalFactorySetup(self):
        self.assertTrue('Google Video' in self.factory.getFactoryTypes())

    def testDefaultPageTypes(self):
        """test that Google Video is an acceptable default-page type"""
        site_properties = self.properties.site_properties
        self.assertTrue('Google Video' in site_properties.getProperty('default_page_types'))

    @unittest.skipIf(PLONE_VERSION > 3, "skipping test for Kupu editor")
    def testKupuLinkable(self):
        """ test if Google Video is linkable in kupu
        """
        kupuTool = getToolByName(self.portal, 'kupu_library_tool', None)
        if kupuTool is not None:
            linkable = list(kupuTool.getPortalTypesForResourceType('linkable'))
            self.asserTrue('Google Video' in linkable)


class TestUninstall(unittest.TestCase):
    """ensure product is properly uninstalled"""

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.properties = self.portal.portal_properties
        self.qitool = self.portal.portal_quickinstaller
        self.qitool.uninstallProducts(products=[PROJECTNAME])

    def testProductUninstalled(self):
        self.assertFalse(self.qitool.isProductInstalled(PROJECTNAME))


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
