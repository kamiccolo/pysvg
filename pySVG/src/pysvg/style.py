#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
'''
(C) 2008, 2009 Kerim Mansour
For licensing information please refer to license.txt
'''
from attributes import *
from core import *

  
        
class style(BaseElement, CoreAttrib, XLinkAttrib):
    """
    Class representing the style element of an svg doc.
    """
    def __init__(self, ):
        BaseElement.__init__(self,'style')
    
    def set_type(self, type):
        self._attributes['type']=type
    def get_type(self):
        return self._attributes.get('type') 

    def set_media(self, media):
        self._attributes['media']=media
    def get_media(self):
        return self._attributes.get('media')
    
    def set_title(self, title):
        self._attributes['title']=title
    def get_title(self):
        return self._attributes.get('title')   
  
