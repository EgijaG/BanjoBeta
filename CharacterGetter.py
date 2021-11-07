import logging
import logging.config
import yaml
from configparser import ConfigParser
from marvel import Marvel

# Loading the loggin config
with open('log_characterGetter.yaml', 'r') as stream:
    config = yaml.safe_load(stream)
logging.config.dictConfig(config)

# Creating the logger
logger = logging.getLogger('root')
logger.info("Marvel comics data retrieval service")


try:
    config = ConfigParser()
    config.read('config.ini')

    marvel_pub_key = config.get('marvel_config', 'PUB_KEY')
    marvel_priv_key = config.get('marvel_config', 'PRIV_KEY')

    m = Marvel(marvel_pub_key, marvel_priv_key)
    characters = m.characters
except:
    logger.exception('')
logger.info('DONE')

x = 1011335
for i in range(0, 10):
    all_cahracters = characters.comics(x)
    for a in range(1, 12):
        print(all_cahracters['data']['results'][int(a)]['title'])
