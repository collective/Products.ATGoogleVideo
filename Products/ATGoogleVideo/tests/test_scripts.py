# -*- coding: utf-8 -*-

__author__ = 'Héctor Velarde <hvelarde@jornada.com.mx>'
__docformat__ = 'restructuredtext'
__copyright__ = 'Copyright (C) 2007  DEMOS, Desarrollo de Medios, S.A. de C.V.'
__license__ = 'The GNU General Public License version 2 or later'

import unittest2 as unittest

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles

from Products.ATGoogleVideo.testing import INTEGRATION_TESTING


class TestGetLatestVideo(unittest.TestCase):
    """Ensure latest video is obtained"""

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('Folder', 'test-folder')
        setRoles(self.portal, TEST_USER_ID, ['Member'])
        self.folder = self.portal['test-folder']

        self.folder.invokeFactory('Google Video', 'video1')
        self.video1 = getattr(self.folder, 'video1')
        self.video1.setTitle('A title')
        self.video1.setDescription('A description')
        self.video1.setDocId('7111080333836653411')
        self.video1.setQuality('best')
        self.video1.setAutoPlay(False)
        self.video1.setTranscription('<p>video\'s transcription</p>')
        self.video1.setDimensions('300:150')

    def testIfVideoUnpublishedResultIsEmpty(self):
        self.assertTrue(self.folder.getLatestGoogleVideo() is None)

    def testIfVideoPublishedResultIsNotEmpty(self):
        wf = self.portal['portal_workflow']
        types = ('Google Video', )
        wf.setChainForPortalTypes(types, 'simple_publication_workflow')
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        wf.doActionFor(self.video1, 'publish')
        self.assertTrue(self.folder.getLatestGoogleVideo() is not None)

    def _testLatestVideoBrain(self):
        """this is not working because attributes are not indexed correctly"""
        self.video1.content_status_modify(workflow_action='publish')
        latest_video = self.folder.getLatestGoogleVideo()
        self.assertEqual(latest_video.Title, 'A title')
        self.assertEqual(latest_video.Description, 'A description')
        self.assertEqual(latest_video.docId, '7111080333836653411')
        self.assertEqual(latest_video.quality, 'best')
        self.assertEqual(latest_video.autoPlay, False)
        self.assertEqual(latest_video.getTranscription(), '<p>video\'s transcription</p>')
        self.assertEqual(latest_video.getWidth(), '300')
        self.assertEqual(latest_video.getHeight(), '150')


GOOGLE_VIDEO_BASE_CODE = """
    /* <![CDATA[ */
    var FO = { movie:'http://video.google.com/googleplayer.swf?docId=%s', width:'%s', height:'%s', majorversion:'9', build:'28', flashvars:'%s', quality:'%s', wmode:'transparent', setcontainercss:'true' };
    UFO.create(FO, 'video');
    /* ]]> */
"""

YOUTUBE_BASE_CODE = """
    /* <![CDATA[ */
    var FO = { movie:'http://www.youtube.com/v/%s%s', width:'%s', height:'%s', majorversion:'9', build:'28', flashvars:'', quality:'%s', wmode:'transparent', setcontainercss:'true' };
    UFO.create(FO, 'video');
    /* ]]> */
"""


class TestUFOJSCode(unittest.TestCase):
    """Ensure Javascript code for UFO is generated"""

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('Folder', 'test-folder')
        setRoles(self.portal, TEST_USER_ID, ['Member'])
        self.folder = self.portal['test-folder']

        self.folder.invokeFactory('Google Video', 'video1')
        self.video1 = getattr(self.folder, 'video1')
        self.video1.setTitle('A title')
        self.video1.setDescription('A description')
        self.video1.setQuality('best')
        self.video1.setAutoPlay(False)
        self.video1.setTranscription('<p>video\'s transcription</p>')
        self.video1.setDimensions('300:150')

    def testUFOForGoogleVideo(self):
        self.video1.setDocId('7111080333836653411')
        code = GOOGLE_VIDEO_BASE_CODE % ('7111080333836653411', '300', '150', '', 'best')
        ufo_code = self.folder.getUFOJSCodeFromVideo(self.video1.getDocId(), self.video1.getQuality(), self.video1.getAutoPlay(), width=self.video1.getWidth(), height=self.video1.getHeight())
        self.assertEqual(code, ufo_code)

        self.video1.setQuality('low')
        self.video1.setAutoPlay(True)
        code = GOOGLE_VIDEO_BASE_CODE % ('7111080333836653411', '300', '150', 'autoplay=true', 'low')
        ufo_code = self.folder.getUFOJSCodeFromVideo(self.video1.getDocId(), self.video1.getQuality(), self.video1.getAutoPlay(), width=self.video1.getWidth(), height=self.video1.getHeight())
        self.assertEqual(code, ufo_code)

    def testUFOForYouTube(self):
        self.video1.setDocId('nojWJ6-XmeQ')
        code = YOUTUBE_BASE_CODE % ('nojWJ6-XmeQ', '', '300', '150', 'best')
        ufo_code = self.folder.getUFOJSCodeFromVideo(self.video1.getDocId(), self.video1.getQuality(), self.video1.getAutoPlay(), width=self.video1.getWidth(), height=self.video1.getHeight())
        self.assertEqual(code, ufo_code)

        self.video1.setQuality('low')
        self.video1.setAutoPlay(True)
        code = YOUTUBE_BASE_CODE % ('nojWJ6-XmeQ', '&amp;autoplay=1', '300', '150', 'low')
        ufo_code = self.folder.getUFOJSCodeFromVideo(self.video1.getDocId(), self.video1.getQuality(), self.video1.getAutoPlay(), width=self.video1.getWidth(), height=self.video1.getHeight())
        self.assertEqual(code, ufo_code)


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
