# coding: utf-8
from __future__ import absolute_import, unicode_literals, division


def find_element_by_id(context, resource_id):
    return context.driver.find_element_by_id(resource_id)


def find_element_by_class_name(context, class_name):
    return context.driver.find_element_by_class_name(class_name)


def find_element_by_xpath(context, xpath):
    return context.driver.find_element_by_xpath(xpath)


def find_element_by_accessibility_id(context, accessibility_id):
    return context.driver.find_element_by_accessibility_id(accessibility_id)


def back(context):
    return context.driver.back()
