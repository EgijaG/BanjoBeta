import yaml
import logging.config


def getLogger(name, log_config=None):
    # logging config
    with open('./log_characterGetter.yaml', 'r') as stream:
        log_config = yaml.safe_load(stream)
        logging.config.dictConfig(log_config)

    # return the prepared logger object
    return logging.getLogger(name)



