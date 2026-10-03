#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Every setting below can be overridden by an environment variable of the same name (e.g. JUDO_PASSWORD, BROKER).
# Booleans accept true/false, 1/0, yes/no, on/off.
import os

def _env_str(name, default):
    return os.environ.get(name, default)

def _env_int(name, default):
    return int(os.environ.get(name, str(default)))

def _env_bool(name, default):
    val = os.environ.get(name)
    if val is None:
        return default
    return val.strip().lower() in ("1", "true", "yes", "on")

#-------------------------------------------------------------------------------
#Judo Config
JUDO_USER = _env_str("JUDO_USER", "myjudousername")
JUDO_PASSWORD = _env_str("JUDO_PASSWORD", "myjudopassword")

#MQTT Config
BROKER = _env_str("BROKER", "192.168.1.2")                  #Broker IP
USE_MQTT_AUTH = _env_bool("USE_MQTT_AUTH", True)            #Set true, if user/pw authentification on broker, set false, if using anonymous login
MQTTUSER = _env_str("MQTTUSER", "mqttuser")                 #only required if USE_MQTT_AUTH = True
MQTTPASSWD = _env_str("MQTTPASSWD", "mosquitto")            #only required if USE_MQTT_AUTH = True
PORT = _env_int("PORT", 1883)                               #MQTT PORT, 1883 default standard

#General Config
LOCATION = _env_str("LOCATION", "my_location")              #Location of Judo device
NAME = _env_str("NAME", "Judo_isoftsaveplus")               #Name of Judo device
MANUFACTURER = _env_str("MANUFACTURER", "ShapeLabs.de")     #CC BY-NC-SA 4.0
SW_VERSION = _env_str("SW_VERSION", "2.0")
STATE_UPDATE_INTERVAL = _env_int("STATE_UPDATE_INTERVAL", 20)   #Update interval in seconds
AVAILABILITY_ONLINE = _env_str("AVAILABILITY_ONLINE", "online")
AVAILABILITY_OFFLINE = _env_str("AVAILABILITY_OFFLINE", "offline")

#Error- and warning messages of plant published to notification topic ( LOCATION/NAME/notify ). Can be used for hassio telegram bot..
LANGUAGE = _env_str("LANGUAGE", "DE")                       # "DE" / "ENG"
MQTT_DEBUG_LEVEL = _env_int("MQTT_DEBUG_LEVEL", 2)          # 0=0ff, 1=Judo-Warnings/Errors, 2=Command feedback  3=Script Errors, Exceptions
MAX_RETRIES = _env_int("MAX_RETRIES", 3)

# The maximum slider values that can be set for leakage protection can be limited here.
# The limitation can be useful to improve the handling of the sliders in the Homeassistant.
LIMIT_EXTRACTION_TIME = _env_int("LIMIT_EXTRACTION_TIME", 60)               #can setup to max 600min
LIMIT_MAX_WATERFLOW = _env_int("LIMIT_MAX_WATERFLOW", 3000)                 #can setup to max 5000L/h
LIMIT_EXTRACTION_QUANTITY = _env_int("LIMIT_EXTRACTION_QUANTITY", 500)      #can setup to max 3000L

USE_SODIUM_CHECK = _env_bool("USE_SODIUM_CHECK", True)      #'True' activates the monitoring of the sodium limit when the water hardness is set
SODIUM_INPUT = _env_int("SODIUM_INPUT", 30)                 #Sodium level of input water [mg/L]. Ask your water provider or check providers webpage
SODIUM_LIMIT = _env_int("SODIUM_LIMIT", 200)                #Sodium limit value. Default 200mg/L (Germany)

#The environment in which the script will run. Select "True" if you want to run it in the Appdeamon, or set "False" if you want to run the script on a generic Linux.
RUN_IN_APPDEAMON = _env_bool("RUN_IN_APPDEAMON", True)

#Set this Flag to True, if you've a Judo Softwell P. There are no functions for leakage protection, no battery-,salt- & softwatersensor
USE_WITH_SOFTWELL_P = _env_bool("USE_WITH_SOFTWELL_P", False)
#-------------------------------------------------------------------------------

# for Appdaemon the whole path is required "/config/appdaemon/apps/main/temp_getjudo.pkl", otherwise "temp_getjudo.pkl"
if RUN_IN_APPDEAMON == True:
    TEMP_FILE = _env_str("TEMP_FILE", "/config/apps/main/temp_getjudo.pkl")
else:
    TEMP_FILE = _env_str("TEMP_FILE", "temp_getjudo.pkl")
