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

charName = ""
comicList = dict()


def checkConfigandAPI():
    try:
        config = ConfigParser()
        config.read('config.ini')

        marvel_pub_key = config.get('marvel_config', 'PUB_KEY')
        marvel_priv_key = config.get('marvel_config', 'PRIV_KEY')

        m = Marvel(marvel_pub_key, marvel_priv_key)
        characters = m.characters
    except:
        logger.exception('')
    logger.info(
        'Succesfully read configuration and established connection with API')

    charBegin = "Captain America"
    all_characters = characters

    # Serial code for the character
    wintSId = getCharacters(charBegin, all_characters)
    getWhereCharacterParticipated(characters, wintSId)
    print(comicList)


# Getting the characters form Marvel Cinematic Universe(MCU) by the name provided when the fucntion is called
def getCharacters(nameStartsW, all_char):
    global charName
    all_char = all_char.all(nameStartsWith=nameStartsW)
    for i in range(len(all_char['data']['results'])):
        print(all_char["data"]["results"][i]["id"],
              all_char["data"]["results"][i]["name"])
        charName = all_char["data"]["results"][i]["name"]
        return all_char["data"]["results"][i]["id"]

# Getting the comics where this particular character has appeared in


def getWhereCharacterParticipated(characters, charId):
    all_char = characters.comics(charId)
    print("The " + charName + " is seen on: ")
    for i in range(len(all_char['data']['results'])):
        print(all_char['data']['results'][int(i)]['title'])
        item = {(all_char['data']['results'][int(i)]['title']): int(i)}
        comicList.update(item)


# calling the first method
checkConfigandAPI()
