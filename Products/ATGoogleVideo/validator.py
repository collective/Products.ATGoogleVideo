# -*- coding: utf-8 -*-
from zope.interface import implements
from Products.validation.interfaces.IValidator import IValidator
import re

from Products.ATGoogleVideo.config import PLONE_VERSION

class WidthHeightValidator:
    
    if PLONE_VERSION == 4:    
        implements(IValidator)
    else:
        __implements__ = (IValidator,)

    def __init__(self, name, title=u'width:height validation'):
        self.name = name
        self.title = title

    def __call__(self, value, *args, **kwargs):
        instance    = kwargs.get('instance', None)
        splited = value.split(':')
        # just the format 999+:999+
        if re.compile('([0-9]+)(:[0-9]+)?').match(value) is None:
            return u'Follow this format, please: "width:height"'
        return True