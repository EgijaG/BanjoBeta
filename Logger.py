import logging.config
import yaml


def getLogger(name, log_config=None):
    # Time and data formats
    timeFmt = ("%(asctime)s;%(levelname)s;%(message)s")
    dateFmt = ("%d %b %Y %H:%M:%S")

    # logging config
    with open('./log_characterGetter.yaml', 'r') as stream:
        config = yaml.safe_load(stream)

        logging.config.dictConfig(config)

    # return the prepared logger object
    return logging.getLogger(name)
