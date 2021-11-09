from configparser import ConfigParser
import os.path
from Logger import getLogger

logger = getLogger(__name__)


def readConfig():
    logger.info('Checking whether the config file exists')
    if(os.path.exists('config.ini')):
        config = ConfigParser()
        return config
    logger.info('Succesfully read config file')
