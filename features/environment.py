# coding: utf-8
from __future__ import absolute_import, unicode_literals, division

import os
from time import sleep
from datetime import datetime
from appium import webdriver

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
apk = os.path.join(BASE_DIR, 'apk/NambaFood_2.10.0.apk')


def make_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)


def before_scenario(context, scenario):
    sleep(5)
    pass


def after_scenario(context, scenario):
    # Runs after each scenario
    if scenario.status == 'failed':
        scenario_error_dir = os.path.join(BASE_DIR, 'feature_errors')
        make_dir(scenario_error_dir)
        if os.name == 'nt':
            screenshot_name = '%s\last_failed_scenario_%s.png' % (scenario_error_dir, datetime.now())
        else:
            screenshot_name = '%s/last_failed_scenario_%s.png' % (scenario_error_dir, datetime.now())
        context.driver.save_screenshot(screenshot_name)
        screen = "Screenshot saved to %s" % (screenshot_name)
        print (screen)


def before_feature(context, feature):
    # Runs before each feature file
    pass


def after_feature(context, feature):
    # Runs after each feature
    pass


def before_all(context):
    context.config.setup_logging()
    context.driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723/wd/hub',
        desired_capabilities={
            'app': apk,
            'platformName': 'Android',
            'platformVersion': '7.1.1',
            'deviceName': 'Android Emulator',
            'avd': 'Nexus_5X_API_25'
        })


def after_all(context):
    # Very last thing to run.
    context.driver.quit()
