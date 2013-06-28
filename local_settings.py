'''
Configuration Settings

Includes keys for Twilio, etc.  Second stanza intended for Heroku deployment.
'''

# Uncommet to configure in file.
ACCOUNT_SID = "ACcc98d19ac4bb0450414bcfa5b9646bdf" 
AUTH_TOKEN = "b932d892aed48ec7962f8eded73cf670"
BSSSPAM_APP_SID = "APc4c905b4a7abafb27c4a09a530a0ed23"
BSS_SPAM_ID = "+17819169659"


# Begin Heroku configuration - configured through environment variables.
import os
ACCOUNT_SID = os.environ['ACCOUNT_SID']
AUTH_TOKEN = os.environ['AUTH_TOKEN']
BSSSPAM_APP_SID = os.environ['BSSSPAM_APP_SID']
BSS_SPAM_ID = os.environ['BSS_SPAM_ID']
