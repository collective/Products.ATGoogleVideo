# This Python file uses the following encoding: utf-8

__author__ = 'Héctor Velarde <hvelarde@jornada.com.mx>'
__docformat__ = 'restructuredtext'
__copyright__ = 'Copyright (C) 2005-2007  DEMOS, Desarrollo de Medios, S.A. de C.V.'
__license__  = 'The GNU General Public License version 2 or later'

from Products.ATContentTypes.interface import IATContentType
from Products.ATContentTypes.interface import IImageContent

class IATGoogleVideo(IATContentType, IImageContent):
    """ marker interface for ATGoogleVideo """
