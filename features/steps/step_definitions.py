# coding: utf-8
from __future__ import absolute_import, unicode_literals, division

from time import sleep

from behave import step

from features.steps.common_functions import (
    find_element_by_id
)


@step("Page should have continue button")
def user_click_continue_button(context):
    sleep(5)
    continue_button = find_element_by_id(context, 'nambafood.nambaapps.kg.food:id/close')
    continue_button.click()


