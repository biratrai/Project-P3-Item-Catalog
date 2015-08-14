
from flask import flash, make_response
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json

import requests
import db_helper

CLIENT_ID = json.loads(
  open('Catalog/client_secrets.json', 'r').read())['web']['client_id']

def google_connect(request,login_session):
  ''' Connect to Google Login'''  
  #Validate state token 
  if request.args.get('state') != login_session['state']:
    response = make_response(json.dumps('Invalid state parameter.'), 401)
    response.headers['Content-Type'] = 'application/json'
    return response

  #Obtain authorization code
  code = request.data

  try:
    # Upgrade the authorization code into a credentials object
    oauth_flow = flow_from_clientsecrets('Catalog/client_secrets.json', scope='')
    oauth_flow.redirect_uri = 'postmessage'
    credentials = oauth_flow.step2_exchange(code)

  # Throw the Error if the authorization code fails
  except FlowExchangeError:
    response = make_response(json.dumps('Failed to upgrade the authorization code.'), 401)
    response.headers['Content-Type'] = 'application/json'
    return response

  # Check that the access token is valid.
  access_token = credentials.access_token
  url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'% access_token)
  h = httplib2.Http()
  result = json.loads(h.request(url, 'GET')[1])

  # If there was an error in the access token info, abort.
  if result.get('error') is not None:
    response = make_response(json.dumps(result.get('error')), 500)
    response.headers['Content-Type'] = 'application/json'

  # Verify that the access token is used for the intended user.
  gplus_id = credentials.id_token['sub']
  if result['user_id'] != gplus_id:
    response = make_response(json.dumps("Token's user ID doesn't match given user ID."), 401)
    response.headers['Content-Type'] = 'application/json'
    return response

  # Verify that the access token is valid for this app.
  if result['issued_to'] != CLIENT_ID:
    response = make_response(json.dumps("Token's client ID does not match app's."), 401)
    response.headers['Content-Type'] = 'application/json'
    return response

  # Check to see if user is already logged in
  stored_credentials = login_session.get('credentials')
  stored_gplus_id = login_session.get('gplus_id')
  if stored_credentials is not None and gplus_id == stored_gplus_id:
    response = make_response(json.dumps('Current user is already connected.'),200)
    response.headers['Content-Type'] = 'application/json'
    return response

  # Store the access token in the session for later use.
  login_session['credentials'] = credentials
  login_session['gplus_id'] = gplus_id

  #Get user info
  userinfo_url =  "https://www.googleapis.com/oauth2/v1/userinfo"
  params = {'access_token': credentials.access_token, 'alt':'json'}
  answer = requests.get(userinfo_url, params=params)

  data = answer.json()
  login_session['provider'] = 'google'
  login_session['username'] = data['name']
  login_session['picture'] = data['picture']
  login_session['email'] = data['email']

  # see if user exists
  user_id = db_helper.getUserID(login_session['email'])
  if not user_id:
    user_id = db_helper.createUser(login_session)
  login_session['user_id'] = user_id
  print login_session['user_id']

  output = ''
  output +='<h1>Welcome, '
  output += login_session['username']
  output += '!</h1>'
  output += '<img src="'
  output += login_session['picture']
  output +=' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
  flash("You are now logged in as %s"%login_session['username'])
  return output

def google_disconnect(login_session):
  print "google_disconnect"
  ''' Disconnect from Google Login'''  
  # Only disconnect a connected user.
  credentials = login_session.get('credentials')
  if credentials is None:
    response = make_response(json.dumps('Current user not connected.'), 401)
    response.headers['Content-Type'] = 'application/json'
    return response

  # Execute HTTP GET request to revoke current token.
  access_token = credentials.access_token
  url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
  h = httplib2.Http()
  result = h.request(url, 'GET')[0]

  if result['status'] == '200':
    # Reset the user's session.
    response = make_response(json.dumps('Successfully disconnected.'), 200)
    response.headers['Content-Type'] = 'application/json'
    return response
  else:
    # For whatever reason, the given token was invalid.
    response = make_response(
        json.dumps('Failed to revoke token for given user.', 400))
    response.headers['Content-Type'] = 'application/json'
    return response

def fb_connect(request,login_session):
  if request.args.get('state') != login_session['state']:
    response = make_response(json.dumps('Invalid state parameter.'), 401)
    response.headers['Content-Type'] = 'application/json'
    return response
  access_token = request.data

  #Exchange client token for long-lived server-side token
  # GET /oauth/access_token?grant_type=fb_exchange_token&client_id={app-id}&client_secret={app-secret}&fb_exchange_token={short-lived-token} 
  app_id = json.loads(open('Catalog/fb_client_secrets.json', 'r').read())['web']['app_id']
  app_secret = json.loads(open('Catalog/fb_client_secrets.json', 'r').read())['web']['app_secret']
  url = 'https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=%s&client_secret=%s&fb_exchange_token=%s' % (app_id,app_secret,access_token)
  h = httplib2.Http()
  result = h.request(url, 'GET')[1]

  #Use token to get user info from API 
  userinfo_url =  "https://graph.facebook.com/v2.2/me"

  #strip expire tag from access token
  token = result.split("&")[0]

  url = 'https://graph.facebook.com/v2.2/me?%s' % token
  h = httplib2.Http()
  result = h.request(url, 'GET')[1]
  print "result\n",result

  data = json.loads(result)
  print "\ndata\n",type(data),data
  login_session['provider'] = 'facebook'
  login_session['username'] = data["name"]
  login_session['email'] = data["name"]+"@facebook.com"
  login_session['facebook_id'] = data["id"]

  # The token must be stored in the login_session in order to properly logout, let's strip out the information before the equals sign in our token
  stored_token = token.split("=")[1]
  login_session['access_token'] = stored_token

  #Get user picture
  url = 'https://graph.facebook.com/v2.2/me/picture?%s&redirect=0&height=200&width=200' % token
  h = httplib2.Http()
  result = h.request(url, 'GET')[1]
  data = json.loads(result)

  login_session['picture'] = data["data"]["url"]
    
  # see if user exists
  user_id = db_helper.getUserID(login_session['email'])
  if not user_id:
    user_id = db_helper.createUser(login_session)
  login_session['user_id'] = user_id

  output = ''
  output +='<h1>Welcome, '
  output += login_session['username']

  output += '!</h1>'
  output += '<img src="'
  output += login_session['picture']
  output +=' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '

  flash ("Now logged in as %s" % login_session['username'])
  return output

def fb_disconnect(login_session):
  print "fb_disconnect"
  facebook_id = login_session['facebook_id']

  # The access token must me included to successfully logout
  access_token = login_session['access_token']
  # url = 'https://graph.facebook.com/%s/permissions' % (facebook_id,access_token)
  url = 'https://graph.facebook.com/{0}/permissions'.format(facebook_id,access_token)
  h = httplib2.Http()
  result = h.request(url, 'DELETE')[1]
  output = "You have been logged out successfully !"
  return output


  