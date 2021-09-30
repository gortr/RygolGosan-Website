# Imports Main App & Flask Components for Routing
from __main__ import app
from flask import render_template, url_for, request, redirect, flash, jsonify, make_response
import simplejson as json

# Imports OAuth Modules & 3rd Party Security Connections for Web Application
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import requests

# Reads the Google details regarding client_id, etc.
client_id = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']
application_name = "RygolGosan"



# Connects API Endpoints to Application
'''# API endpoints for all users.
@app.route('/users.json')
def userJSON():
    users = session.query(User).all()
    return jsonify(User = [u.serialize for u in users])'''