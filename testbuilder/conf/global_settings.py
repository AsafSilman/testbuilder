"""
Global configuration file with all default vaues
"""

import os
import logging

# Collection of installed interfaces
# 
# Structure
# Key: Interface prefix
# Value: Interface location
# 
# Example
# {"Basic": "testbuilder.interface.basic"}
INSTALLED_INTERFACES = {
    "basic": "testbuilder.interface.basic",
    "selenium": "testbuilder.interface.selenium"
}

INSTALLED_MIDDLEWARES = {
    "basic": "testbuilder.middleware.basic",
    "objectmap": "testbuilder.middleware.objectmap",
    "logging": "testbuilder.middleware.logging"
}

INSTALLED_OBJECTMAPS_PARSERS = {
    "python": "testbuilder.objectmap.python"
}

INSTALLED_TESTLOADERS = {
    "yaml": "testbuilder.loader.yamlloader"
}

INSTALLED_PROFILES = {
    "default": {
        "middlewares": [
            "basic",
            "objectmap",
            "logging"
        ]
    }
}

OBJECT_MAPS = {
    "basic": ("python", "testbuilder.objectmap.static.objectmap")
}

####################################################
# Logging Settings
####################################################

LOG_LEVEL = logging.INFO

####################################################
# Application Settings
####################################################

APP_DIRECTORY = ""
APP_NAME = ""
APP_LOGIN = {
    "username": "rmo_user",
    "password": "rmo_pass"
}

####################################################
# Selenium Interface Settings
####################################################
SELENIUM_DRIVER_BASE_PATH = os.environ.get("SELENIUM_DRIVER_BASE_PATH")

SELENIUM_CHROME_DRIVER = "chromedriver"
SELENIUM_CHROME_VERSION = (2,25)

SELENIUM_FIREFOX_DRIVER = "geckodriver"
SELENIUM_FIREFOX_VERSION = (0,21)

SELENIUM_IMPLICIT_WAIT = 10 # Seconds

SELENIUM_RETRY_ATTEMPTS = 5
