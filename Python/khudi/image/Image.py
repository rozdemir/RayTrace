#!/usr/bin/env python
""" generated source for module Image """
from __future__ import print_function
from abc import ABCMeta, abstractmethod
# package: khudi.image
class Image(object):
    """ generated source for interface Image """
    __metaclass__ = ABCMeta
    @abstractmethod
    def Read(self, filename):
        """ generated source for method Read """

    @abstractmethod
    def Write(self, filename):
        """ generated source for method Write """

    @abstractmethod
    def SetColor(self, r, g, b):
        """ generated source for method SetColor """

