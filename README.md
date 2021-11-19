This is a uni project to test out making a constructor with:
- logging,
- configuration file,
- proper comments,
- test,
- database migration

The application retrieves data from Marvel API and searches for two specific characters.
Also retrieves comics list to find in which each of these characters appear.
The character serial number serves as foreign key to reference Comics and Characters tables in the database, which is also the connection for data in the code.

To start the application:
1. Open the prepareenv.py file adn run it - will install all needed dependencies,
2. Open the characterGetter.py file,
3. Run the file(it is connected to all the other files and will execute the program).
