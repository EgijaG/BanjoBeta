import certifi
import pymongo
import sqlite3
from ConfReader import readConfig

from Logger import getLogger

logger = getLogger(__name__)

# Reading config file
try:
    config = readConfig()
    config.read('config.ini')
    password = config.get('mysql_config', 'DB_PASS')
    url = config.get('mysql_config', 'DB_URL')
    user = config.get('mysql_config', 'DB_USER')
    mng_user = config.get('mongodb_config', 'mng_user')
    mng_pass = config.get('mongodb_config', 'mng_pass')
except:
    logger.exception('')
logger.info("Configuration succesfully read")

# SQLite variables
con = sqlite3.connect('Marvel-sqlite')
cur = con.cursor()
ca = certifi.where()

# MongoDB variables
myclient = pymongo.MongoClient(
    f'mongodb+srv://{mng_user}:{mng_pass}@marvel.lh0ot.mongodb.net/Marvel?retryWrites=true&w=majority')
logger.info(
    "Connecting to: "f'mongodb+srv://{mng_user}:{mng_pass}@marvel.lh0ot.mongodb.net/Marvel?retryWrites=true&w=majority')

mydb = myclient["Marvel"]
mycol = mydb["Marvel"]


def getMongoData():
    mnData = mycol.find({})
    return mnData


def addDataToCharacterTable(charName, id):
    try:
        cur.execute(
            'INSERT INTO Characters (ID,name) VALUES (?,?)', (id, charName))
        con.commit()
    except sqlite3.Error as e:
        print('Problem with inserting data into the table - ', e)
        logger.exception('')
    logger.info('Succesfully inserted data into table Characters')


def addComicsToDB(id, comicName, charID):
    try:
        cur.execute(
            'INSERT INTO Comics (ID,title,characterID) VALUES (?,?,?)', (id, comicName, charID))
        con.commit()
    except sqlite3.Error as e:
        print('Problem with inserting data into the table - ', e)
        logger.exception('')
    logger.info('Succesfully inserted data into table Comics')


def addDataFromMng():
    logger.info(
        'Adding data to local database from the database that is located online')
    data = getMongoData()
    for d in data:
        addDataToCharacterTable(d.get("ID"), d.get("name"))
        addComicsToDB(d.get('ID'), d.get('title'), d.get('characterID'))


def createTables():
    try:
        logger.info("Creating a table, trying to execute query.")
        cur.execute(
            'CREATE TABLE Characters(ID INTEGER PRIMARY KEY NOT NULL UNIQUE, name TEXT NOT NULL UNIQUE);')
        cur.execute('CREATE TABLE Comics(ID INTEGER PRIMARY KEY NOT NULL UNIQUE, title TEXT NOT NULL UNIQUE, characterID INTEGER NOT NULL, FOREIGN KEY(characterID) REFERENCES Characters(ID));')
        addDataFromMng()
    except sqlite3.Error as e:
        logger.exception('')
        print(e)
        cur.execute('DELETE FROM Characters')
        cur.execute('DELETE FROM Comics')
        con.commit()
    logger.info("The tables have been created succesfully!")

# Not the smartest way to handle the data insert with two equal methods, but I can't figure it out yet


def addDataToMngChars(id, name):
    global isDataThere
    isDataThere = False
    data = getMongoData()

    for d in data:
        if(d.get("ID") == id):
            isDataThere = True
            print(d.get('ID'))
    if(isDataThere == False):
        mngdata = {'ID': id, 'name': name}
        a = mycol.insert_one(mngdata)
        addDataToCharacterTable(name, id)
    logger.info('Data insertion into Mongo DB - successfull')


def addComicsDataToMng(id, title, charId):
    global isDataThere
    isDataThere = False
    data = getMongoData()

    for d in data:
        if(d.get("ID") == id):
            isDataThere = True
            print(d.get("title"))
    if(isDataThere == False):
        mngdata = {'ID': id, 'title': title, 'characterID': charId}
        mycol.insert_one(mngdata)
        addComicsToDB(id, title, charId)
    logger.info('Data insertion into Mongo DB - successfull')
