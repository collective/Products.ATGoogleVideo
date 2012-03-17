# -*- coding: utf-8 -*-

__author__ = 'Héctor Velarde <hvelarde@jornada.com.mx>'
__docformat__ = 'restructuredtext'
__copyright__ = 'Copyright (C) 2007  DEMOS, Desarrollo de Medios, S.A. de C.V.'
__license__ = 'The GNU General Public License version 2 or later'

import unittest2 as unittest

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles

from Products.ATGoogleVideo.config import PROJECTNAME
from Products.ATGoogleVideo.testing import INTEGRATION_TESTING


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
