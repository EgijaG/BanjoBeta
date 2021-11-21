
from dis import code_info
from genericpath import exists
import os
import pymongo
from marvel import Marvel
from ConfReader import readConfig

print('Configuration file test')


# Testing whther the file exists in the working dir
print('-------------------')
print('Checking if the config file exists >>>')
assert os.path.isfile('config.ini') == True
print('OK')
print('-------------------')

# Opening the config file
config = readConfig()
config.read('config.ini')

# Checking whether the configuration has the data neccesary to connect to Marvel API
print('-------------------')
print('Checking Marvel API data in config >>>')
assert config.has_option('marvel_config', 'PUB_KEY') == True
assert config.has_option('marvel_config', 'PRIV_KEY') == True
print('OK')
print('-------------------')

# Checking whether config contains the data needed for data migration to mongoDB
print('-------------------')
print('Checking Mongo DB data in config >>>')
assert config.has_option('mongodb_config', 'mng_user') == True
assert config.has_option('mongodb_config', 'mng_pass') == True
print('OK')
print('-------------------')

# Checking whether the data from API is accesible
print('-------------------')
print('Checking  Marvel API data receival >>>')
marvel_pub_key = config.get('marvel_config', 'PUB_KEY')
marvel_priv_key = config.get('marvel_config', 'PRIV_KEY')
m = Marvel(marvel_pub_key, marvel_priv_key)
assert m.characters != None
print('OK')
print('-------------------')

# Checking Mongo DB connection
print('-------------------')
print('Checking Mongo DB connection >>>')
mng_user = config.get('mongodb_config', 'mng_user')
mng_pass = config.get('mongodb_config', 'mng_pass')
myclient = pymongo.MongoClient(
    f'mongodb+srv://{mng_user}:{mng_pass}@marvel.lh0ot.mongodb.net/Marvel?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE')
srvData = myclient.admin.command('ismaster')
assert srvData['ismaster'] == True
print('OK')
print('-------------------')

# Checking the log file config file existence
print('-------------------')
print('Checking if characterGetter log config file exists(log_characterGetter.yaml) >>>')
assert os.path.isfile('log_characterGetter.yaml') == True
print('OK')
print('-------------------')

print('-------------------')
print('Checking if characterGetter log config file exists(log_DataBase.yaml) >>>')
assert os.path.isfile('log_DataBase.yaml') == True
print('OK')
print('-------------------')

print('-------------------')
print('Checking if DataBase log config file exists(log_characterGetter.yaml) >>>')
assert os.path.isfile('log_characterGetter.yaml') == True
print('OK')
print('-------------------')

print('-------------------')
print('Checking if log directory exists >>>')
assert os.path.isdir('log') == True
print('OK')
print('-------------------')

print("Configuration file test DONE -> ALL OK")
print("----------------------------------------")