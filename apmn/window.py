'''
Created on Dec 3, 2012

@author: superizer
'''

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QShortcut, QSplitter
from PyQt5.QtCore import Qt, pyqtSignal, QUrl, QVariant, QUrlQuery, QSize
from PyQt5.QtWebKitWidgets import QWebPage, QWebView, QWebInspector
from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtNetwork import *

from jinja2 import Environment, PackageLoader

import logging
logger = logging.getLogger(__name__)

import os

from . import context
from apmn_client.client import ApaimaneeClient

class WebPage(QWebPage):
    form_submitted = pyqtSignal(QUrl, QVariant)
    request_reload = pyqtSignal(QUrl)

    def acceptNavigationRequest(self, frame, req, nav_type):
        if nav_type == QWebPage.NavigationTypeFormSubmitted:
            forms = req.originatingObject().findAllElements('form')

            def get_attribute_form(inputs, elements):
                for input in inputs:
                    value_str = "this.value"
                    if input.attribute('type') == 'textarea':
                        value_str = "this.text"

                    elements[input.attribute('name')] = input.evaluateJavaScript(value_str)

            elements={}
            for form in forms:
                if form.attribute('action') in req.url().path():
                    inputs = form.findAll("input");
                    get_attribute_form(inputs, elements)

                    textareas = form.findAll("textarea");
                    get_attribute_form(textareas, elements)

                    selections = form.findAll("select");
                    get_attribute_form(selections, elements)

                    button = form.findAll("button");
                    get_attribute_form(button, elements)


            #print("elements: ", elements)
            self.form_submitted.emit(req.url(), elements)

        if nav_type == QWebPage.NavigationTypeReload:
            self.request_reload.emit(req.url())

        return super(WebPage, self).acceptNavigationRequest(frame, req, nav_type)


class Window(QWidget):

    session = dict()

    def __init__(self, config):
        super().__init__()
        self.setWindowTitle("Apaimanee MOBA");

        self.config = config

        self.base_uri = QUrl.fromLocalFile(os.path.dirname(__file__)).toString()

        # initial web view add handle all link and form submitted
        self.web_view = QWebView(self)
        self.web_view.setPage(WebPage())
        self.web_view.page().setLinkDelegationPolicy(QWebPage.DelegateAllLinks)
        self.web_view.page().linkClicked.connect(self.link_clicked)
        #self.web_view.page().urlChanged.connect(self.url_changed)
        self.web_view.page().loadFinished.connect(self.load_finished)
        self.web_view.page().loadStarted.connect(self.load_started)

        self.web_view.page().form_submitted.connect(self.handle_form_submitted)
        self.web_view.page().request_reload.connect(self.handle_reload)

        # initial template lookup

        self.template_env = Environment(loader=PackageLoader('apmn', 'templates'))
        #self.tempalte_lookup = TemplateLookup(directories=[self.config.settings.get("mako.directories")],
                                 #module_directory=self.config.settings.get("mako.module_directory"),
                                 #input_encoding='utf-8',
                                 #)

        # layout attribute
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)


        self.apaimanee_client = ApaimaneeClient(None, self.config.settings['apmn.host'], self.config.settings['apmn.port'])


        # add debug inspector
        if self.config.settings.get("debug", False):
            self.setup_inspector()
            self.splitter = QSplitter(self)
            self.splitter.setOrientation(Qt.Vertical)
            layout.addWidget(self.splitter)
            self.splitter.addWidget(self.web_view)
            self.splitter.addWidget(self.web_inspector)

        else:
            layout.addWidget(self.web_view)


    def setup_inspector(self):
        '''
            This code from http://agateau.com/2012/02/03/pyqtwebkit-experiments-part-2-debugging/
        '''
        page = self.web_view.page()
        page.settings().setAttribute(QWebSettings.DeveloperExtrasEnabled, True)
        self.web_inspector = QWebInspector(self)
        self.web_inspector.setPage(page)

        shortcut = QShortcut(self)
        shortcut.setKey(Qt.Key_F12)
        shortcut.activated.connect(self.toggle_inspector)
        self.web_inspector.setVisible(False)

    def toggle_inspector(self):
        self.web_inspector.setVisible(not self.web_inspector.isVisible())


    def handle_form_submitted(self, qurl, elements=dict()):

 #       print("\n\ngot url: ", qurl)
        qqurl = QUrlQuery(qurl)
        for key, value in qqurl.queryItems():
            elements[key] = value

        self.render(qurl.path(), elements)
        # do stuff with elements...
#        for item in elements.items():
#            print ("got: ", item)

    def handle_reload(self, qurl):
        self.render(qurl.path())

    def load_started(self):
        ''''''
        # print("load_started ->: ", self.web_view.url())


    def load_finished(self, finished):
        ''''''
        # print("load_finished ->: ", finished)
#        if finished:
#            self.web_view.setUrl(QUrl('/login'))

#     def url_changed(self, qurl):
#         ''''''
        # print("url_changed ->: ", qurl)

    def link_clicked(self, qurl):
        # print("link_clicked ->: ", qurl)
        qqurl = QUrlQuery(qurl)
        elements = {}
        # print("got link_clicked url: ", qurl)
        for key, value in qqurl.queryItems():
            elements[key] = value
        print(qurl.path())
        self.render(qurl.path(), elements)
        #self.render(qurl.path())


    def render(self, url, args=None):
        self.config.current_route_path = url
        print("current_route_path: ", self.config.current_route_path)
        logger.debug("url: %s" % url)
        route = self.config.get_route(url)
        logger.debug("view: %s" % route)

        if route is not None:
            view = route.get('view')
            context_obj = context.ResourceContext(self.config, self.session, self.apaimanee_client)
            context_obj.add_args(args)
            try:
                response = view(context_obj)
            except Exception as e:
                if e.args[0] == 'Request Exit':
                    self.close()
                    return

                logger.exception(e)
                #need error page
                return self.link_clicked('/home')


            if not isinstance(response, dict):
                if isinstance(response, QUrl):
                    return self.link_clicked(response)
#                    url = response.path()
#                    print('window url', url)
#                    return self.render(url)
#                else:
#                    # need error page
#                    return self.render('/login')

            logger.debug("response: %s"%response)

            template = self.template_env.get_template(
                            self.config.get_route(url).get('renderer')
                            )
            response['request'] = context_obj
            response['base_uri'] = self.base_uri
            html = template.render(**response)

            self.web_view.setHtml(html, QUrl("file://"+url))
            # self.web_view.setHtml(html)
            #self.web_view.load(a)

    def welcome(self):
        context_obj = context.ResourceContext(self.config, self.session)
        return self.link_clicked(context_obj.redirect_url('login'))
