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

#from Interface.Verify import verifyObject
from zope.schema import getValidationErrors
from Products.ATContentTypes.interface import IATContentType
from Products.ATContentTypes.interface import IImageContent
from Products.ATContentTypes.lib.historyaware import HistoryAwareMixin
from Products.ATContentTypes.lib.imagetransform import ATCTImageTransform

from Products.ATGoogleVideo.config import *
from Products.ATGoogleVideo.interfaces import IATGoogleVideo

class TestContentType(ATGoogleVideoTestCase):
    """ ensure content type implementation """

    def afterSetUp(self):
        self.folder.invokeFactory('Google Video', 'video1')
        self.video1 = getattr(self.folder, 'video1')

    def testImplementsATContentType(self):
        iface = IATContentType
        self.assertTrue(iface.providedBy(self.video1))
        self.assertFalse(getValidationErrors(iface, self.video1))

    def testImplementsImageContent(self):
        iface = IImageContent
        self.assertTrue(iface.providedBy(self.video1))
        self.assertFalse(getValidationErrors(iface, self.video1))

    def testImplementsATGoogleVideo(self):
        iface = IATGoogleVideo
        self.assertTrue(iface.providedBy(self.video1))
        self.assertFalse(getValidationErrors(iface, self.video1))

    def testIsHistoryAwareMixin(self):
        self.assertTrue(isinstance(self.video1, HistoryAwareMixin))

    def testIsATCTImageTransform(self):
        self.assertTrue(isinstance(self.video1, ATCTImageTransform))

def isValidGoogleVideoId(id):
    """ Google Video ids are 18 or 19 digits, with or without a minus sign before """
    import re
    p = re.compile('^-?\d{18,19}$')
    return p.match(id) != None

def isValidYouTubeId(id):
    """ YouTube ids are 11 alphanumeric characters, minus signs or underscores """
    import re
    p = re.compile('^[\w-]{11}$')
    return p.match(id) != None

class TestContentCreation(ATGoogleVideoTestCase):
    """ ensure content type can be created and edited """

    def afterSetUp(self):
        self.folder.invokeFactory('Google Video', 'video1')
        self.video1 = getattr(self.folder, 'video1')

    def testCreateGoogleVideo(self):
        self.failUnless('video1' in self.folder.objectIds())

    def testEditGoogleVideo(self):
        self.video1.setTitle('A title')
        self.video1.setDescription('A description')
        self.video1.setDocId('7111080333836653411')
        self.video1.setAutoPlay(True)
        self.video1.setTranscription('<p><b>Simon says:</b> get up, get down</p>')
        
        self.assertEqual(self.video1.Title(), 'A title')
        self.assertEqual(self.video1.Description(), 'A description')
        self.assertEqual(self.video1.getDocId(), '7111080333836653411')
        self.assertEqual(self.video1.getAutoPlay(), True)
        self.assertEqual(self.video1.getTranscription(), '<p><b>Simon says:</b> get up, get down</p>')

    def testGoogleVideoValidation(self):
        """ this will be used when validation is implemented """
        validGoogleVideo = (
            '7111080333836653411',
            '2373913889068217879',
            '1384277706451157121',
            '-6176702600168718216',
            '-988521890368706730',
            '-6947118853654187245',
            '-6744496180655305393',
            '-9136575504838642038',
            '507732229697832036',
            '-421067427884933323',
        )
        for id in validGoogleVideo:
            self.failUnless(isValidGoogleVideoId(id))

    def testGoogleVideoInvalidation(self):
        """ this will be used when validation is implemented """
        knownWrong = (
            '+6176702600168718216',
            '6A309553DDC2ECB427',
            '-CE622B1BD7578F9916',
            '11108033336653411',
            '50773222969783203',
            'nojWJ6-XmeQ',
            'JahdnOQ9XCA',
            'VcQIwbvGRKU',
            'sMEnn0xJ0l0',
            '9VKlskwm378',
        )
        for id in knownWrong:
            self.failUnless(not isValidGoogleVideoId(id))

    def testYouTubeValidation(self):
        """ this will be used when validation is implemented """
        validYouTube = (
            'nojWJ6-XmeQ',
            'JahdnOQ9XCA',
            'VcQIwbvGRKU',
            'sMEnn0xJ0l0',
            '9VKlskwm378',
            'mdBfbUy-Oz0',
            '_fqbznoeEOI',
            'EpSK0OriE7w',
            '76f2d3AlXxc',
            'QWUh585V2mM',
        )
        for id in validYouTube:
            self.failUnless(isValidYouTubeId(id))

    def testYouTubeInvalidation(self):
        """ this will be used when validation is implemented """
        knownWrong = (
            'nojWJ6-Xme',
            'Jahdn*Q9XCA',
            '-CE622B1BD7578F9916',
            'sMnn0xJ0l0',
            '507732229697',
            '-6947118853654187245',
            '-6744496180655305393',
            '-9136575504838642038',
            '507732229697832036',
            '-421067427884933323',
        )
        for id in knownWrong:
            self.failUnless(not isValidYouTubeId(id))

def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestContentType))
    suite.addTest(makeSuite(TestContentCreation))
    return suite

if __name__ == '__main__':
    framework()
