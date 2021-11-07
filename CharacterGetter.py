
from asyncio.log import logger
from configparser import ConfigParser
from marvel import Marvel


config = ConfigParser()
config.read('config.ini')
try:
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
