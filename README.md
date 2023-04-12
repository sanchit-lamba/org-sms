# ORG-SMS
This repo contains code that exports org-agenda from emacs and send the text as an sms using twilio api
# Introduction
This project attempts to create a simple and easy way to export org-agenda and send it as an sms to your phone so there is no need to use an extra app to sync the org files manage file conflicts
# Requirements
* Bash shell
* Python
* emacs and org mode
# Usage
1. Replace the required values in [twilio-api.py](twilio-api.py) with the auth token and the number you intend to send messages to
2. Run [bash.sh](bash.sh) it will export the agenda to a new file and trigger all other python scripts 

It's recommended to set up a cron job to run [bash.sh](bash.sh) at a specific time so that you can run this script at a specific time of the day to get consistant updates

NOTE: you can only send sms to the number you registered with on twilio on a free account
