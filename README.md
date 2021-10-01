# RygolGosan Project
**Author:** Rigoberto Gort
**Date:** 10/01/2021

## Project Info
**Filename** 

README.md

**Main Project File:**

`app.py`

**Connected Backend Files**

`api.py`
`routes.py`
`models.py`

**Connected Module Files** 

`database_seeding.py`

**Connected HTML Files** 

`base.html`
`features.html`
`gettingstarted.html`
`header.html`
`index.html`
`login.html`
`publicindex.html`
`signup.html`

**Connected CSS Files** 

`main.css`

**Connected JS Files** 



### Configuration Instructions
`app.py`

This is the primary file required in order to run the RygolGosan-Website application.

This file imports the data that was setup in the sitedatabase.db file from database_seeding.py.

### Operating Instructions
Please confirm that you have the following installed on your machine:

- Virtual Box (https://www.virtualbox.org/wiki/Downloads)
- Python 3 (https://www.python.org/downloads/)
- Git (https://git-scm.com/)


### Python3 Dependencies
- VirtualEnv (https://docs.python.org/3/library/venv.html)
- Flask (https://flask.palletsprojects.com/en/1.1.x/)
- SQLite (https://sqlite.org/index.html)
- SQLalchemy (https://www.sqlalchemy.org/download.html)
- WTForms (pip install wtforms[email])
- WTForms (https://wtforms.readthedocs.io/en/2.3.x/)
- OAuth2Client (https://pypi.org/project/oauth2client/)
- Bcrypt (https://pypi.org/project/bcrypt/)
- Flask_Login LoginManager (https://flask-login.readthedocs.io/en/latest/)


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
