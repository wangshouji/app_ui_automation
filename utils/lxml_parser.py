#!/user/bin/env python
#coding=utf-8
from lxml import etree
import urllib
import time
import re


class MyLxmlParser(object):

    def __init__(self , html = None , xpath = None , parser = 'html'):
        """
         parser = html,xpath not is None,else parser = xml ,xpath can be None
        :param html: if parser = html , is string ,else parser = xml ,is file path
        :param xpath:
        :param parser: html , xml
        """
        if parser == 'html' and xpath is not None:
            self.etree_elements = etree.HTML(html)
            self.etree_elementTrees = etree.ElementTree(self.etree_elements)
            self.elements = self.etree_elements.xpath(xpath)
            self.parent_elements = self.etree_elements.xpath(xpath)
            self.attrs = []
        elif parser == 'xml' and xpath is not None:
            self.etree_elementTrees = etree.parse(html)
            self.etree_elements = self.etree_elementTrees.getroot()
            self.elements = self.etree_elements.xpath(xpath)
            self.parent_elements = self.etree_elements.xpath(xpath)
            self.attrs = []


    def parser_selenium_html(self , etree_elements = None , etree_elementTrees = None , elements = None ,
                    parent_elements = None):
        """
            parser selenium html page
        :param etree_elements:
        :param etree_elementTrees:
        :param elements:
        :param parent_elements:
        :return:
        """
        if len(elements) > 0:
            parent = elements[0]
        for element in elements:
            parent_elements.pop(parent_elements.index(element))
            attr = element.attrib
            if 'id' in parent.getparent().attrib.keys():
                attr['xpath'] = '//*[@id="' + parent.getparent().attrib['id'] + '"]' + \
                                etree_elementTrees.getpath(element).split(
                                    etree_elementTrees.getpath(parent.getparent()))[1]
            else:
                attr['xpath'] = '/' + etree_elementTrees.getpath(element). \
                    split(etree_elementTrees.getpath(parent.getparent()))[1]
            if 'id' in element.attrib.keys():
                attr['xpath'] = '//*[@id="' + element.attrib['id'] + '"]'
                child_elements = etree_elements.xpath(etree_elementTrees.getpath(element) + '//*')
                self.parser_selenium_html(etree_elements=etree_elements, etree_elementTrees=etree_elementTrees,
                       elements=child_elements, parent_elements=elements)
            self.attrs.append(attr)


    def parser_uiautomator_xml(self , etree_elements = None , etree_elementTrees = None , elements = None ,
                    parent_elements = None):
        """
            parser uiautomator2_up xml page
        :param etree_elements:
        :param etree_elementTrees:
        :param elements:
        :param parent_elements:
        :return:
        """
        if len(elements) > 0:
            parent = elements[0]
            for element in elements:
                element.tag = element.attrib['class']
        for element in elements:
            try:
                parent_elements.pop(parent_elements.index(element))
            except ValueError as e:
                pass
            attr = element.attrib
            if 'resource-id' in parent.getparent().attrib.keys() and parent.getparent().attrib['resource-id'] !='':
                attr['xpath'] = '//*[@resource-id="' + parent.getparent().attrib['resource-id'] + '"]' + \
                                etree_elementTrees.getpath(element).split(
                                    etree_elementTrees.getpath(parent.getparent()))[1]
            else:
                attr['xpath'] = '/' + etree_elementTrees.getpath(element). \
                    split(etree_elementTrees.getpath(parent.getparent()))[1]
            if 'resource-id' in element.attrib.keys() and element.attrib['resource-id'] !='':
                attr['xpath'] = '//*[@resource-id="' + element.attrib['resource-id'] + '"]'
                if len(etree_elementTrees.xpath(attr['xpath'])) > 1:
                    if 'text' in element.attrib.keys() and element.attrib['text'] !='':
                        attr['xpath'] = '//' + element.tag + '[@text="' + element.attrib['text'] + '"]'
                    elif 'content-desc' in element.attrib.keys() and element.attrib['content-desc'] !='':
                        attr['xpath'] = '//' + element.tag + '[@content-desc="' + element.attrib['content-desc'] + '"]'
                    else:
                        attr['xpath'] = '/' + etree_elementTrees.getpath(element). \
                            split(etree_elementTrees.getpath(parent.getparent()))[1]
                child_elements = etree_elements.xpath(etree_elementTrees.getpath(element) + '//*')
                self.parser_uiautomator_xml(etree_elements=etree_elements, etree_elementTrees=etree_elementTrees,
                       elements=child_elements, parent_elements=elements)
            elif 'text' in element.attrib.keys() and element.attrib['text'] !='':
                attr['xpath'] = '//' + element.tag +'[@text="' + element.attrib['text'] + '"]'
            elif 'content-desc' in element.attrib.keys() and element.attrib['content-desc'] !='':
                attr['xpath'] = '//' + element.tag + '[@content-desc="' + element.attrib['content-desc'] + '"]'
            self.attrs.append(attr)

    def parser_appium_android_xml(self , etree_elements = None , etree_elementTrees = None , elements = None ,
                    parent_elements = None):
        """
            parser uiautomator2_up xml page
        :param etree_elements:
        :param etree_elementTrees:
        :param elements:
        :param parent_elements:
        :return:
        """
        if len(elements) > 0:
            parent = elements[0]
        for element in elements:
            try:
                parent_elements.pop(parent_elements.index(element))
            except ValueError as e:
                pass
            attr = element.attrib
            if 'resource-id' in parent.getparent().attrib.keys() and parent.getparent().attrib['resource-id'] !='':
                attr['xpath'] = '//*[@resource-id="' + parent.getparent().attrib['resource-id'] + '"]' + \
                                etree_elementTrees.getpath(element).split(
                                    etree_elementTrees.getpath(parent.getparent()))[1]
            else:
                attr['xpath'] = '/' + etree_elementTrees.getpath(element). \
                    split(etree_elementTrees.getpath(parent.getparent()))[1]
            if 'resource-id' in element.attrib.keys() and element.attrib['resource-id'] !='':
                attr['xpath'] = '//*[@resource-id="' + element.attrib['resource-id'] + '"]'
                if len(etree_elementTrees.xpath(attr['xpath'])) > 1:
                    if 'text' in element.attrib.keys() and element.attrib['text'] !='':
                        attr['xpath'] = '//' + element.tag + '[@text="' + element.attrib['text'] + '"]'
                    elif 'content-desc' in element.attrib.keys() and element.attrib['content-desc'] !='':
                        attr['xpath'] = '//' + element.tag + '[@content-desc="' + element.attrib['content-desc'] + '"]'
                    else:
                        attr['xpath'] = '/' + etree_elementTrees.getpath(element). \
                            split(etree_elementTrees.getpath(parent.getparent()))[1]
                child_elements = etree_elements.xpath(etree_elementTrees.getpath(element) + '//*')
                self.parser_appium_android_xml(etree_elements=etree_elements, etree_elementTrees=etree_elementTrees,
                       elements=child_elements, parent_elements=elements)
            elif 'text' in element.attrib.keys() and element.attrib['text'] !='':
                attr['xpath'] = '//' + element.tag +'[@text="' + element.attrib['text'] + '"]'
            elif 'content-desc' in element.attrib.keys() and element.attrib['content-desc'] !='':
                attr['xpath'] = '//' + element.tag + '[@content-desc="' + element.attrib['content-desc'] + '"]'
            self.attrs.append(attr)


    def parser_appium_ios_xml(self , etree_elements = None , etree_elementTrees = None , elements = None ,
                    parent_elements = None):
        """
            parser uiautomator2_up xml page
        :param etree_elements:
        :param etree_elementTrees:
        :param elements:
        :param parent_elements:
        :return:
        """
        if len(elements) > 0:
            parent = elements[0]
        for element in elements:
            try:
                parent_elements.pop(parent_elements.index(element))
            except ValueError as e:
                pass
            attr = element.attrib
            if 'name' in parent.getparent().attrib.keys() and parent.getparent().attrib['name'] !='':
                attr['xpath'] = '//*[@name="' + parent.getparent().attrib['name'] + '"]' + \
                                etree_elementTrees.getpath(element).split(
                                    etree_elementTrees.getpath(parent.getparent()))[1]
            else:
                attr['xpath'] = '/' + etree_elementTrees.getpath(element). \
                    split(etree_elementTrees.getpath(parent.getparent()))[1]
            if 'name' in element.attrib.keys() and element.attrib['name'] !='':
                attr['xpath'] = '//*[@name="' + element.attrib['name'] + '"]'
                if len(etree_elementTrees.xpath(attr['xpath'])) > 1:
                    if 'label' in element.attrib.keys() and element.attrib['label'] !='':
                        attr['xpath'] = '//' + element.tag + '[@label="' + element.attrib['label'] + '"]'
                    elif 'value' in element.attrib.keys() and element.attrib['value'] !='':
                        attr['xpath'] = '//' + element.tag + '[@value="' + element.attrib['value'] + '"]'
                    else:
                        attr['xpath'] = '/' + etree_elementTrees.getpath(element). \
                            split(etree_elementTrees.getpath(parent.getparent()))[1]
                child_elements = etree_elements.xpath(etree_elementTrees.getpath(element) + '//*')
                self.parser_appium_ios_xml(etree_elements=etree_elements, etree_elementTrees=etree_elementTrees,
                       elements=child_elements, parent_elements=elements)
            elif 'label' in element.attrib.keys() and element.attrib['label'] != '':
                attr['xpath'] = '//' + element.tag + '[@label="' + element.attrib['label'] + '"]'
            elif 'value' in element.attrib.keys() and element.attrib['value'] != '':
                attr['xpath'] = '//' + element.tag + '[@value="' + element.attrib['value'] + '"]'
            self.attrs.append(attr)

    def parser_macaca_xml(self , etree_elements = None , etree_elementTrees = None , elements = None ,
                    parent_elements = None):
        """
            parser uiautomator2_up xml page
        :param etree_elements:
        :param etree_elementTrees:
        :param elements:
        :param parent_elements:
        :return:
        """
        if len(elements) > 0:
            parent = elements[0]
        for element in elements:
            try:
                parent_elements.pop(parent_elements.index(element))
            except ValueError as e:
                pass
            attr = element.attrib
            if 'resource-id' in parent.getparent().attrib.keys() and parent.getparent().attrib['resource-id'] !='':
                attr['xpath'] = '//*[@resource-id="' + parent.getparent().attrib['resource-id'] + '"]' + \
                                etree_elementTrees.getpath(element).split(
                                    etree_elementTrees.getpath(parent.getparent()))[1]
            else:
                attr['xpath'] = '/' + etree_elementTrees.getpath(element). \
                    split(etree_elementTrees.getpath(parent.getparent()))[1]
            if 'resource-id' in element.attrib.keys() and element.attrib['resource-id'] !='':
                attr['xpath'] = '//*[@resource-id="' + element.attrib['resource-id'] + '"]'
                child_elements = etree_elements.xpath(etree_elementTrees.getpath(element) + '//*')
                self.parser_macaca_xml(etree_elements=etree_elements, etree_elementTrees=etree_elementTrees,
                       elements=child_elements, parent_elements=elements)
            self.attrs.append(attr)

    def creat_page_object(self , envs = 'python' , doc = 'html' , automation = 'selenium' , filename = None):

        """
        :param envs: python , java
        :param doc: html , xml
        :param automation: selenium , appium_android , appium_ios, uiautomator2_up, macaca
        :return:
        """
        if envs == 'python' and doc == 'html' and automation == 'selenium':
            self.parser_selenium_html(self.etree_elements , self.etree_elementTrees ,
                             self.elements , self.parent_elements)

        elif envs == 'python' and doc == 'xml' and automation == 'uiautomator2':
            self.parser_uiautomator_xml(self.etree_elements, self.etree_elementTrees,
                             self.elements, self.parent_elements)

        elif envs == 'python' and doc == 'xml' and automation == 'appium_android':
            self.parser_appium_android_xml(self.etree_elements, self.etree_elementTrees,
                                        self.elements, self.parent_elements)

        elif envs == 'python' and doc == 'xml' and automation == 'appium_ios':
            self.parser_appium_ios_xml(self.etree_elements, self.etree_elementTrees,
                                        self.elements, self.parent_elements)

        elif envs == 'python' and doc == 'xml' and automation == 'macaca':
            self.parser_macaca_xml(self.etree_elements, self.etree_elementTrees,
                                       self.elements, self.parent_elements)

        if envs == 'python' and len(self.attrs) > 0:
            with open('../page_object/' + filename + '.py' , 'w' , encoding='utf-8') as f:
                f.writelines('#!/user/bin/env python\n#coding=utf-8\nfrom page_object.func import func_name\n')
                f.writelines('class ' + filename.capitalize() + '(object):\n')
                f.writelines('\tdef __init__(self):\n\t\tpass\n\n')
                index = 1
                for attr in self.attrs:
                    f.writelines("\t@func_name('null')\n")
                    f.writelines("\tdef get_attr{0}(self):\n".format(str(index)))
                    f.writelines("\t\treturn {0}\n\n".format(str(attr)))
                    index += 1
                f.close()

if __name__ == '__main__':
    pass