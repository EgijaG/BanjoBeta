from DataBase import addComicsDataToMng, addComicsToDB, addDataToCharacterTable, addDataToMngChars, createTables
from Logger import getLogger
from marvel import Marvel
from ConfReader import readConfig


# Creating the logger
logger = getLogger(__name__)
logger.info('Marvel comics data retrieval service')

# MCU Character name
charName = ''
# List of comics where charName participated
comicList = dict()


def checkConfigandAPI():
    try:
        config = readConfig()
        config.read('config.ini')
        marvel_pub_key = config.get('marvel_config', 'PUB_KEY')
        marvel_priv_key = config.get('marvel_config', 'PRIV_KEY')

        m = Marvel(marvel_pub_key, marvel_priv_key)
        characters = m.characters
    except:
        logger.exception('')
    logger.info(
        'Succesfully read configuration and established connection with API')

    charBegin = 'Winter'
    charBegin2 = 'Black widow'
    all_characters = characters

    # Serial code for the character
    wintSId = getCharacter(charBegin, all_characters)
    # Getting where this character appears in comics
    getWhereCharacterParticipated(characters, wintSId)
    # Serial code for the character
    print('-----------------------------------------------')
    bWId = getCharacter(charBegin2, all_characters)
    # Getting where this character appears in comics
    getWhereCharacterParticipated(characters, bWId)


# Getting the characters form Marvel Cinematic Universe(MCU) by the name provided when the fucntion is called
def getCharacter(nameStartsW, all_char):
    global charName
    all_char = all_char.all(nameStartsWith=nameStartsW)
    for i in range(len(all_char['data']['results'])):
        name = all_char['data']['results'][i]['name']
        charName = name
        id = charName = all_char['data']['results'][i]['id']
        # Adding found data to table in DB
        addDataToCharacterTable(name, id)
        addDataToMngChars(id, name)
        return all_char['data']['results'][i]['id']
    logger.info('Succesfully inserted data into table Characters')


# Getting the comics where this particular character has appeared in
def getWhereCharacterParticipated(characters, charId):
    all_char = characters.comics(charId)
    print('The ', charName, ' appears on: ')
    for i in range(len(all_char['data']['results'])):
        item = all_char['data']['results'][int(i)]['title']
        id = all_char['data']['results'][int(i)]['id']
        addComicsToDB(id, item, charId)
        addComicsDataToMng(id, item, charId)
    logger.info('Succesfully inserted data into table Comics')


# calling the first method that creates a chain reaction for the rest
createTables()
checkConfigandAPI()
