# Gopavasanth
# Date : 05/05/2018
from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

import auth
def get_labels():
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])

SCOPES = 'https://mail.google.com/'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Quickstart'
authInst = auth.auth(SCOPES,CLIENT_SECRET_FILE,APPLICATION_NAME)
credentials = authInst.get_credentials()

http = credentials.authorize(httplib2.Http())
service = discovery.build('gmail', 'v1', http=http)

<<<<<<< HEAD
my_file = open("file.txt", "r")

import send_email

sendInst = send_email.send_email(service)
#message = sendInst.create_message_with_attachment('gopavasanth1999@gmail.com','p.bhanuprakash12345@gmail.com','Hello_API',my_file.read(), 'image.jpg' )
message = sendInst.create_message('gopavasanth1999@gmail.com','manikishanghantasala@gmail.com', 'Hello_API',my_file.read())
sendInst.send_message('me',message)
my_file.close()
=======
import send_email

sendInst = send_email.send_email(service)
message = sendInst.create_message_with_attachment('gopavasanth1999@gmail.com','sreejithsankar55@gmail.com','Hello_API','Hi there, This is Gopa Vasanth', 'image.jpg' )
sendInst.send_message('me',message)
>>>>>>> c08a102038e0280024cb93b535eaec0dbd14398b
