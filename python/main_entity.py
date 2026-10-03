import time
import sys
import appdaemon.plugins.hass.hassapi as hass
try:
    import config_getjudo
except ModuleNotFoundError:  #no local config file -> settings from environment variables
    import config_getjudo_default as config_getjudo

class main_loop(hass.Hass):
    def initialize(self):
        import getjudo


