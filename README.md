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
1. Clone this repo - git clone ...,
2. cd to the repo,
3. git flow init
4. ./prepareDevEnv.sh or on mac bash prepareDevEnv.sh
3. Run the command the script shows.

Have fun! :)
