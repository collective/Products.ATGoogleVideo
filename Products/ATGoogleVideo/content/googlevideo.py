# -*- coding: utf-8 -*-

__author__ = 'Héctor Velarde <hvelarde@jornada.com.mx>'
__docformat__ = 'restructuredtext'
__copyright__ = 'Copyright (C) 2005-2007  DEMOS, Desarrollo de Medios, S.A. de C.V.'
__license__ = 'The GNU General Public License version 2 or later'

try:
    from Products.LinguaPlone.public import *
except ImportError:
    # No multilingual support
    from Products.Archetypes.public import *

from zope.interface import implements

from AccessControl import ClassSecurityInfo

from Products.ATContentTypes.content.document import ATCTContent
from Products.ATContentTypes.content.schemata import ATContentTypeSchema
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from Products.ATContentTypes.lib.historyaware import HistoryAwareMixin
from Products.ATContentTypes.lib.imagetransform import ATCTImageTransform
from Products.CMFCore.permissions import View
from Products.validation import V_REQUIRED

from Products.ATGoogleVideo.config import PROJECTNAME, QUALITY
from Products.ATGoogleVideo.interfaces import IATGoogleVideo

ATGoogleVideoSchema = ATContentTypeSchema.copy() + Schema((

    StringField('docId',
        languageIndependent=True,
        required=1,
        #searchable=True,
        widget=StringWidget(
            label='docId',
            label_msgid='label_docId',
            description='Video "docId" identifier.',
            description_msgid='help_docId',
            i18n_domain='ATGoogleVideo',
            size=20,
            ),
        ),

    StringField('quality',
        default='best',
        languageIndependent=True,
        required=1,
        enforceVocabulary=1,
        vocabulary=QUALITY,
        widget=SelectionWidget(
            label='Quality',
            label_msgid='label_quality',
            description='Specifies rendering quality, how graphics are anti-aliased and how bitmaps are smoothed. Use of "best" is recommended.',
            description_msgid='help_quality',
            i18n_domain='ATGoogleVideo',
            ),
        ),

    BooleanField('autoPlay',
        default=False,
        languageIndependent=True,
        required=False,
        widget=BooleanWidget(
            label='autoPlay',
            label_msgid='label_autoPlay',
            description='Specifies whether the movie begins playing immediately on loading in the browser.',
            description_msgid='help_autoPlay',
            i18n_domain='ATGoogleVideo',
            ),
        ),

    ImageField('image',
        languageIndependent=True,
        #max_size=zconf.ATGoogleVideo.max_image_dimension,
        storage=AnnotationStorage(migrate=True),
        sizes={
            'large': (768, 768),
            'preview': (400, 400),
            'mini': (200, 200),
            'thumb': (128, 128),
            'tile':  (64, 64),
            'icon':  (32, 32),
            'listing':  (16, 16),
            },
        validators=(('isNonEmptyFile', V_REQUIRED),),
        widget=ImageWidget(
            label='Image',
            label_msgid='label_image',
            description='Will be shown in the video listing. Image will be scaled to a sensible size.',
            description_msgid='help_image',
            i18n_domain='ATGoogleVideo',
            show_content_type=False,
            ),
        ),

    StringField('dimensions',
        default='425:350',
        required=True,
        validators=('isValidDimensions'),
        widget=StringWidget(
            label='Dimensions',
            label_msgid='label_dimensions',
            description='Video\'s dimensions according to format "width:height". If you give just one value, video\'s dimensions will be a given px square.',
            description_msgid='help_dimensions',
            i18n_domain='ATGoogleVideo',
            size=20,
            ),
        ),

    TextField('transcription',
        languageIndependent=False,
        storage=AnnotationStorage(migrate=True),
        required=False,
        searchable=True,
        default_output_type='text/x-html-safe',
        widget=RichWidget(
            label="Transcription",
            label_msgid="label_transcription",
            description="Video's audio transcripted.",
            description_msgid="help_transcription",
            i18n_domain="ATGoogleVideo",
        ),
    ),

    ),)

finalizeATCTSchema(ATGoogleVideoSchema)


class ATGoogleVideo(ATCTContent, HistoryAwareMixin, ATCTImageTransform):
    """ An Archetypes based type to store Google Video and YouTube references.
    """
    implements(IATGoogleVideo)
    security = ClassSecurityInfo()
    portal_type = 'Google Video'
    schema = ATGoogleVideoSchema
    _at_rename_after_creation = True

    security.declareProtected(View, 'tag')
    def tag(self, **kwargs):
        """Generate image tag using the api of the ImageField
        """
        return self.getField('image').tag(self, **kwargs)

    def __bobo_traverse__(self, REQUEST, name):
        """Transparent access to image scales
        """
        if name.startswith('image'):
            field = self.getField('image')
            image = None
            if name == 'image':
                image = field.getScale(self)
            else:
                scalename = name[len('image_'):]
                if scalename in field.getAvailableSizes(self):
                    image = field.getScale(self, scale=scalename)
            if image is not None and not isinstance(image, basestring):
                # image might be None or '' for empty images
                return image

        return ATCTContent.__bobo_traverse__(self, REQUEST, name)

    security.declarePublic('View')
    def getRemoteUrl(self):
        '''Returns docId from this object
           This way we don't need to add a new metadata to
           the catalog
        '''
        return self.getDocId()

    security.declarePublic('View')
    def getWidth(self):
        '''Extracts width from field 'dimensions'
        '''
        return self.getDimensions().split(':')[0]

    security.declarePublic('View')
    def getHeight(self):
        '''Extracts height from field 'dimensions'
        '''
        # Retrocompatibility
        dim = self.getDimensions().split(':')
        height = len(dim) > 1 and dim[1] or dim[0]
        return height

registerType(ATGoogleVideo, PROJECTNAME)
