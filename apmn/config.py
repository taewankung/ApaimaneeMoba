'''
Created on Dec 3, 2012

@author: superizer
'''

import os
import configparser

class Configuration:
    '''
    classdocs
    '''

    def __init__(self, config_file=None):
        self.config_file = config_file
        self.settings = dict()
        self.route = dict()
        self.current_project_path = os.path.dirname(__file__)
        self.current_route_path = None

        self.__parse()

    def __parse(self):

        sections = ["hawkeye"]

        boolean_conf    = ['debug']
        integer_conf    = ['nokkhum.api.port']


        for key in boolean_conf:
            self.settings[key] = False

        self.settings['debug'] = True
        if self.config_file is None:
            return

        config_parser = configparser.ConfigParser()
        config_parser.read(self.config_file)

        for section in sections:
            if not config_parser.has_section(section):
                continue

            for k, v in config_parser.items(section):
                if k in boolean_conf:
                    self.settings[k] = config_parser.getboolean(section, k)
                elif k in integer_conf:
                    self.settings[k] = config_parser.getint(section, k)
                else:
                    self.settings[k] = v.replace("hawkeye:", self.current_project_path+"/")



    def add_route(self, name, url, view, renderer=None):
        self.route[name] = dict(
                                name=name,
                                url=url,
                                view=view,
                                renderer=renderer
                                )
    def get_route(self, name):
        if self.route.get(name, None):
            return self.route.get(name)

        for k, v in self.route.items():
            if v['url'] == name:
                return v

        return None

