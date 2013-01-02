# -*- coding: utf-8 -*-

from Products.ATContentTypes.interface import IATContentType
from Products.ATContentTypes.interface import IImageContent


class IATGoogleVideo(IATContentType, IImageContent):
    """ marker interface for ATGoogleVideo """
