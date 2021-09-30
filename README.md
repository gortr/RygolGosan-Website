# RygolGosan Project
**Author:** Rigoberto Gort
**Date:** 09/30/2021

## Project Info
**Filename** 

README.md

**Main Project File:**

`app.py`

**Connected Backend Files**

`models.py`
`routes.py`
`api.py`

**Connected Module Files** 

`database_seeding.py`

**Connected HTML Files** 

`base.html`
`features.html`
`gettingstarted.html`
`header.html`
`home.html`
`login.html`
`publichome.html`
`register.html`

**Connected CSS Files** 

`main.css`

**Connected JS Files** 



### Configuration Instructions
`app.py`

This is the primary file required in order to run the EVE Fleet-Up application.

This file imports the data that was setup in the sitedatabase.db file from database_seeding.py.

### Operating Instructions
Please confirm that you have the following installed on your machine:

- Virtual Box (https://www.virtualbox.org/wiki/Downloads)
- Python 3 (https://www.python.org/downloads/)
- Flask (https://flask.palletsprojects.com/en/1.1.x/)
- SQLite (https://sqlite.org/index.html)
- SQLalchemy (https://www.sqlalchemy.org/download.html)
- WTForms (pip install wtforms[email])
- OAuth2Client (https://pypi.org/project/oauth2client/)
- Git (https://git-scm.com/)

For example, if you are using the standard Python IDLE  (GUI) then you would open the file in that environment. 

You would need to,

1. Verify that you have the required files installed in a directory of your choosing.
2. Verify that you are in that directory and run `source venv/Scripts/activate` in the CMD or Terminal.
3. Once there make sure to run the `python database_seeding.py` file. (Make sure sitedatabase.db does not exist first)
4. Afterwards make sure to run the feed the database information to test including a valid email and username which would tie into your Google Account.
5. Run `python3 app.py`.
6. The localhost server should now be live for debugging, etc.
7. Open a browser and enter `localhost:5000`
8. Test the database to your hearts content!
