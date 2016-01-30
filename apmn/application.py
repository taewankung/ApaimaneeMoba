'''
Created on Dec 2, 2012

@author: superizer
'''
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebKit import *
from PyQt5.QtWidgets import QApplication

from .window import Window
import sys

import logging
logger = logging.getLogger(__name__)

from . import routing

class Application(object):
    '''
    classdocs
    '''
    def __init__(self, config):
        '''
        Constructor
        '''

        self.app = QApplication(sys.argv)
        self.config = config
        routing.add_route(config)

    def start(self):

        window = Window(self.config)
        window.showMaximized()
        window.welcome()
        return self.app.exec_()
