import logging


def getLogger(name, log_config=None):
    # Time and data formats
    timeFmt = ("%(asctime)s;%(levelname)s;%(message)s")
    dateFmt = ("%d %b %Y %H:%M:%S")

    # logging config
    logging.basicConfig(filename=name+'.log', encoding='utf-8',
                        level=logging.INFO, format=timeFmt, datefmt=dateFmt)

    # return the prepared logger object
    return logging.getLogger(name)
